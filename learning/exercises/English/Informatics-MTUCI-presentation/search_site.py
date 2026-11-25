import subprocess
import re

url = "https://mtuci.ru/search/?q=%D0%BA%D0%B8%D0%B1%D0%B5%D1%80%D0%BF%D0%BE%D0%BB%D0%B8%D0%B3%D0%BE%D0%BD"
cmd = ['curl.exe', '-s', '-L', '-H', 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64)', url]
html = subprocess.run(cmd, capture_output=True).stdout.decode('utf-8', errors='ignore')

links = re.findall(r'<a[^>]+href="(/about_the_university/news/\d+/)"[^>]*>([\s\S]*?)</a>', html)
print("Search results for киберполигон:", len(links))
for l, t in links[:10]:
    clean_title = re.sub(r'<[^>]+>', '', t).strip()
    print(l, "-->", clean_title)
