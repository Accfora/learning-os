import subprocess
import re
import urllib.parse

def search_mtuci(query):
    encoded = urllib.parse.quote(query)
    url = f"https://mtuci.ru/search/?q={encoded}&where="
    cmd = ['curl.exe', '-s', '-L', '-H', 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64)', url]
    html = subprocess.run(cmd, capture_output=True).stdout.decode('utf-8', errors='ignore')
    links = re.findall(r'href="(/about_the_university/news/\d+/)"', html)
    return list(dict.fromkeys(links))

queries = ["киберполигон", "квантовых", "хакатон", "Касперского", "лаборатория"]
found_articles = {}
for q in queries:
    res = search_mtuci(q)
    print(f"Query '{q}': {len(res)} articles")
    for link in res[:5]:
        found_articles[link] = q

print("Total unique news links:", len(found_articles))
for link, q in list(found_articles.items())[:15]:
    print(link, "<-", q)
