# 简介
该仓库用于整理个人觉得不错的skills和mcp以及网站还有工具

# mcp
```
{
  "args": [
    "-y",
    "@modelcontextprotocol/server-sequential-thinking"
  ],
  "command": "npx",
  "type": "stdio"
}
```
优化模型思考和推理



```
{
  "args": [
    "-y",
    "@upstash/context7-mcp"
  ],
  "command": "npx",
  "type": "stdio"
}
```
查阅最新的技术文档


```
{
  "args": [
    "minimax-coding-plan-mcp",
    "-y"
  ],
  "command": "uvx",
  "env": {
    "MINIMAX_API_HOST": "https://api.minimaxi.com",
    "MINIMAX_API_KEY": "sk-***"
  }
}
```
便宜比较好获得的网络搜索功能

```
https://github.com/DeusData/codebase-memory-mcp
https://github.com/ast-grep/ast-grep-mcp
```
帮我agent理解代码

```
https://github.com/GongRzhe/Office-Word-MCP-Server
claude for word
```
编写word文档

```
VSCode 扩展商店，搜索 Pencil（开发者 High Agency）
https://github.com/OpenCoworkAI/open-codesign
```
设计

```
https://github.com/iOfficeAI/OfficeAI
https://github.com/iOfficeAI/OfficeCLI
```
office编辑

# skills
```
https://github.com/obra/superpowers
```
帮助思考和测试

```
https://github.com/OthmanAdi/planning-with-files
```
写计划的

```
https://clawhub.ai/solomon4github/multi-search-engine-2-0-1
```
增强搜索功能

# 在线服务

```
https://filebin.net/
```
在线文件托管

# 工具
```
  katana \
  -list ../httpx/alive.txt   # 目标列表
  -d 8                       # 爬取深度 8 层
  -c 100                     # 100 个并发 fetcher
  -p 30                      # 同时处理 30 个目标
  -jc                        # 解析 JS 文件中的 endpoint
  -jsl                       # jsluice 深度解析 JS（耗内存但更全）
  -kf all                    # 爬取 robotstxt + sitemapxml
  -fx                        # 提取表单/输入框元素
  -hl                        # headless 模式
  -nos                       # Chrome --no-sandbox（Codespaces 环境必须加）
  -fs rdn                    # 范围限制在根域名内
  -timeout 15                # 请求超时 15 秒
  -retry 2                   # 失败重试 2 次
  -rd 1                      # 每个请求间隔 1 秒
  -j                         # JSONL 格式输出
  -o katana_full.json        # 输出文件
```
收集潜在的endpoint
