import urllib.request
import json
import os

# We can search Wikimedia Commons for VR headset laboratory / students in computer laboratory
# Wikimedia has thousands of high-res CC images of students in VR headsets and computer science labs!

queries = [
    ("vr_lab.jpg", "Virtual reality in education laboratory"),
    ("computer_class.jpg", "Computer science university students laboratory classroom"),
    ("cyber_security.jpg", "Cybersecurity server room data center")
]

assets = r"c:\Users\borod\OneDrive\Рабочий стол\МТУСИ\ОК&ВМ\learning-os-template\learning\exercises\English\Informatics-MTUCI-presentation\assets"

for fname, q in queries:
    url = f"https://commons.wikimedia.org/w/api.php?action=query&generator=search&gsrsearch={urllib.parse.quote(q)}&gsrlimit=5&prop=imageinfo&iiprop=url|size&format=json"
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        with urllib.request.urlopen(req) as resp:
            data = json.loads(resp.read().decode())
            pages = data.get('query', {}).get('pages', {})
            for pid, pinfo in pages.items():
                img_url = pinfo['imageinfo'][0]['url']
                if img_url.lower().endswith(('.jpg', '.jpeg', '.png')):
                    out = os.path.join(assets, fname)
                    print(f"Downloading {fname} from {img_url}")
                    import subprocess
                    subprocess.run(['curl.exe', '-s', '-L', '-H', 'User-Agent: Mozilla/5.0', img_url, '-o', out])
                    print(f"Saved {fname}: {os.path.getsize(out)} bytes")
                    break
    except Exception as e:
        print("Error searching", q, e)
