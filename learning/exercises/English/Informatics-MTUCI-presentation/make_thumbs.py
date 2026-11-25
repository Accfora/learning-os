import os
from PIL import Image

assets = r"c:\Users\borod\OneDrive\Рабочий стол\МТУСИ\ОК&ВМ\learning-os-template\learning\exercises\English\Informatics-MTUCI-presentation\assets"

files = ["full_5-min.jpg", "full_6-min.jpeg", "full_7-min.jpeg", "full_8-min.jpeg"]

for f in files:
    p = os.path.join(assets, f)
    with Image.open(p) as im:
        im.thumbnail((800, 600))
        out = os.path.join(assets, "thumb_" + f.replace('.jpeg', '.jpg'))
        im.save(out, "JPEG")
        print("Saved thumbnail:", out)
