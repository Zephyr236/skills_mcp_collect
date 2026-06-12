import json
import sys
from urllib.parse import urlparse, urlunparse
from collections import defaultdict

def extract_domain(url):
    """提取完整域名（netloc）"""
    parsed = urlparse(url)
    return parsed.netloc


def normalize_url(url):
    """规范化URL，只保留 scheme + netloc + path 作为去重键"""
    parsed = urlparse(url.strip())
    base = urlunparse((parsed.scheme, parsed.netloc, parsed.path, '', '', ''))
    return base, parsed


def deduplicate_urls(url_list, output_file=None):
    """对URL列表进行去重（按路径）"""
    url_groups = defaultdict(list)
    
    for url in url_list:
        base, parsed = normalize_url(url)
        url_groups[base].append(url)
    
    # 保留每个路径的第一个URL
    deduped = [urls[0] for urls in url_groups.values()]
    deduped.sort()
    
    if output_file:
        with open(output_file, 'w', encoding='utf-8') as f:
            for url in deduped:
                f.write(url + '\n')
        print(f"去重完成！共发现 {len(url_groups)} 个唯一路径，已保存至 {output_file}")
    else:
        for url in deduped:
            print(url)
    
    return deduped


def main(input_txt, output_txt, domain):
    urls = []
    
    with open(input_txt, 'r', encoding='utf-8') as file:
        for line_num, line in enumerate(file, 1):
            line = line.strip()
            if not line:
                continue
            try:
                obj = json.loads(line)
                req = obj.get("request", {})
                
                endpoint = req.get("endpoint", "")
                method = req.get("method", "")
                
                if (method == "GET" and 
                    endpoint and
                    not any(ext in endpoint for ext in [".js", ".css", ".htm"]) and
                    "?locale=" not in endpoint and
                    "?Lang=" not in endpoint and
                    extract_domain(endpoint).endswith(domain) and
                    "?" in endpoint and "=" in endpoint):
                    
                    urls.append(endpoint)
                    
            except json.JSONDecodeError:
                print(f"第 {line_num} 行 JSON 解析失败: {line[:100]}...")
            except Exception as e:
                print(f"第 {line_num} 行处理异常: {e}")
    
    print(f"过滤得到 {len(urls)} 个潜在 SQLi 注入点 URL")
    deduplicate_urls(urls, output_txt)


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python extract_sql_points.py <input.jsonl> <output.txt> <domain>")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    domain = sys.argv[3]
    main(input_file, output_file,domain)
