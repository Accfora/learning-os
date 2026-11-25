import subprocess
import re

cmd = ['curl.exe', '-s', '-L', '-H', 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64)', 'https://vk.com/wall-19273188?q=%D0%BA%D0%B8%D0%B1%D0%B5%D1%80%D0%BF%D0%BE%D0%BB%D0%B8%D0%B3%D0%BE%D0%BD']
html = subprocess.run(cmd, capture_output=True).stdout.decode('utf-8', errors='ignore')
imgs = re.findall(r'(https://sun\d+-\d+\.userapi\.com/[^\s"\'<>]+\.(?:jpg|jpeg|png))', html)
print('VK cyberpolygon imgs found:', len(imgs))
for im in list(set(imgs))[:10]:
    print(' ', im)
