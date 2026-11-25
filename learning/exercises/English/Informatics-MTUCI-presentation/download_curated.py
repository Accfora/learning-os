import subprocess
import os

assets = r"c:\Users\borod\OneDrive\Рабочий стол\МТУСИ\ОК&ВМ\learning-os-template\learning\exercises\English\Informatics-MTUCI-presentation\assets"

# High-res educational images from open repositories / Wikimedia direct
images = {
    # Real VR Headset lab in education
    "vr_lab.jpg": "https://images.unsplash.com/photo-1593508512255-86ab42a8e620?q=80&w=1200&auto=format&fit=crop",
    # Real Computer science coding classroom with PC monitors
    "computer_class.jpg": "https://images.unsplash.com/photo-1531482615713-2afd69097998?q=80&w=1200&auto=format&fit=crop",
    # Real IT Hackathon / student tech awards
    "it_hackathon.jpg": "https://images.unsplash.com/photo-1517245386807-bb43f82c33c4?q=80&w=1200&auto=format&fit=crop"
}

for name, url in images.items():
    out = os.path.join(assets, name)
    cmd = ["curl.exe", "-s", "-L", "-H", "User-Agent: Mozilla/5.0", url, "-o", out]
    subprocess.run(cmd)
    if os.path.exists(out):
        print(f"Downloaded {name}: {os.path.getsize(out)} bytes")
