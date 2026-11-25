import urllib.request
import json
import os

titles = [
    "File:Главное здание МТУСИ.jpg",
    "File:MTUSI.jpg",
    "File:Главный корпус (Лефортово).jpg"
]

assets = r"c:\Users\borod\OneDrive\Рабочий стол\МТУСИ\ОК&ВМ\learning-os-template\learning\exercises\English\Informatics-MTUCI-presentation\assets"

for t in titles:
    api_url = f"https://commons.wikimedia.org/w/api.php?action=query&titles={urllib.parse.quote(t)}&prop=imageinfo&iiprop=url&format=json"
    req = urllib.request.Request(api_url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        with urllib.request.urlopen(req) as resp:
            data = json.loads(resp.read().decode())
            pages = data.get('query', {}).get('pages', {})
            for pid, pdata in pages.items():
                img_url = pdata['imageinfo'][0]['url']
                fname = t.replace('File:', '').replace(' ', '_')
                out_path = os.path.join(assets, fname)
                print(f"Downloading {fname} from {img_url}")
                # Download with curl
                import subprocess
                subprocess.run(['curl.exe', '-s', '-L', '-H', 'User-Agent: Mozilla/5.0', img_url, '-o', out_path])
                print(f"Saved {out_path}, size: {os.path.getsize(out_path)}")
    except Exception as e:
        print("Error:", e)
