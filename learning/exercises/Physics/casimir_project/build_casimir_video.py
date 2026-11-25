import os
import subprocess
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from PIL import Image, ImageDraw, ImageFont
import imageio_ffmpeg

FFMPEG_EXE = imageio_ffmpeg.get_ffmpeg_exe()
OUT_DIR = os.path.dirname(os.path.abspath(__file__))
FONTS_DIR = os.path.join(os.environ.get('WINDIR', 'C:\\Windows'), 'Fonts')

def get_font(name, size):
    path = os.path.join(FONTS_DIR, name)
    if os.path.exists(path):
        return ImageFont.truetype(path, size)
    return ImageFont.load_default()

FONT_TITLE = get_font('segoeuib.ttf', 48)
FONT_SUBTITLE = get_font('segoeui.ttf', 30)
FONT_BADGE = get_font('segoeuib.ttf', 22)
FONT_BODY = get_font('segoeui.ttf', 26)
FONT_BODY_BOLD = get_font('segoeuib.ttf', 26)
FONT_FOOTER = get_font('segoeui.ttf', 20)

LOGO_PATH = os.path.join(OUT_DIR, "channel_logo.jpg")

SCENES = [
    {
        "id": 1,
        "title": "ЭФФЕКТ КАЗИМИРА",
        "subtitle": "Рождение силы притяжения из абсолютной пустоты",
        "badge": "КВАНТОВАЯ ФИЗИКА • ВАКУУМ • 1948 ГОД",
        "visual_type": "space_intro"
    },
    {
        "id": 2,
        "title": "ФИЗИЧЕСКИЙ МЕХАНИЗМ",
        "subtitle": "Квантовые флуктуации электромагнитного поля",
        "badge": "ПРИНЦИП ГЕЙЗЕНБЕРГА • ВИРТУАЛЬНЫЕ ЧАСТИЦЫ",
        "visual_type": "quantum_field"
    },
    {
        "id": 3,
        "title": "СТОЯЧИЕ ВОЛНЫ И ДАВЛЕНИЕ",
        "subtitle": "Почему пластины сжимаются с чудовищной силой",
        "badge": "ГРАНИЧНЫЕ УСЛОВИЯ • РАЗНИЦА ДАВЛЕНИЙ",
        "visual_type": "casimir_formula"
    },
    {
        "id": 4,
        "title": "НАНОТЕХНОЛОГИИ И МИКРОЧИПЫ",
        "subtitle": "Проблема квантового слипания (Stiction) в наносистемах",
        "badge": "МТУСИ • IT & НАНОЭЛЕКТРОНИКА • КРЕМНИЕВЫЕ ЧИПЫ",
        "visual_type": "nanotech_diagram"
    },
    {
        "id": 5,
        "title": "СПАСИБО ЗА ВНИМАНИЕ!",
        "subtitle": "Квантовая физика на защите технологий будущего",
        "badge": "МТУСИ • КАФЕДРА ФИЗИКИ • 2026",
        "visual_type": "conclusion"
    }
]

def make_circular_logo(logo_path, size=110):
    if not os.path.exists(logo_path):
        return None
    im = Image.open(logo_path).convert("RGBA").resize((size, size), Image.Resampling.LANCZOS)
    mask = Image.new("L", (size, size), 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0, size, size), fill=255)
    
    out = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    out.paste(im, (0, 0), mask)
    
    draw_out = ImageDraw.Draw(out)
    draw_out.ellipse((1, 1, size-2, size-2), outline="#38BDF8", width=3)
    return out

def get_audio_duration(file_path):
    cmd = [FFMPEG_EXE, "-i", file_path]
    res = subprocess.run(cmd, stderr=subprocess.PIPE, stdout=subprocess.PIPE, text=True)
    import re
    m = re.search(r"Duration:\s*(\d+):(\d+):(\d+\.\d+)", res.stderr)
    if m:
        hours, mins, secs = m.groups()
        return float(hours)*3600 + float(mins)*60 + float(secs)
    return 20.0

