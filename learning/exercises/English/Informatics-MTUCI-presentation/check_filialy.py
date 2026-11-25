import subprocess
import re

url = "https://mtuci.ru/about_the_university/filialy/"
cmd = ['curl.exe', '-s', '-L', '-H', 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64)', url]
html = subprocess.run(cmd, capture_output=True).stdout.decode('utf-8', errors='ignore')

imgs = re.findall(r'(/upload/[^"\'\s>]+\.(?:webp|jpg|jpeg|png))', html, re.IGNORECASE)
for im in set(imgs):
    print("https://mtuci.ru" + im)
