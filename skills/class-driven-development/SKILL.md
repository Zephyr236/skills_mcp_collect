---
name: class-driven-development
description: Use when planning a project in plan mode that involves multiple classes or modules - guides class-first decomposition with white-box and black-box testing per unit before proceeding
---

# Class-Driven Development

## Overview

Decompose project into independent classes, implement each one with white-box and black-box testing before moving to the next. Only proceed when all tests pass. Assembly is handled separately after skill completes.

## When to Use

**Plan Mode 中自动加载。** 适用于任何需要拆分为多个类/模块的项目开发。

**触发特征：**
- 开始新项目规划
- 项目涉及多个类或模块协作
- 需要明确的测试策略

**不适用于：**
- 单个简单函数/脚本
- 已确定不需要拆分的小工具

## Core Workflow

```dot
digraph class-driven-dev {
    rankdir=LR;
    "Plan Mode" -> "类详细设计"
    "类详细设计" -> "测试计划（白盒+黑盒）"
    "测试计划" -> "用户确认"
    "用户确认" -> "实现类"
    "实现类" -> "白盒测试计划"
    "白盒测试计划" -> "用户确认"
    "用户确认" -> "白盒测试执行"
    "白盒测试执行" -> "黑盒测试计划"
    "黑盒测试计划" -> "用户确认"
    "用户确认" -> "黑盒测试执行"
    "黑盒测试执行" -> [color=green,label="全部通过"]
    "全部通过" -> "清理测试文件"
    "清理测试文件" -> "下一个类" -> ...
    "最后一个类完成" -> "Skill 结束"
}
```

## Planning Phase

### 1. 类详细设计

对每个类必须记录完整信息：

**类名：** `{ClassName}`
**文件位置：** `{filepath}`
**职责描述：** `{这个类是干什么的，实现什么功能，详细描述}`

**公开接口：**
| 方法 | 参数 | 返回值 | 功能描述 |
|------|------|--------|----------|
| `method1` | `param` | `return` | `做什么` |

**依赖关系：**
- 依赖哪些类：`DependencyA`, `DependencyB`
- 被哪些类依赖：`DependentC`

**内部实现要点：**
- 关键数据结构
- 状态机/状态转换
- 异常处理分支

### 2. 测试计划

**白盒测试计划：**
- 测试目标：验证 `{class_name}` 内部实现
- 边界条件：哪些需要测试
- 异常路径：哪些需要 assertRaises
- Mock 策略：依赖如何 mock

**黑盒测试计划：**
- 测试目标：验证 `{class_name}` 外部行为
- 输入输出：正常流程验证
- 边界值：边界条件测试
- 错误处理：异常输入处理

### 3. 用户确认

**每个计划阶段必须让用户确认后再执行：**
- 类设计确认 → 才实现类
- 白盒计划确认 → 才执行白盒测试
- 黑盒计划确认 → 才执行黑盒测试

**计划格式（展示给用户）：**
```
## {ClassName} 测试计划

### 白盒测试
**目标：** {描述}
**用例：** {列表}
**Mock：** {方式}

### 黑盒测试
**目标：** {描述}
**用例：** {列表}
```

用户输入「确认」或「ok」后继续。

## Execution Phase

每个类的开发循环：

```
实现类 → 白盒计划 → 确认 → 白盒测试 → 黑盒计划 → 确认 → 黑盒测试 → 清理 → 下一个类
```

### 调度 Agent

**白盒测试：**
```
Agent(
    subagent_type="general-purpose",
    prompt=Read("~/.claude/skills/class-driven-development/white-box-agent.md")
)
```

**黑盒测试：**
```
Agent(
    subagent_type="general-purpose",
    prompt=Read("~/.claude/skills/class-driven-development/black-box-agent.md")
)
```

### 测试过程透明化

**必须向用户展示：**
1. **Agent 输入**：完整的测试 prompt（含类描述）
2. **Agent 输出**：完整的测试结果（含用例详情）
3. **测试代码**：生成的测试文件内容
4. **运行结果**：pytest 输出

### 测试失败处理

| 阶段 | 失败原因 | 处理方式 |
|------|----------|----------|
| 白盒 | 内部实现错误 | 返回修改建议，修复后重跑白盒 |
| 黑盒 | 行为不符合预期 | 返回期望vs实际，修复后重跑黑盒 |

**依次执行：白盒必须 100% 通过后才进入黑盒。**

### 清理测试文件

每个类测试通过后，删除该类的测试文件：
- `tests/test_{class_name}_white.py`
- `tests/test_{class_name}_black.py`

保持项目目录干净，只保留实现代码。

## Skill 结束

当所有类的白盒+黑盒测试都通过时：
> "所有类测试完成，测试文件已清理。现在可以开始拼接阶段，将各模块组合成完整项目。"

**Skill 不包含拼接实现**，由用户自行决定拼接方式和时机。

## Quick Reference

| 操作 | 命令/动作 |
|------|-----------|
| 调度白盒测试 | `Agent(subagent_type="general-purpose", prompt=Read("white-box-agent.md"))` |
| 调度黑盒测试 | `Agent(subagent_type="general-purpose", prompt=Read("black-box-agent.md"))` |
| 白盒通过后 | 才能调度黑盒测试 |
| 每个计划阶段 | 必须用户确认后才能执行 |
| 所有类完成 | 删除测试文件，提示拼接阶段 |

## Common Mistakes

**跳过计划确认**
- 表现：直接执行测试不展示计划
- 解决：强制每步计划都要用户确认

**测试过程不透明**
- 表现：只说通过/失败，不展示详情
- 解决：必须展示完整输入输出和测试代码

**跳过白盒直接黑盒**
- 表现：黑盒通过但实现有隐患
- 解决：强制白盒 100% 通过才继续

**测试后不清理**
- 表现：测试文件残留项目中
- 解决：每个类完成后立即删除测试文件