def render_nanotech_diagram():
    fig, ax = plt.subplots(figsize=(12, 5.0), facecolor='#060913')
    ax.set_facecolor('#060913')
    
    # Substrate
    rect_sub = patches.Rectangle((1.0, 0.5), 10.0, 0.8, facecolor='#1E293B', edgecolor='#475569', lw=2)
    ax.add_patch(rect_sub)
    ax.text(6.0, 0.9, "Кремниевая подложка чипа (Silicon Substrate)", color='#94A3B8', fontsize=12, fontweight='bold', ha='center')
    
    # Anchor
    rect_anchor = patches.Rectangle((1.5, 1.3), 1.2, 2.2, facecolor='#334155', edgecolor='#64748B', lw=2)
    ax.add_patch(rect_anchor)
    
    # Bent MEMS cantilever (showing stiction due to Casimir attraction)
    x_c = np.linspace(2.7, 9.5, 150)
    # Curves downward toward the substrate due to Casimir attraction
    y_c = 3.5 - 2.0 * ((x_c - 2.7) / (9.5 - 2.7))**2
    ax.plot(x_c, y_c, color='#38BDF8', lw=5, label='Кремниевая нанобалка MEMS-датчика')
    
    # Contact point (Stiction)
    ax.scatter([9.5], [1.5], color='#F43F5E', s=160, zorder=6, label='Точка слипания (Stiction failure)')
    
    # Casimir force arrows
    for xa in [5.5, 7.0, 8.5]:
        ya = 3.5 - 2.0 * ((xa - 2.7) / (9.5 - 2.7))**2
        ax.annotate('', xy=(xa, 1.3), xytext=(xa, ya),
                    arrowprops=dict(facecolor='#F43F5E', edgecolor='#F43F5E', width=3, headwidth=10))
        ax.text(xa + 0.2, (ya + 1.3)/2, "F_casimir", color='#FDA4AF', fontsize=10, fontweight='bold')
        
    ax.text(6.0, 4.2, "ПРОБЛЕМА НАНОМЕХАНИКИ: Самопроизвольное схлопывание нанозазоров (d < 50 нм)", 
            color='#F8FAFC', fontsize=13, fontweight='bold', ha='center')
    ax.text(9.5, 2.2, "Крах датчика!\n(слипание контактов)", color='#F43F5E', fontsize=11, fontweight='bold', ha='center')
    
    ax.set_xlim(0.5, 11.5)
    ax.set_ylim(0.2, 4.8)
    ax.axis('off')
    ax.legend(loc='upper left', facecolor='#0F172A', edgecolor='#334155', labelcolor='#F8FAFC', fontsize=10)
    
    plt.tight_layout()
    chart_path = os.path.join(OUT_DIR, "nanotech_diagram.png")
    plt.savefig(chart_path, dpi=160, bbox_inches='tight', facecolor=fig.get_facecolor())
    plt.close()
    return chart_path

