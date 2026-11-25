import urllib.request
import json
import re

# Let's search Yandex or DuckDuckGo for image URLs
# DuckDuckGo HTML or JSON search
def search_ddg_images(query):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
    # get vqd token
    url = f"https://duckduckgo.com/?q={urllib.parse.quote(query)}&iax=images&ia=images"
    req = urllib.request.Request(url, headers=headers)
    try:
        html = urllib.request.urlopen(req, timeout=5).read().decode('utf-8')
        vqd_match = re.search(r'vqd=([\d-]+)', html)
        if not vqd_match:
            vqd_match = re.search(r'vqd="([^"]+)"', html)
        if vqd_match:
            vqd = vqd_match.group(1)
            api_url = f"https://duckduckgo.com/i.js?l=ru-ru&o=json&q={urllib.parse.quote(query)}&vqd={vqd}&f=,,,&p=1"
            req2 = urllib.request.Request(api_url, headers=headers)
            res = json.loads(urllib.request.urlopen(req2, timeout=5).read().decode('utf-8'))
            return [r['image'] for r in res.get('results', [])[:5]]
    except Exception as e:
        print("DDG search error:", e)
    return []

queries = [
    "МТУСИ киберполигон фото",
    "МТУСИ компьютерный класс фото",
    "МТУСИ лаборатория искусственного интеллекта",
    "МТУСИ лаборатория касперского фото",
    "система p-vision мониторинг видеопотока"
]

for q in queries:
    imgs = search_ddg_images(q)
    print(q, '->', len(imgs))
    for im in imgs[:3]:
        print('  ', im)
