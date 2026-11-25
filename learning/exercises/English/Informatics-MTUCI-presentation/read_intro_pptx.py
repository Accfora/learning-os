import zipfile, os
from pptx import Presentation

pptx_path = r'c:\Users\borod\OneDrive\Рабочий стол\МТУСИ\ОК&ВМ\learning-os-template\raw\lectures\IT Fundamentals\2026-09-10-intro-sem1.pptx'
prs = Presentation(pptx_path)

print(f"Total slides: {len(prs.slides)}")
for i, slide in enumerate(prs.slides):
    text = " ".join([shape.text for shape in slide.shapes if shape.has_text_frame])
    print(f"Slide {i+1}: {text[:120].strip()}")
