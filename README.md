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

katana -u http://127.0.0.1:80 \                                                                                                            
      -d 5 -c 20 -p 10 -jc -kf all -fx \                                                                                                       
      -retry 2 -timeout 10 -j -o output.json

# 标准无头模式 — JS渲染 + 表单填充 + XHR提取
katana -u <URL> -d 5 -c 10 -p 5 -hl -nos -jc -jsl -fx -xhr -aff -retry 2 -timeout 15 -j -o output.json

# 混合无头模式 — 非headless先爬，headless再补刀
katana -u <URL> -d 6 -c 10 -p 5 -hl -hh -nos -jc -jsl -fx -xhr -aff -retry 2 -timeout 15 -j -o output.json

# 基础高效型 — 均衡速度与覆盖
katana -u <URL> -d 5 -c 20 -p 10 -jc -kf all -fx -retry 2 -timeout 10 -j -o output.json

# 深度优先型 — 适合层级较深的网站
katana -u <URL> -d 10 -c 20 -p 10 -s depth-first -jc -kf all -fx -retry 3 -timeout 15 -j -o output.json

# 广度优先型 — 先铺开再深入，避免遗漏某个分支
katana -u <URL> -d 8 -c 30 -p 15 -s breadth-first -jc -kf all -fx -retry 2 -timeout 10 -j -o output.json
```
收集潜在的endpoint