def render_slide_frame(scene, diagram_img_path=None, nano_img_path=None):
    width, height = 1920, 1080
    img = Image.new('RGB', (width, height), color='#050814')
    draw = ImageDraw.Draw(img)
    
    # Gradient
    for y in range(height):
        ratio = y / height
        r = int(5 + ratio * 8)
        g = int(8 + ratio * 14)
        b = int(20 + ratio * 28)
        draw.line([(0, y), (width, y)], fill=(r, g, b))
        
    # Grid lines
    for x in range(0, width, 120):
        draw.line([(x, 0), (x, height)], fill=(255, 255, 255, 6), width=1)
    for y in range(0, height, 120):
        draw.line([(0, y), (width, y)], fill=(255, 255, 255, 6), width=1)
        
    # Top Brand Bar
    draw.rectangle([(80, 45), (width - 80, 95)], fill="#0D1527", outline="#1E293B", width=2)
    draw.text((110, 56), "МТУСИ  |  КАФЕДРА ФИЗИКИ  |  ВИДЕОДОКЛАД", fill="#38BDF8", font=FONT_BADGE)
    draw.text((width - 450, 56), "Канал @MoscowPhysics", fill="#C084FC", font=FONT_BADGE)
    
    # Official channel logo
    circ_logo = make_circular_logo(LOGO_PATH, size=100)
    if circ_logo:
        img.paste(circ_logo, (width - 200, 125), circ_logo)
        
    # Badge
    badge_text = scene.get("badge", "ФИЗИКА")
    draw.rounded_rectangle([(80, 125), (780, 175)], radius=10, fill="#0F172A", outline="#38BDF8", width=2)
    draw.text((105, 137), badge_text, fill="#38BDF8", font=FONT_BADGE)
    
    # Title & Subtitle
    draw.text((80, 205), scene["title"], fill="#F8FAFC", font=FONT_TITLE)
    draw.text((80, 275), scene["subtitle"], fill="#94A3B8", font=FONT_SUBTITLE)
    draw.line([(80, 330), (width - 220, 330)], fill="#334155", width=2)
    
    # Content
    if scene["visual_type"] == "space_intro":
        draw.rounded_rectangle([(80, 370), (width - 80, 500)], radius=16, fill="#0F172A", outline="#1E293B", width=2)
        draw.text((110, 395), "КЛЮЧЕВОЙ ВОПРОС:", fill="#F43F5E", font=FONT_BODY_BOLD)
        draw.text((110, 440), "Может ли абсолютная пустота и вакуум толкать реальные физические объекты?", fill="#E2E8F0", font=FONT_BODY)
        
        draw.rounded_rectangle([(80, 530), (width - 80, 790)], radius=16, fill="#0F172A", outline="#1E293B", width=2)
        draw.text((110, 555), "ПРЕДСКАЗАНИЕ ХЕНДРИКА КАЗИМИРА (1948 г.):", fill="#38BDF8", font=FONT_BODY_BOLD)
        points = [
            "• Две незаряженные металлические пластины в глубоком вакууме притягиваются друг к другу.",
            "• Сила притяжения возникает БЕЗ гравитации, электрических зарядов и магнитных полей.",
            "• Источник силы — квантовые нулевые колебания вакуума (виртуальные частицы)."
        ]
        yp = 605
        for pt in points:
            draw.text((110, yp), pt, fill="#CBD5E1", font=FONT_BODY)
            yp += 52
            
    elif scene["visual_type"] == "quantum_field":
        if diagram_img_path and os.path.exists(diagram_img_path):
            diag = Image.open(diagram_img_path).resize((1760, 480), Image.Resampling.LANCZOS)
            img.paste(diag, (80, 360))
            
        draw.rounded_rectangle([(80, 860), (width - 80, 930)], radius=12, fill="#0F172A", outline="#38BDF8", width=2)
        draw.text((110, 878), "ФИЗИЧЕСКИЙ ПРИНЦИП:  Снаружи пластин моды волн бесконечны  >  Внутри зазора лишь стоячие моды", fill="#E2E8F0", font=FONT_BODY_BOLD)

    elif scene["visual_type"] == "casimir_formula":
        draw.rounded_rectangle([(80, 370), (width - 80, 560)], radius=18, fill="#0F172A", outline="#818CF8", width=3)
        draw.text((110, 400), "ФУНДАМЕНТАЛЬНАЯ ФОРМУЛА КАЗИМИРА:", fill="#818CF8", font=FONT_BODY_BOLD)
        formula = "F / S = ( π² · ℏ · c ) / ( 240 · d⁴ )"
        draw.text((110, 460), formula, fill="#F8FAFC", font=get_font('segoeuib.ttf', 44))
        
        draw.rounded_rectangle([(80, 590), (width - 80, 860)], radius=16, fill="#0F172A", outline="#1E293B", width=2)
        draw.text((110, 615), "АНАЛИЗ ФОРМУЛЫ И ЗАВИСИМОСТЕЙ:", fill="#38BDF8", font=FONT_BODY_BOLD)
        f_points = [
            "• ℏ (постоянная Планка) и c (скорость света) подтверждают квантово-релятивистскую природу силы.",
            "• Обратная зависимость от d⁴ (четвёртой степени расстояния): при уменьшении зазора сила растёт лавинообразно!",
            "• При зазоре 10 нанометров давление достигает более 1 атмосферы (100 кПа)!"
        ]
        yp = 665
        for fp in f_points:
            draw.text((110, yp), fp, fill="#CBD5E1", font=FONT_BODY)
            yp += 55

    elif scene["visual_type"] == "nanotech_diagram":
        if nano_img_path and os.path.exists(nano_img_path):
            n_diag = Image.open(nano_img_path).resize((1760, 460), Image.Resampling.LANCZOS)
            img.paste(n_diag, (80, 360))
            
        draw.rounded_rectangle([(80, 840), (width - 80, 925)], radius=14, fill="#1E1B4B", outline="#F43F5E", width=2)
        draw.text((110, 865), "ВЫВОД ДЛЯ IT И МТУСИ:  Инженерам микроэлектроники необходимо предотвращать слипание квантовыми покрытиями.", fill="#FDA4AF", font=FONT_BODY_BOLD)

    elif scene["visual_type"] == "conclusion":
        draw.rounded_rectangle([(80, 370), (width - 80, 680)], radius=18, fill="#0F172A", outline="#1E293B", width=2)
        draw.text((110, 410), "ИТОГИ И ВЫВОДЫ ДОКЛАДА:", fill="#38BDF8", font=FONT_BODY_BOLD)
        c_points = [
            "1. Вакуум в квантовой механике — не пустота, а кипящий океан виртуальных фотонов.",
            "2. Сила Казимира доказана экспериментально и используется для прецизионных наносенсоров.",
            "3. Понимание эффекта критически важно для проектирования нанопроцессоров и чипов будущего в МТУСИ."
        ]
        yp = 475
        for cp in c_points:
            draw.text((110, yp), cp, fill="#E2E8F0", font=FONT_BODY)
            yp += 65
            
        draw.rounded_rectangle([(80, 715), (width - 80, 860)], radius=16, fill="#1E1B4B", outline="#6366F1", width=2)
        draw.text((110, 735), "ДОКЛАД ПОДГОТОВИЛ СТУДЕНТ МТУСИ:", fill="#A5B4FC", font=FONT_BODY_BOLD)
        draw.text((110, 785), "Бородин Леонид Сергеевич   |   Группа: БВТ2602   |   Канал: @MoscowPhysics (2026)", fill="#FFFFFF", font=get_font('segoeuib.ttf', 38))

    # Footer
    draw.line([(80, 960), (width - 80, 960)], fill="#1E293B", width=1)
    footer_text = f"Студент: Бородин Л. С. (БВТ2602)   •   Кафедра физики МТУСИ   •   2026   •   Слайд {scene['id']} из {len(SCENES)}"
    draw.text((80, 990), footer_text, fill="#64748B", font=FONT_FOOTER)
    
    out_slide = os.path.join(OUT_DIR, f"slide_{scene['id']}.png")
    img.save(out_slide, "PNG")
    print(f"  [+] Slide {scene['id']} generated: {out_slide}", flush=True)
    return out_slide

