import subprocess
import os
from PIL import Image

assets = r"c:\Users\borod\OneDrive\Рабочий стол\МТУСИ\ОК&ВМ\learning-os-template\learning\exercises\English\Informatics-MTUCI-presentation\assets"

gallery_files = [
    "1-min.jpg",
    "2-min.jpeg",
    "3-min.jpg",
    "4-min.jpeg",
    "5-min.jpg",
    "6-min.jpeg",
    "7-min.jpeg",
    "8-min.jpeg"
]

for gf in gallery_files:
    url = f"https://abitur.mtuci.ru/upload/images/abitur-front-gallery/{gf}"
    out = os.path.join(assets, f"full_{gf}")
    cmd = ["curl.exe", "-s", "-L", "-H", "User-Agent: Mozilla/5.0", url, "-o", out]
    subprocess.run(cmd)
    if os.path.exists(out):
        try:
            with Image.open(out) as im:
                print(f"SUCCESS {gf}: {im.size}, {os.path.getsize(out)} bytes")
        except Exception as e:
            print(f"FAILED {gf}: {e} (bytes: {os.path.getsize(out)})")
