from PIL import Image
import os

assets = r"c:\Users\borod\OneDrive\Рабочий стол\МТУСИ\ОК&ВМ\learning-os-template\learning\exercises\English\Informatics-MTUCI-presentation\assets"

for f in ["lab_12309_0.jpg", "lab_12309_1.jpg"]:
    p = os.path.join(assets, f)
    with Image.open(p) as im:
        im.thumbnail((800, 600))
        out = os.path.join(assets, "prev_" + f)
        im.save(out, "JPEG")
        print("Created preview for", f)
