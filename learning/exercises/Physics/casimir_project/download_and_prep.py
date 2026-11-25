import os
import urllib.request
import subprocess
import imageio_ffmpeg
from gtts import gTTS

FFMPEG_EXE = imageio_ffmpeg.get_ffmpeg_exe()
OUT_DIR = os.path.dirname(os.path.abspath(__file__))
VIDEOS_DIR = os.path.join(OUT_DIR, "raw_videos")
os.makedirs(VIDEOS_DIR, exist_ok=True)

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

SOURCES = {
    "microchip": "https://upload.wikimedia.org/wikipedia/commons/a/a5/Zoom_Into_a_Microchip.webm",
    "casimir_diana": "https://upload.wikimedia.org/wikipedia/commons/4/4d/The_Casimir_Effect_-_Diana_Chao.webm",
    "water_casimir": "https://upload.wikimedia.org/wikipedia/commons/9/9d/Water_wave_analogue_of_Casimir_effect.ogv"
}

def download_file(url, out_path):
    print(f"Downloading {url} to {out_path}...", flush=True)
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req) as resp, open(out_path, 'wb') as f:
        f.write(resp.read())
    print(f"  [+] Saved {out_path} ({os.path.getsize(out_path)} bytes)", flush=True)

for name, url in SOURCES.items():
    ext = url.split('.')[-1].split('?')[0]
    dest = os.path.join(VIDEOS_DIR, f"{name}.{ext}")
    if not os.path.exists(dest) or os.path.getsize(dest) == 0:
        download_file(url, dest)
    else:
        print(f"Already exists: {dest}")
