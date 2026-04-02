---
name: skill-mcp-check
description: Use when starting any task to check if available skills and MCPs are sufficient, and search for missing ones to recommend to the user
---

# Skill/MCP Check

## Overview

Use a subagent to enumerate tools, analyze gaps, and recommend missing skills/MCPs. Approved skills are loaded automatically; MCPs require manual installation.

## When to Use

Manually invoke via `/skill-mcp-check` when:
- Task requires tools outside your immediate knowledge
- New domain, unfamiliar technology, or unclear approach
- You want to ensure you have the best tools before starting

**When NOT to invoke:** If you already know exactly what tools you need and they're available, skip this.

## The Sufficiency Check Process

### Step 1: Spawn Gap Analysis Subagent

Use `Agent` tool to spawn a subagent. The subagent must ONLY do gap analysis — **do NOT execute the task**.

**Critical constraint:** The subagent's ONLY job is to analyze whether available tools are sufficient. It must NOT:
- Search for actual results
- Download anything
- Generate reports about the task content
- Perform any task-related work

### Step 2: Await Subagent Results

Wait for the subagent to complete and return its gap analysis report.

### Step 3: Present Recommendations to User

If subagent found gaps:
1. Present the recommendation list clearly
2. Ask user which ones to approve

### Step 4: Load Approved Tools

For each user-approved recommendation:

**For Skills:**
- Use `Skill` tool to load: `Skill(skill="skill-name")`
- Confirm loading to user

**For MCPs:**
- Provide configuration instructions for the user to install manually
- MCP installation is done by the user, not automated

### Step 5: Proceed or Confirm

After loading approved tools:
- Confirm to user what was loaded
- Ask for permission to proceed with the task

## Recommendation Format

```
**Recommended:** [Name]
**Type:** Skill / MCP
**Purpose:** [What it does in 1-2 sentences]
**How to load:**
  - Skill: /[skill-name] or Skill tool
  - MCP: [configuration steps for user]
**Why it helps:** [Specific gap it fills]
```

## What NOT To Do

- ❌ Don't execute the task before checking tools
- ❌ Don't auto-install MCPs (user must install manually)
- ❌ Don't skip subagent enumeration
- ❌ Don't load skills without user approval
- ❌ Don't over-recommend — only gaps that actually matter
- ❌ **The subagent must NOT execute the task — gap analysis ONLY**

## Subagent Prompt Template

When spawning the subagent, use this EXACT template:

```markdown
## MISSION: Gap Analysis ONLY — Do NOT execute the task

You are analyzing whether available tools are sufficient for a task.
Your ONLY output is a gap analysis report.
Do NOT search for results, download files, or do any task-related work.

### Task to analyze:
[Insert user's task here]

### Your process (STOP after Step 5):
1. List ALL skills available by name from your context
2. Call ListMcpResourcesTool with NO parameters
3. From the full list, identify which tools are relevant to the task
4. Assess sufficiency **based on the task's goal**
5. Return structured gap analysis report (DO NOT execute task)

### Critical: Understanding the Task Goal

**Before assessing gaps, understand what the task is asking:**

- If the task IS to research/discover tools or techniques → having those tools already would defeat the purpose. Focus on **research/discovery tools**, not the tools being researched.
- If the task IS to build/deploy something → then missing implementation tools ARE gaps.
- If the task IS to analyze/understand code → then code analysis tools are relevant.

**Example for OSINT research task:**
- Task goal: "research OSINT tools and techniques"
- What IS needed: search, discovery, reading, analysis tools
- What is NOT a gap: "no OSINT framework" — having one would defeat the research goal
- Real gap: "no PDF parser" — can't analyze PDF documents

### Gap Assessment Rules

A gap is ONLY a gap if:
- The tool is needed to ACCOMPLISH the task
- The tool is not already available
- The tool being researched is not itself the task goal

**Common mistakes to avoid:**
- ❌ "No [X] framework" when the task IS to research [X]
- ❌ "Can't search GitHub" when search skills are available
- ❌ "Can't clone repos" when git/bash is available

### Report format:
## Available Tools
[table: Capability | Tool | Status]

## Gaps Found
[what's missing]

## Recommendations
[each with: name, type, purpose, how to load, why it helps]

### STOP HERE — Do not proceed beyond this point
```

## Red Flags — Subagent Must NOT

- ❌ Start searching for actual results
- ❌ Download files or code
- ❌ Generate reports about the task content
- ❌ Perform any work beyond gap analysis
- ❌ Continue past the gap analysis report

**If you catch yourself wanting to "help by doing the task" — STOP. Return the gap analysis report instead.**
