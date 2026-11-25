import urllib.request
import json
import os
import subprocess

assets = r"c:\Users\borod\OneDrive\Рабочий стол\МТУСИ\ОК&ВМ\learning-os-template\learning\exercises\English\Informatics-MTUCI-presentation\assets"

def get_commons_img(query, out_name):
    search_url = f"https://commons.wikimedia.org/w/api.php?action=query&list=search&srsearch={urllib.parse.quote(query)}&srnamespace=6&format=json"
    req = urllib.request.Request(search_url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        with urllib.request.urlopen(req) as resp:
            data = json.loads(resp.read().decode())
            results = data.get('query', {}).get('search', [])
            for r in results:
                title = r['title']
                info_url = f"https://commons.wikimedia.org/w/api.php?action=query&titles={urllib.parse.quote(title)}&prop=imageinfo&iiprop=url&format=json"
                req2 = urllib.request.Request(info_url, headers={'User-Agent': 'Mozilla/5.0'})
                with urllib.request.urlopen(req2) as resp2:
                    d2 = json.loads(resp2.read().decode())
                    for pid, pdata in d2.get('query', {}).get('pages', {}).items():
                        url = pdata.get('imageinfo', [{}])[0].get('url', '')
                        if url.lower().endswith(('.jpg', '.jpeg', '.png')):
                            out_path = os.path.join(assets, out_name)
                            subprocess.run(['curl.exe', '-s', '-L', '-H', 'User-Agent: Mozilla/5.0', url, '-o', out_path])
                            print(f"Downloaded {out_name} from {url} ({os.path.getsize(out_path)} bytes)")
                            return True
    except Exception as e:
        print(f"Error {query}: {e}")
    return False

get_commons_img("Virtual reality headset student classroom", "vr_lab.jpg")
get_commons_img("Students computer laboratory programming classroom", "computer_class.jpg")
