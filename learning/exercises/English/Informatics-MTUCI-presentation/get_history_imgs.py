import subprocess
import os
from PIL import Image

assets = r"c:\Users\borod\OneDrive\Рабочий стол\МТУСИ\ОК&ВМ\learning-os-template\learning\exercises\English\Informatics-MTUCI-presentation\assets"

files = ["history2.webp", "his1.webp", "his2.webp", "his25.webp", "his26.webp", "his27.webp"]

for f in files:
    url = f"https://mtuci.ru/upload/dev2fun.imagecompress/webp/local/templates/mtuci/assets/img/content/{f}"
    out = os.path.join(assets, f)
    cmd = ["curl.exe", "-s", "-L", "-H", "User-Agent: Mozilla/5.0", url, "-o", out]
    subprocess.run(cmd)
    if os.path.exists(out):
        try:
            with Image.open(out) as im:
                png_path = os.path.join(assets, f.replace('.webp', '.png'))
                im.save(png_path, "PNG")
                print(f, "OK, size:", im.size)
        except Exception as e:
            print(f, "Error:", e)
