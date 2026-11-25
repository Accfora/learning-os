from PIL import Image
import os

assets = r"c:\Users\borod\OneDrive\Рабочий стол\МТУСИ\ОК&ВМ\learning-os-template\learning\exercises\English\Informatics-MTUCI-presentation\assets"

for f in ["Главное_здание_МТУСИ.jpg", "MTUSI.jpg", "Главный_корпус_(Лефортово).jpg"]:
    p = os.path.join(assets, f)
    with Image.open(p) as im:
        im.thumbnail((800, 600))
        out = os.path.join(assets, "prev_" + f)
        im.save(out, "JPEG")
        print("Created preview:", out)
