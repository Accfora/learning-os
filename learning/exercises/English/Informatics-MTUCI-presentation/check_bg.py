import subprocess
import os
from PIL import Image

assets = r"c:\Users\borod\OneDrive\Рабочий стол\МТУСИ\ОК&ВМ\learning-os-template\learning\exercises\English\Informatics-MTUCI-presentation\assets"
url = "https://mtuci.ru/upload/dev2fun.imagecompress/webp/local/templates/mtuci/assets/img/content/university_bg.webp"
out_webp = os.path.join(assets, "university_bg.webp")
out_png = os.path.join(assets, "real_campus.png")

subprocess.run(["curl.exe", "-s", "-L", "-H", "User-Agent: Mozilla/5.0", url, "-o", out_webp])
if os.path.exists(out_webp):
    with Image.open(out_webp) as im:
        im.save(out_png, "PNG")
        print("university_bg saved! size:", im.size)
