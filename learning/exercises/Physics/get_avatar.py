import requests
import re
import os

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
try:
    resp = requests.get('https://t.me/MoscowPhysics', headers=headers, timeout=10)
    match = re.search(r'property="og:image"\s+content="([^"]+)"', resp.text)
    if match:
        img_url = match.group(1)
        print("Found Avatar URL:", img_url)
        img_res = requests.get(img_url, headers=headers, timeout=10)
        os.makedirs('casimir_project', exist_ok=True)
        with open('casimir_project/channel_logo.jpg', 'wb') as f:
            f.write(img_res.content)
        print("Saved casimir_project/channel_logo.jpg successfully!")
    else:
        print("Could not find og:image in t.me/MoscowPhysics")
except Exception as e:
    print("Error:", e)
