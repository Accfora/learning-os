import subprocess
import re

news_ids = ['14392', '14378', '14375', '14373', '14372', '14361', '14360', '14357', '14350', '14349', '14348', '14338', '14337']

for nid in news_ids:
    url = f"https://mtuci.ru/about_the_university/news/{nid}/"
    cmd = ['curl.exe', '-s', '-L', '-H', 'User-Agent: Mozilla/5.0', url]
    html = subprocess.run(cmd, capture_output=True).stdout.decode('utf-8', errors='ignore')
    title = re.findall(r'<h1[^>]*>(.*?)</h1>', html)
    t_text = title[0].strip() if title else 'No Title'
    imgs = re.findall(r'/upload/[^"\'\s>]+\.(?:jpg|jpeg|png)', html, re.IGNORECASE)
    orig = [i for i in set(imgs) if 'resize_cache' not in i]
    print(f"ID {nid}: {t_text}")
    print(f"   Images: {len(orig)}")
    for im in orig[:2]:
        print(f"   https://mtuci.ru{im}")
