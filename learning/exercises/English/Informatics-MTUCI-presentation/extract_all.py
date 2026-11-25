import zipfile, os

pptx_path = r'c:\Users\borod\OneDrive\Рабочий стол\МТУСИ\ОК&ВМ\learning-os-template\raw\lectures\IT Fundamentals\2026-09-10-intro-sem1.pptx'
out_dir = r'c:\Users\borod\OneDrive\Рабочий стол\МТУСИ\ОК&ВМ\learning-os-template\learning\exercises\English\Informatics-MTUCI-presentation\extracted_intro'
os.makedirs(out_dir, exist_ok=True)

with zipfile.ZipFile(pptx_path) as z:
    for name in z.namelist():
        if name.startswith('ppt/media/'):
            base = os.path.basename(name)
            with open(os.path.join(out_dir, base), 'wb') as f:
                f.write(z.read(name))
            print("Extracted", base)
