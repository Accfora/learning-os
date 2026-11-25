import subprocess
import re

url = "https://abitur.mtuci.ru/"
cmd = ["curl.exe", "-s", "-L", "-H", "User-Agent: Mozilla/5.0", url]
html = subprocess.run(cmd, capture_output=True).stdout.decode('utf-8', errors='ignore')

# Find gallery section
gall_match = re.findall(r'<div[^>]*class="[^"]*gallery[^"]*"[^>]*>[\s\S]*?</div>\s*</div>', html, re.IGNORECASE)
if gall_match:
    print(gall_match[0][:2000])
else:
    # search for 1-min
    idx = html.find('1-min')
    print(html[idx-300:idx+800])
