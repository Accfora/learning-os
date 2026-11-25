import subprocess
import re
import os
from PIL import Image

assets = r"c:\Users\borod\OneDrive\Рабочий стол\МТУСИ\ОК&ВМ\learning-os-template\learning\exercises\English\Informatics-MTUCI-presentation\assets"

news_ids = ["13385", "12309", "12882", "13104", "13426"]

for nid in news_ids:
    url = f"https://mtuci.ru/about_the_university/news/{nid}/"
    cmd = ['curl.exe', '-s', '-L', '-H', 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64)', url]
    html = subprocess.run(cmd, capture_output=True).stdout.decode('utf-8', errors='ignore')
    imgs = re.findall(r'(/upload/[^"\'\s>]+\.(?:webp|jpg|jpeg|png))', html, re.IGNORECASE)
    origs = [im for im in set(imgs) if 'resize_cache' not in im]
    print(f"News {nid} has {len(origs)} images")
    for idx, im in enumerate(origs[:2]):
        full_url = "https://mtuci.ru" + im
        out_name = f"lab_{nid}_{idx}.webp"
        out_path = os.path.join(assets, out_name)
        subprocess.run(['curl.exe', '-s', '-L', '-H', 'User-Agent: Mozilla/5.0', full_url, '-o', out_path])
        if os.path.exists(out_path):
            try:
                with Image.open(out_path) as im_pil:
                    jpg_out = os.path.join(assets, f"lab_{nid}_{idx}.jpg")
                    im_pil.convert('RGB').save(jpg_out, "JPEG")
                    print(f"  Saved {jpg_out}, size={im_pil.size}")
            except Exception as e:
                pass
