from PIL import Image
import os

assets = r"c:\Users\borod\OneDrive\Рабочий стол\МТУСИ\ОК&ВМ\learning-os-template\learning\exercises\English\Informatics-MTUCI-presentation\assets"

for f in ["lab_13426_0.jpg", "lab_13426_1.jpg", "lab_12882_0.jpg"]:
    p = os.path.join(assets, f)
    with Image.open(p) as im:
        im.thumbnail((800, 600))
        out = os.path.join(assets, "prev_" + f)
        im.save(out, "JPEG")
        print("Created preview for", f)
