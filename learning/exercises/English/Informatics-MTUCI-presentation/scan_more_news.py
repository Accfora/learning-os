import subprocess
import re

news_items = []
for p in range(12, 35):
    url = f"https://mtuci.ru/about_the_university/news/?PAGEN_1={p}"
    cmd = ['curl.exe', '-s', '-L', '-H', 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64)', url]
    html = subprocess.run(cmd, capture_output=True).stdout.decode('utf-8', errors='ignore')
    cards = re.findall(r'<a[^>]+href="(/about_the_university/news/\d+/)"[^>]*>([\s\S]*?)</a>', html)
    for href, text in cards:
        clean = re.sub(r'<[^>]+>', '', text).strip()
        if len(clean) > 15:
            news_items.append((href, clean))

keywords = ['кибер', 'лаборатор', 'квант', 'vr', 'ar', 'полигон', 'хакатон', 'искусствен']
found = []
for href, title in news_items:
    if any(k in title.lower() for k in keywords):
        found.append((href, title))

print(f"Total matching in pages 12-35: {len(found)}")
for href, title in found[:25]:
    print(href, "-->", title)
