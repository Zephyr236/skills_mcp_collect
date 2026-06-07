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
  katana -list targets.txt \
    -d 8 \                          # 深度 8 层
    -c 100 \                        # 100 并发
    -p 30 \                         # 每个目标最大并行数
    -jc \                           # 爬取 JS 文件中的 URL
    -jsl \                          # 解析 JS endpoint
    -sc \                           # 爬取 sitemap.xml
    -robotstxt \                    # 解析 robots.txt
    -fx \                           # 提取所有表单
    -kf all \                       # 所有已知字段
    -hl \                           # 无头浏览器（发现动态渲染内容）
    -nos \                          # 不截图，提速
    -fhr \                          # 跟随重定向
    -smd \                          # 爬取同一主域下的所有子域
    -timeout 15 \                   # 超时 15 秒
    -retry 2 \                      # 重试 2 次
    -delay 100ms \                  # 请求间隔，避免触发 WAF
    -json \                         # JSON 输出（保留完整元数据）
    -o katana_full.json
```
收集潜在的endpoint
