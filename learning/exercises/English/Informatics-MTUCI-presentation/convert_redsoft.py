from PIL import Image
import os

assets = r"c:\Users\borod\OneDrive\Рабочий стол\МТУСИ\ОК&ВМ\learning-os-template\learning\exercises\English\Informatics-MTUCI-presentation\assets"

files = [
    "wMkmWcZ9i54_Tu9l-b30YQJEj5yru8d2jghR7lJHwtGLzjKakSsv4itw6dfHb8RXdrGJznUfH3XMJ_zHi2EkFDbYmoCxAQ.webp",
    "ilNwOg6IldutD1vZuCp-soS078cF4zuYrBJvTDLxZ4jhDMDSQNSM_zGMcdU1oTXYdRgFb1sLWVERVIGyWUQTK6Hk.webp",
    "cNqyCkUMayGLQe4J9JjLTkIz5nS-c_ImBCa26SO6TODRguuf0uvyktH_yy1Rl9AG8nk0m-Dz0eUgVNNTunkw3s-z.webp",
    "DjpK3k_HICde71xWZlgEV5KCQUb8VFWwuTokZc6qPab8iRUawo8X5BMoTDfxMj5y5mkcFqcYAJB6uZO_Uo4Z_hLxMt61JQ.webp",
    "RXRLXGD2QcEh0fStW4PWuKzRvATKzYYPq27_9nItUChcgR-gd1-m3Z0-780nOuTjHXFuXMUK27GfQdqB5P0tGurX.webp"
]

for idx, f in enumerate(files):
    p = os.path.join(assets, f)
    if os.path.exists(p):
        with Image.open(p) as im:
            out = os.path.join(assets, f"redsoft_{idx+1}.jpg")
            im.convert('RGB').save(out, "JPEG")
            print(f"Saved redsoft_{idx+1}.jpg, size={im.size}")
