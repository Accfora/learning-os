import subprocess
import re

news_items = []
for p in range(1, 12):
    url = f"https://mtuci.ru/about_the_university/news/?PAGEN_1={p}"
    cmd = ['curl.exe', '-s', '-L', '-H', 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64)', url]
    html = subprocess.run(cmd, capture_output=True).stdout.decode('utf-8', errors='ignore')
    # news links have text inside
    cards = re.findall(r'<a[^>]+href="(/about_the_university/news/\d+/)"[^>]*>([\s\S]*?)</a>', html)
    for href, text in cards:
        clean = re.sub(r'<[^>]+>', '', text).strip()
        if len(clean) > 15:
            news_items.append((href, clean))

print("Total news items extracted:", len(news_items))
keywords = ['кибер', 'лаборатор', 'ии', 'квант', 'ит', 'хакатон', 'робот', 'безопасн', 'касперск', 'яндекс', '5g', 'код']
matching = []
for href, title in news_items:
    if any(k in title.lower() for k in keywords):
        matching.append((href, title))

print(f"Matching news items: {len(matching)}")
for href, title in matching[:25]:
    print(href, "-->", title[:80])
