import urllib.request
import json

url = "https://commons.wikimedia.org/w/api.php?action=query&list=categorymembers&cmtitle=Category:Moscow_Technical_University_of_Communications_and_Informatics&cmtype=file&cmlimit=50&format=json"
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
try:
    with urllib.request.urlopen(req) as resp:
        data = json.loads(resp.read().decode())
        files = data.get('query', {}).get('categorymembers', [])
        print("Files in category:", len(files))
        for f in files:
            print("  ", f['title'])
except Exception as e:
    print(e)
