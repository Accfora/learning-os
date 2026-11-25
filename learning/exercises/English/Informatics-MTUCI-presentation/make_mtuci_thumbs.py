from PIL import Image
import os

assets = r"c:\Users\borod\OneDrive\Рабочий стол\МТУСИ\ОК&ВМ\learning-os-template\learning\exercises\English\Informatics-MTUCI-presentation\assets"

files = [
    "mtuci_real_12473_1.jpg",
    "mtuci_real_12331_0.jpg",
    "mtuci_real_12331_1.jpg",
    "mtuci_real_12489_0.jpg"
]

for f in files:
    p = os.path.join(assets, f)
    with Image.open(p) as im:
        im.thumbnail((800, 600))
        out = os.path.join(assets, "prev_" + f)
        im.save(out, "JPEG")
        print("Created preview for", f)
