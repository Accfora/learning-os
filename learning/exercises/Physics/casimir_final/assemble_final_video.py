import os
import subprocess
import imageio_ffmpeg
from PIL import Image, ImageDraw, ImageFont
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
import shutil

FFMPEG_EXE = imageio_ffmpeg.get_ffmpeg_exe()
PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
FOOTAGE_DIR = os.path.join(PROJECT_DIR, "footage")
AUDIO_DIR = os.path.join(PROJECT_DIR, "audio")
os.makedirs(AUDIO_DIR, exist_ok=True)

FONTS_DIR = os.path.join(os.environ.get('WINDIR', 'C:\\Windows'), 'Fonts')

def get_font(name, size):
    path = os.path.join(FONTS_DIR, name)
    if os.path.exists(path):
        return ImageFont.truetype(path, size)
    return ImageFont.load_default()

FONT_TITLE = get_font('segoeuib.ttf', 44)
FONT_SUB = get_font('segoeui.ttf', 28)
FONT_BADGE = get_font('segoeuib.ttf', 20)
FONT_BODY = get_font('segoeui.ttf', 24)
FONT_BODY_B = get_font('segoeuib.ttf', 24)

# 1. Create transparent circular channel logo
def create_channel_logo():
    src_logo = os.path.join(os.path.dirname(PROJECT_DIR), "casimir_project", "channel_logo.jpg")
    out_logo = os.path.join(PROJECT_DIR, "channel_logo.png")
    size = 110
    if os.path.exists(src_logo):
        im = Image.open(src_logo).convert("RGBA").resize((size, size), Image.Resampling.LANCZOS)
        mask = Image.new("L", (size, size), 0)
        draw = ImageDraw.Draw(mask)
        draw.ellipse((0, 0, size, size), fill=255)
        
        circ = Image.new("RGBA", (size, size), (0, 0, 0, 0))
        circ.paste(im, (0, 0), mask)
        draw_c = ImageDraw.Draw(circ)
        draw_c.ellipse((1, 1, size-2, size-2), outline="#38BDF8", width=3)
        circ.save(out_logo)
        print("  [+] Channel logo ready: channel_logo.png")
    return out_logo

# 2. Copy and prepare voiceover files
def prepare_audio():
    src_audio_dir = os.path.join(os.path.dirname(PROJECT_DIR), "casimir_project")
    for i in range(1, 6):
        src = os.path.join(src_audio_dir, f"audio_{i}.mp3")
        dst = os.path.join(AUDIO_DIR, f"scene_{i}.mp3")
        if os.path.exists(src):
            shutil.copy2(src, dst)
    print("  [+] Narration audio tracks ready.")

