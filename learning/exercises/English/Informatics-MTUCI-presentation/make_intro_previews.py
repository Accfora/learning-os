import os
from PIL import Image

src_dir = r'c:\Users\borod\OneDrive\Рабочий стол\МТУСИ\ОК&ВМ\learning-os-template\learning\exercises\English\Informatics-MTUCI-presentation\extracted_intro'
prev_dir = r'c:\Users\borod\OneDrive\Рабочий стол\МТУСИ\ОК&ВМ\learning-os-template\learning\exercises\English\Informatics-MTUCI-presentation\intro_previews'
os.makedirs(prev_dir, exist_ok=True)

for i in range(1, 25):
    fname = f"image{i if i > 1 else ''}.png"
    p = os.path.join(src_dir, fname)
    if os.path.exists(p):
        with Image.open(p) as im:
            im.thumbnail((600, 338))
            out = os.path.join(prev_dir, f"slide_{i}.jpg")
            im.convert('RGB').save(out, "JPEG")
print("Previews created!")
