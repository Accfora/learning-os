import subprocess
import re

cmd = ['curl.exe', '-s', '-L', '-H', 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64)', 'https://mtuci.ru/about_the_university/news/14357/']
html = subprocess.run(cmd, capture_output=True).stdout.decode('utf-8', errors='ignore')

# Match all images
imgs = re.findall(r'(\S+?\.(?:webp|jpg|jpeg|png))', html, re.IGNORECASE)
for im in set(imgs):
    if '/upload/' in im:
        print(im)