# 3. Create high-resolution uncompressed 16:9 Casimir standing wave diagram
def render_casimir_diagram():
    out_png = os.path.join(PROJECT_DIR, "casimir_diagram_1080p.png")
    # True 16:9 ratio: 19.2 x 10.8 inches at 100 dpi = 1920x1080
    fig, ax = plt.subplots(figsize=(19.2, 10.8), facecolor='#060913', dpi=100)
    ax.set_facecolor('#060913')
    
    # Top title area
    ax.text(9.6, 10.1, "ЭФФЕКТ КАЗИМИРА: СТОЯЧИЕ ВОЛНЫ В ВАКУУМЕ", color='#F8FAFC', fontsize=26, fontweight='bold', ha='center')
    ax.text(9.6, 9.5, "Разница квантового давления виртуальных фотонов", color='#94A3B8', fontsize=18, ha='center')
    
    # Plates
    d_left = 7.5
    d_right = 11.7
    plate_w = 0.4
    
    rect1 = patches.Rectangle((d_left - plate_w, 2.0), plate_w, 6.0, facecolor='#64748B', edgecolor='#38BDF8', lw=3)
    rect2 = patches.Rectangle((d_right, 2.0), plate_w, 6.0, facecolor='#64748B', edgecolor='#38BDF8', lw=3)
    ax.add_patch(rect1)
    ax.add_patch(rect2)
    
    # Outside chaotic waves (left)
    x_l = np.linspace(1.0, d_left - plate_w, 400)
    y_l1 = 5.0 + 0.4 * np.sin(10 * x_l) + 0.25 * np.sin(22 * x_l)
    y_l2 = 5.0 - 0.4 * np.sin(10 * x_l) - 0.25 * np.sin(22 * x_l)
    ax.plot(x_l, y_l1, color='#F43F5E', lw=2.5, alpha=0.9)
    ax.plot(x_l, y_l2, color='#F43F5E', lw=1.5, ls='--', alpha=0.5)
    
    # Outside chaotic waves (right)
    x_r = np.linspace(d_right + plate_w, 18.2, 400)
    y_r1 = 5.0 + 0.4 * np.sin(12 * x_r) + 0.25 * np.sin(25 * x_r)
    y_r2 = 5.0 - 0.4 * np.sin(12 * x_r) - 0.25 * np.sin(25 * x_r)
    ax.plot(x_r, y_r1, color='#F43F5E', lw=2.5, alpha=0.9)
    ax.plot(x_r, y_r2, color='#F43F5E', lw=1.5, ls='--', alpha=0.5)
    
    # Inside standing waves
    x_in = np.linspace(d_left, d_right, 250)
    w_mode = 5.0 + 0.85 * np.sin(np.pi * (x_in - d_left) / (d_right - d_left))
    w_mode_neg = 5.0 - 0.85 * np.sin(np.pi * (x_in - d_left) / (d_right - d_left))
    ax.plot(x_in, w_mode, color='#38BDF8', lw=4, label='Резонансная стоячая волна')
    ax.plot(x_in, w_mode_neg, color='#38BDF8', lw=2.5, ls='--')
    
    # Force Arrows pushing inward
    ax.annotate('', xy=(d_left - plate_w, 5.0), xytext=(d_left - 2.2, 5.0),
                arrowprops=dict(facecolor='#F43F5E', edgecolor='#F43F5E', width=5, headwidth=14))
    ax.annotate('', xy=(d_right + plate_w, 5.0), xytext=(d_right + 2.2, 5.0),
                arrowprops=dict(facecolor='#F43F5E', edgecolor='#F43F5E', width=5, headwidth=14))
                
    ax.text(3.5, 6.8, "ВНЕШНЕЕ ДАВЛЕНИЕ ВАКУУМА\n(любые длины волн)", color='#FDA4AF', fontsize=14, fontweight='bold', ha='center')
    ax.text(15.7, 6.8, "ВНЕШНЕЕ ДАВЛЕНИЕ ВАКУУМА\n(любые длины волн)", color='#FDA4AF', fontsize=14, fontweight='bold', ha='center')
    ax.text(9.6, 2.7, "Зазор d (нанометры)\nТолько резонансные моды", color='#7DD3FC', fontsize=15, fontweight='bold', ha='center')
    
    # Formula box at bottom
    ax.text(9.6, 1.0, "Фундаментальная формула силы Казимира:   F / S = ( π² · ℏ · c ) / ( 240 · d⁴ )", 
            color='#E2E8F0', fontsize=17, fontweight='bold', ha='center',
            bbox=dict(boxstyle='round,pad=0.8', facecolor='#0F172A', edgecolor='#818CF8', lw=2))
            
    ax.set_xlim(0, 19.2)
    ax.set_ylim(0, 10.8)
    ax.axis('off')
    
    plt.tight_layout(pad=0)
    plt.savefig(out_png, dpi=100, facecolor=fig.get_facecolor())
    plt.close()
    print("  [+] High-res uncompressed 16:9 diagram ready: casimir_diagram_1080p.png")
    return out_png

def get_audio_duration(file_path):
    cmd = [FFMPEG_EXE, "-i", file_path]
    res = subprocess.run(cmd, stderr=subprocess.PIPE, stdout=subprocess.PIPE, text=True)
    import re
    m = re.search(r"Duration:\s*(\d+):(\d+):(\d+\.\d+)", res.stderr)
    if m:
        hours, mins, secs = m.groups()
        return float(hours)*3600 + float(mins)*60 + float(secs)
    return 30.0

# 4. Render scenes with real video footage
def build_clip(scene_id, input_video_or_img, audio_path, is_image, title, banner_text, out_mp4):
    dur = get_audio_duration(audio_path) + 0.5
    logo_png = os.path.join(PROJECT_DIR, "channel_logo.png").replace("\\", "/")
    
    # Clean overlay layout:
    # Top bar with title, bottom bar with highlight, top right channel logo
    safe_title = title.replace("'", "").replace(":", " -")
    safe_banner = banner_text.replace("'", "").replace(":", " -")
    
    font_bold = "C\\:/Windows/Fonts/segoeuib.ttf"
    font_reg = "C\\:/Windows/Fonts/segoeui.ttf"
    
    if is_image:
        filter_str = (
            f"[0:v]scale=1920:1080:force_original_aspect_ratio=decrease,pad=1920:1080:(ow-iw)/2:(oh-ih)/2:black,"
            f"drawbox=x=80:y=40:w=1760:h=60:color=black@0.75:t=fill,"
            f"drawtext=fontfile='{font_bold}':text='МТУСИ  |  КАФЕДРА ФИЗИКИ  |  {safe_title}':x=110:y=56:fontsize=24:fontcolor=0x38BDF8,"
            f"drawbox=x=80:y=970:w=1760:h=60:color=black@0.75:t=fill,"
            f"drawtext=fontfile='{font_reg}':text='{safe_banner}':x=110:y=986:fontsize=22:fontcolor=0xE2E8F0[v1];"
            f"[v1][1:v]overlay=W-220:120[outv]"
        )
        cmd = [
            FFMPEG_EXE, "-y",
            "-loop", "1",
            "-i", input_video_or_img,
            "-i", logo_png,
            "-i", audio_path,
            "-filter_complex", filter_str,
            "-map", "[outv]",
            "-map", "2:a",
            "-c:v", "libx264",
            "-t", str(dur),
            "-pix_fmt", "yuv420p",
            "-c:a", "aac",
            "-b:a", "192k",
            out_mp4
        ]
    else:
        # For real video footage: loop video, scale/crop to 1080p, overlay graphics
        filter_str = (
            f"[0:v]scale=1920:1080:force_original_aspect_ratio=increase,crop=1920:1080,"
            f"drawbox=x=80:y=40:w=1760:h=60:color=black@0.75:t=fill,"
            f"drawtext=fontfile='{font_bold}':text='МТУСИ  |  КАФЕДРА ФИЗИКИ  |  {safe_title}':x=110:y=56:fontsize=24:fontcolor=0x38BDF8,"
            f"drawbox=x=80:y=940:w=1760:h=90:color=black@0.85:t=fill,"
            f"drawtext=fontfile='{font_bold}':text='{safe_banner}':x=110:y=970:fontsize=24:fontcolor=0xF8FAFC[v1];"
            f"[v1][1:v]overlay=W-220:120[outv]"
        )
        cmd = [
            FFMPEG_EXE, "-y",
            "-stream_loop", "-1",
            "-i", input_video_or_img,
            "-i", logo_png,
            "-i", audio_path,
            "-filter_complex", filter_str,
            "-map", "[outv]",
            "-map", "2:a",
            "-c:v", "libx264",
            "-t", str(dur),
            "-pix_fmt", "yuv420p",
            "-c:a", "aac",
            "-b:a", "192k",
            out_mp4
        ]
    subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print(f"  [+] Scene {scene_id} generated ({dur:.1f}s)")
    return out_mp4

