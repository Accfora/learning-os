import subprocess
import re

def search_bing_images(query):
    url = f"https://www.bing.com/images/search?q={subprocess.list2cmdline([query])[1:-1]}&form=HDRSC2&first=1"
    cmd = ['curl.exe', '-s', '-L', '-H', 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36', url]
    html = subprocess.run(cmd, capture_output=True).stdout.decode('utf-8', errors='ignore')
    # Bing stores image URLs in murl
    murls = re.findall(r'murl&quot;:&quot;(https?://[^&]+?\.(?:jpg|jpeg|png))&quot;', html)
    return murls

queries = [
    "МТУСИ киберполигон",
    "МТУСИ компьютерный класс",
    "МТУСИ квантовый центр",
    "МТУСИ лаборатория искусственного интеллекта",
    "МТУСИ лаборатория касперского"
]

for q in queries:
    res = search_bing_images(q)
    print(q, "found:", len(res))
    for r in res[:4]:
        print("  ", r)
