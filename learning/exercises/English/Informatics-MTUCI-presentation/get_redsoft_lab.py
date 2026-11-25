import subprocess
import re
import os
from PIL import Image

url = "https://mtuci.ru/about_the_university/news/14361/"
cmd = ['curl.exe', '-s', '-L', '-H', 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64)', url]
html = subprocess.run(cmd, capture_output=True).stdout.decode('utf-8', errors='ignore')

# Extract images
imgs = re.findall(r'(/upload/[^"\'\s>]+\.(?:webp|jpg|jpeg|png))', html, re.IGNORECASE)
print("Found images in 14361:", len(imgs))

assets = r"c:\Users\borod\OneDrive\Рабочий стол\МТУСИ\ОК&ВМ\learning-os-template\learning\exercises\English\Informatics-MTUCI-presentation\assets"

for im in set(imgs):
    if 'resize_cache' not in im:
        full_url = "https://mtuci.ru" + im
        out_name = os.path.basename(im)
        out_path = os.path.join(assets, out_name)
        subprocess.run(['curl.exe', '-s', '-L', '-H', 'User-Agent: Mozilla/5.0', full_url, '-o', out_path])
        print("Downloaded:", out_name, "size:", os.path.getsize(out_path))