def main():
    print("=== ASSEMBLING POLISHED CASIMIR VIDEO WITH REAL FOOTAGE ===\n", flush=True)
    create_channel_logo()
    prepare_audio()
    diagram_path = render_casimir_diagram()
    
    scenes_config = [
        {
            "id": 1,
            "footage": os.path.join(FOOTAGE_DIR, "01_deep_space_laser.webm"),
            "audio": os.path.join(AUDIO_DIR, "scene_1.mp3"),
            "is_img": False,
            "title": "ЭФФЕКТ КАЗИМИРА - СИЛА ИЗ ВАКУУМА",
            "banner": "Может ли абсолютная пустота притягивать реальные предметы?"
        },
        {
            "id": 2,
            "footage": os.path.join(FOOTAGE_DIR, "02_vacuum_fluctuations.ogv"),
            "audio": os.path.join(AUDIO_DIR, "scene_2.mp3"),
            "is_img": False,
            "title": "КВАНТОВЫЕ ФЛУКТУАЦИИ ВАКУУМА",
            "banner": "Вакуум непрерывно кипит виртуальными фотонами всех частот"
        },
        {
            "id": 3,
            "footage": diagram_path,
            "audio": os.path.join(AUDIO_DIR, "scene_3.mp3"),
            "is_img": True,
            "title": "ГРАНИЧНЫЕ УСЛОВИЯ И СТОЯЧИЕ ВОЛНЫ",
            "banner": "Разница внешнего и внутреннего давления сжимает пластины"
        },
        {
            "id": 4,
            "footage": os.path.join(FOOTAGE_DIR, "03_casimir_water_experiment.ogv"),
            "audio": os.path.join(AUDIO_DIR, "scene_4.mp3"),
            "is_img": False,
            "title": "ФИЗИЧЕСКИЙ ЭКСПЕРИМЕНТ И НАНОЧИПЫ",
            "banner": "Экспериментальная демонстрация эффекта и проблема слипания деталей в микросхемах"
        },
        {
            "id": 5,
            "footage": os.path.join(FOOTAGE_DIR, "04_semiconductor_laser.ogv"),
            "audio": os.path.join(AUDIO_DIR, "scene_5.mp3"),
            "is_img": False,
            "title": "МТУСИ - КАФЕДРА ФИЗИКИ (2026)",
            "banner": "Доклад подготовил: Бородин Леонид Сергеевич (группа БВТ2602)"
        }
    ]
    
    rendered_clips = []
    for sc in scenes_config:
        out_clip = os.path.join(PROJECT_DIR, f"clip_{sc['id']}.mp4")
        build_clip(sc["id"], sc["footage"], sc["audio"], sc["is_img"], sc["title"], sc["banner"], out_clip)
        rendered_clips.append(out_clip)
        
    # Concat
    concat_txt = os.path.join(PROJECT_DIR, "concat_list.txt")
    with open(concat_txt, "w", encoding="utf-8") as f:
        for c in rendered_clips:
            f.write(f"file '{c.replace('\\', '/')}'\n")
            
    final_output = os.path.join(PROJECT_DIR, "Эффект_Казимира_МТУСИ_Бородин.mp4")
    cmd = [
        FFMPEG_EXE, "-y",
        "-f", "concat",
        "-safe", "0",
        "-i", concat_txt,
        "-c", "copy",
        final_output
    ]
    subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print(f"\n🎉 SUCCESS! FINISHED VIDEO: {final_output}", flush=True)

if __name__ == "__main__":
    main()