def assemble_scene_video(scene, duration, diagram_img, nano_img):
    aud_path = os.path.join(OUT_DIR, f"audio_{scene['id']}.mp3")
    out_video = os.path.join(OUT_DIR, f"scene_{scene['id']}.mp4")
    total_sec = duration + 0.5
    
    slide_img = render_slide_frame(scene, diagram_img, nano_img)
    cmd = [
        FFMPEG_EXE, "-y",
        "-loop", "1",
        "-i", slide_img,
        "-i", aud_path,
        "-c:v", "libx264",
        "-t", str(total_sec),
        "-pix_fmt", "yuv420p",
        "-vf", "scale=1920:1080",
        "-c:a", "aac",
        "-b:a", "192k",
        "-shortest",
        out_video
    ]
    subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print(f"  [+] Scene {scene['id']} video segment created ({total_sec:.1f}s)", flush=True)
    return out_video

def concatenate_all(videos):
    concat_txt = os.path.join(OUT_DIR, "concat_casimir.txt")
    with open(concat_txt, "w", encoding="utf-8") as f:
        for v in videos:
            f.write(f"file '{v.replace('\\', '/')}'\n")
            
    final_mp4 = os.path.join(OUT_DIR, "Эффект_Казимира_Бородин_БВТ2602.mp4")
    cmd = [
        FFMPEG_EXE, "-y",
        "-f", "concat",
        "-safe", "0",
        "-i", concat_txt,
        "-c", "copy",
        final_mp4
    ]
    subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print(f"\n🎉 FINAL VIDEO SUCCESSFULLY CREATED: {final_mp4}", flush=True)
    return final_mp4

def main():
    print("=== STARTING CASIMIR HIGH-QUALITY VIDEO BUILD PIPELINE ===\n", flush=True)
    diagram_path = os.path.join(OUT_DIR, "casimir_diagram.png")
    
    print("Rendering nanotech stiction diagram...", flush=True)
    nano_path = render_nanotech_diagram()
    
    print("\nRendering video scenes...", flush=True)
    video_segments = []
    total_time = 0.0
    for sc in SCENES:
        aud = os.path.join(OUT_DIR, f"audio_{sc['id']}.mp3")
        dur = get_audio_duration(aud)
        total_time += dur
        v = assemble_scene_video(sc, dur, diagram_path, nano_path)
        video_segments.append(v)
        
    print(f"\nTotal video duration: {total_time:.1f} seconds (~{total_time/60:.1f} min)", flush=True)
    concatenate_all(video_segments)
    print("\n=== PIPELINE FINISHED ===", flush=True)

if __name__ == "__main__":
    main()
