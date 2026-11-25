import os
import subprocess
import json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from PIL import Image, ImageDraw, ImageFont
from gtts import gTTS
import imageio_ffmpeg
from scipy.integrate import solve_ivp

FFMPEG_EXE = imageio_ffmpeg.get_ffmpeg_exe()
OUT_DIR = os.path.dirname(os.path.abspath(__file__))
FONTS_DIR = os.path.join(os.environ.get('WINDIR', 'C:\\Windows'), 'Fonts')

def get_font(name, size):
    path = os.path.join(FONTS_DIR, name)
    if os.path.exists(path):
        return ImageFont.truetype(path, size)
    return ImageFont.load_default()

FONT_TITLE = get_font('segoeuib.ttf', 54)
FONT_SUBTITLE = get_font('segoeui.ttf', 32)
FONT_HEADING = get_font('segoeuib.ttf', 40)
FONT_BODY = get_font('segoeui.ttf', 28)
FONT_BODY_BOLD = get_font('segoeuib.ttf', 28)
FONT_BADGE = get_font('segoeuib.ttf', 22)
FONT_FOOTER = get_font('segoeui.ttf', 22)

SCENES = [
    {
        "id": 1,
        "title": "ЭФФЕКТ ДЖАНИБЕКОВА",
        "subtitle": "Загадка космического кувырка в невесомости",
        "badge": "САЛЮТ-7 • ИСТОРИЯ ОТКРЫТИЯ • 1985 ГОД",
        "text": (
            "Двадцать пятое июня 1985 года. Советская орбитальная станция Салют-7. "
            "Космонавт Владимир Джанибеков откручивает крепёжную гайку-барашек. "
            "Гайка свободно отлетает, плавно вращается в невесомости и вдруг, без каких-либо внешних сил, "
            "совершает резкий кувырок ровно на сто восемьдесят градусов! "
            "Пролетев ещё немного, она повторяет этот кульбит снова и снова."
        ),
        "bullets": [
            ("Открытие на орбите:", "Владимир Джанибеков, станция «Салют-7» (1985 г.)"),
            ("Наблюдаемый эффект:", "Вращающееся тело периодически переворачивается на 180°"),
            ("Особенность:", "Кувырок происходит строго ритмично без контакта и внешних сил")
        ],
        "takeaway": "Случайное орбитальное наблюдение, поставившее в тупик ведущих инженеров космонавтики."
    },
    {
        "id": 2,
        "title": "В ЧЁМ ПАРАДОКС?",
        "subtitle": "Кажущееся нарушение законов физики и мифы",
        "badge": "ФИЗИЧЕСКИЙ ПАРАДОКС • ЗАКОНЫ СОХРАНЕНИЯ",
        "text": (
            "На первый взгляд кажется, что нарушается фундаментальный закон сохранения момента импульса. "
            "В прессе даже возникли мифы: якобы Земля в любой момент может так же кувыркнуться, "
            "поменяв полюса местами. Однако никакой мистики здесь нет. "
            "Полный вектор момента импульса и кинетическая энергия остаются абсолютно постоянными. "
            "Всё дело в геометрии распределения массы твердого тела."
        ),
        "bullets": [
            ("Закон сохранения момента L:", "Полный вектор кинетического момента L строго постоянен в пространстве"),
            ("Кинетическая энергия T:", "Энергия вращения сохраняется, меняются лишь компоненты угловой скорости"),
            ("Миф о перевороте Земли:", "Опровергнут: геометрия вращения Земли исключает такой переворот")
        ],
        "takeaway": "Вектор момента импульса в пространстве неподвижен — кувыркается само тело относительно вектора L."
    },
    {
        "id": 3,
        "title": "ТРИ ГЛАВНЫХ МОМЕНТА ИНЕРЦИИ",
        "subtitle": "Геометрия масс несимметричного твердого тела",
        "badge": "КЛАССИЧЕСКАЯ МЕХАНИКА • ОСИ ИНЕРЦИИ",
        "text": (
            "У любого несимметричного твёрдого тела существуют три главные взаимно перпендикулярные оси инерции. "
            "Расположим их моменты инерции по возрастанию: и один — наименьший, и два — промежуточный, "
            "и три — наибольший. "
            "Вращение вокруг оси с наименьшим или наибольшим моментом абсолютно устойчиво. "
            "Но если закрутить тело вокруг промежуточной оси и два — малейшие возмущения приводят к потере стабильности!"
        ),
        "bullets": [
            ("I₁ (Минимальный момент):", "Вращение абсолютно устойчиво к возмущениям"),
            ("I₂ (Промежуточный момент):", "Вращение НЕУСТОЙЧИВО — малейшая флуктуация вызывает кувырок"),
            ("I₃ (Максимальный момент):", "Вращение абсолютно устойчиво к возмущениям")
        ],
        "takeaway": "Условие эффекта Джанибекова: тело обязательно должно вращаться вокруг ПРОМЕЖУТОЧНОЙ оси I₂."
    },
    {
        "id": 4,
        "title": "УРАВНЕНИЯ ЭЙЛЕРА И СИМУЛЯЦИЯ",
        "subtitle": "Математическое доказательство неустойчивости",
        "badge": "МАТЕМАТИЧЕСКАЯ МОДЕЛЬ • ТЕОРЕМА ТЕННИСНОЙ РАКЕТКИ",
        "text": (
            "Свободное движение твердого тела описывается динамическими уравнениями Леонарда Эйлера. "
            "Если исследовать устойчивость уравнений методом малых возмущений, знаки коэффициентов для первой и третьей осей "
            "дают периодические тригонометрические решения. "
            "Но для промежуточной оси коэффициенты приводят к экспоненциальному росту отклонения! "
            "В результате тело неизбежно переходит на другую ветвь траектории, переворачиваясь на сто восемьдесят градусов."
        ),
        "has_simulation": True,
        "takeaway": "Экспоненциальный рост малых возмущений делает кувырок математически неизбежным."
    },
    {
        "id": 5,
        "title": "ЗЕМЛЯ И СПУТНИКИ СВЯЗИ",
        "subtitle": "Применение в телекоммуникациях и аэрокосмической отрасли",
        "badge": "МТУСИ • КОСМИЧЕСКАЯ СВЯЗЬ И ИНЖЕНЕРИЯ",
        "text": (
            "Почему же не кувыркается наша Земля? "
            "Благодаря центробежным силам Земля сплюснута у полюсов, и ось её суточного вращения — это ось с максимальным моментом инерции. "
            "Поэтому наша планета устойчива миллиарды лет. "
            "Однако для телекоммуникационных спутников и аппаратов связи на орбите этот эффект критичен. "
            "Если инженеры не учтут промежуточную ось, спутник начнёт неконтролируемо вращаться и потеряет связь с Землёй!"
        ),
        "bullets": [
            ("Планета Земля:", "Вращается вокруг оси I_max — кувырок физически невозможен"),
            ("Космические аппараты:", "Бортовые системы стабилизации (гиродины) гасят опасные моменты"),
            ("Спутники связи МТУСИ:", "Правильная развесовка аппаратуры гарантирует непрерывную радиосвязь")
        ],
        "takeaway": "Знание механики Эйлера — фундаментальная основа для проектирования спутниковых группировок."
    },
    {
        "id": 6,
        "title": "СПАСИБО ЗА ВНИМАНИЕ!",
        "subtitle": "Физика вокруг нас — от гайки до спутников связи",
        "badge": "МТУСИ • КАФЕДРА ФИЗИКИ • 2026",
        "text": (
            "Таким образом, эффект Джанибекова — это красивейшая демонстрация классической механики, "
            "где строгие математические уравнения объясняют самое загадочное поведение тел в открытом космосе. "
            "Доклад подготовил студент группы БВТ2602 Бородин Леонид. "
            "Спасибо за внимание!"
        ),
        "bullets": [
            ("Автор работы:", "Бородин Леонид Сергеевич"),
            ("Учебная группа:", "БВТ2602 (Кафедра физики МТУСИ)"),
            ("Канал кафедры:", "@MoscowPhysics")
        ],
        "takeaway": "Классическая физика не перестаёт удивлять и вдохновлять будущих инженеров связи!"
    }
]

def generate_audio_files():
    print("Generating audio with gTTS (Google Speech Engine)...", flush=True)
    for scene in SCENES:
        mp3_path = os.path.join(OUT_DIR, f"audio_{scene['id']}.mp3")
        tts = gTTS(scene["text"], lang="ru", slow=False)
        tts.save(mp3_path)
        print(f"  [+] Scene {scene['id']} audio ready: {mp3_path}", flush=True)

def get_audio_duration(file_path):
    cmd = [
        FFMPEG_EXE, "-i", file_path
    ]
    res = subprocess.run(cmd, stderr=subprocess.PIPE, stdout=subprocess.PIPE, text=True)
    import re
    m = re.search(r"Duration:\s*(\d+):(\d+):(\d+\.\d+)", res.stderr)
    if m:
        hours, mins, secs = m.groups()
        return float(hours)*3600 + float(mins)*60 + float(secs)
    return 10.0

def generate_simulation_chart():
    I1, I2, I3 = 1.0, 2.0, 3.0
    w0 = [0.01, 2.0, 0.01]  # perturbation around I2
    
    def euler(t, w):
        w1, w2, w3 = w
        return [
            (I2 - I3) / I1 * w2 * w3,
            (I3 - I1) / I2 * w3 * w1,
            (I1 - I2) / I3 * w1 * w2
        ]
        
    t_span = (0, 20)
    t_eval = np.linspace(0, 20, 500)
    sol = solve_ivp(euler, t_span, w0, t_eval=t_eval)
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 4.2), facecolor='#0B1120')
    
    # Time plot
    ax1.set_facecolor('#0B1120')
    ax1.plot(sol.t, sol.y[1], color='#38BDF8', lw=2.5, label='ω₂ (вокруг оси I₂)')
    ax1.plot(sol.t, sol.y[0], color='#F43F5E', lw=1.8, ls='--', label='ω₁ (возмущение)')
    ax1.plot(sol.t, sol.y[2], color='#10B981', lw=1.8, ls=':', label='ω₃ (кувырок)')
    ax1.set_title("Кувырок угловой скорости ω(t)", color='#F8FAFC', fontsize=14, fontweight='bold', pad=10)
    ax1.set_xlabel("Время t (сек)", color='#94A3B8', fontsize=11)
    ax1.set_ylabel("Угловая скорость ω", color='#94A3B8', fontsize=11)
    ax1.tick_params(colors='#94A3B8')
    ax1.grid(True, color='#1E293B', ls='--')
    ax1.legend(facecolor='#1E293B', edgecolor='#334155', labelcolor='#F8FAFC', fontsize=10)
    
    # 3D/Phase Trajectory
    ax2.set_facecolor('#0B1120')
    ax2.plot(sol.y[1], sol.y[0], color='#818CF8', lw=2.2)
    ax2.scatter([2.0], [0.0], color='#F59E0B', s=80, zorder=5, label='Старт')
    ax2.scatter([-2.0], [0.0], color='#F43F5E', s=80, zorder=5, label='Кувырок (180°)')
    ax2.set_title("Фазовый портрет (ω₂ vs ω₁)", color='#F8FAFC', fontsize=14, fontweight='bold', pad=10)
    ax2.set_xlabel("ω₂ (промежуточная ось)", color='#94A3B8', fontsize=11)
    ax2.set_ylabel("ω₁ (малое возмущение)", color='#94A3B8', fontsize=11)
    ax2.tick_params(colors='#94A3B8')
    ax2.grid(True, color='#1E293B', ls='--')
    ax2.legend(facecolor='#1E293B', edgecolor='#334155', labelcolor='#F8FAFC', fontsize=10)
    
    for spine in ax1.spines.values():
        spine.set_color('#334155')
    for spine in ax2.spines.values():
        spine.set_color('#334155')
        
    plt.tight_layout()
    chart_path = os.path.join(OUT_DIR, "sim_chart.png")
    plt.savefig(chart_path, dpi=160, bbox_inches='tight', facecolor=fig.get_facecolor())
    plt.close()
    return chart_path

def render_slide(scene, sim_chart_path=None):
    width, height = 1920, 1080
    img = Image.new('RGB', (width, height), color='#070B19')
    draw = ImageDraw.Draw(img)
    
    # Space gradient
    for y in range(height):
        ratio = y / height
        r = int(7 + ratio * 8)
        g = int(11 + ratio * 15)
        b = int(25 + ratio * 25)
        draw.line([(0, y), (width, y)], fill=(r, g, b))
        
    # Grid lines
    for x in range(0, width, 120):
        draw.line([(x, 0), (x, height)], fill=(255, 255, 255, 8), width=1)
    for y in range(0, height, 120):
        draw.line([(0, y), (width, y)], fill=(255, 255, 255, 8), width=1)

    # Top Brand Bar
    draw.rectangle([(80, 45), (width - 80, 95)], fill="#0F172A", outline="#1E293B", width=2)
    draw.text((110, 56), "МТУСИ  |  КАФЕДРА ФИЗИКИ  |  ВИДЕОПРОЕКТЫ", fill="#38BDF8", font=FONT_BADGE)
    draw.text((width - 360, 56), "@MoscowPhysics", fill="#A855F7", font=FONT_BADGE)
    
    # Badge
    badge_text = scene.get("badge", "ФИЗИКА")
    draw.rounded_rectangle([(80, 125), (750, 175)], radius=10, fill="#1E293B", outline="#38BDF8", width=2)
    draw.text((105, 137), badge_text, fill="#38BDF8", font=FONT_BADGE)
    
    # Titles
    draw.text((80, 205), scene["title"], fill="#F8FAFC", font=FONT_TITLE)
    draw.text((80, 280), scene["subtitle"], fill="#94A3B8", font=FONT_SUBTITLE)
    draw.line([(80, 335), (width - 80, 335)], fill="#334155", width=2)
    
    # Content Area
    if scene.get("has_simulation") and sim_chart_path:
        chart = Image.open(sim_chart_path)
        chart = chart.resize((1760, 440), Image.Resampling.LANCZOS)
        img.paste(chart, (80, 370))
        
        draw.rounded_rectangle([(80, 830), (width - 80, 915)], radius=12, fill="#0F172A", outline="#818CF8", width=2)
        formula_text = "Динамические уравнения Эйлера:   I₁·ω̇₁ = (I₂ - I₃)ω₂ω₃   |   I₂·ω̇₂ = (I₃ - I₁)ω₃ω₁   |   I₃·ω̇₃ = (I₁ - I₂)ω₁ω₂"
        draw.text((110, 855), formula_text, fill="#E2E8F0", font=FONT_BODY_BOLD)
    else:
        bullets = scene.get("bullets", [])
        y_pos = 380
        for i, (head, desc) in enumerate(bullets):
            card_box = [(80, y_pos), (width - 80, y_pos + 120)]
            draw.rounded_rectangle(card_box, radius=16, fill="#0F172A", outline="#1E293B", width=2)
            
            draw.ellipse([(110, y_pos + 35), (160, y_pos + 85)], fill="#1E293B", outline="#38BDF8", width=2)
            draw.text((127, y_pos + 42), str(i + 1), fill="#38BDF8", font=FONT_HEADING)
            
            draw.text((190, y_pos + 25), head, fill="#F8FAFC", font=FONT_BODY_BOLD)
            draw.text((190, y_pos + 68), desc, fill="#94A3B8", font=FONT_BODY)
            y_pos += 150
            
        if scene.get("takeaway"):
            takeaway_box = [(80, 840), (width - 80, 925)]
            draw.rounded_rectangle(takeaway_box, radius=14, fill="#1E1B4B", outline="#6366F1", width=2)
            draw.text((110, 865), "ВЫВОД: " + scene["takeaway"], fill="#C7D2FE", font=FONT_BODY_BOLD)
            
    # Footer
    draw.line([(80, 960), (width - 80, 960)], fill="#1E293B", width=1)
    footer_text = f"Студент: Бородин Л. С. (БВТ2602)   •   Кафедра физики МТУСИ   •   2026   •   Слайд {scene['id']} из {len(SCENES)}"
    draw.text((80, 990), footer_text, fill="#64748B", font=FONT_FOOTER)
    
    slide_path = os.path.join(OUT_DIR, f"slide_{scene['id']}.png")
    img.save(slide_path, "PNG")
    print(f"  [+] Slide {scene['id']} saved: {slide_path}", flush=True)
    return slide_path

def build_scene_video(scene_id, duration):
    slide_img = os.path.join(OUT_DIR, f"slide_{scene_id}.png")
    audio_file = os.path.join(OUT_DIR, f"audio_{scene_id}.mp3")
    out_video = os.path.join(OUT_DIR, f"scene_{scene_id}.mp4")
    
    total_sec = duration + 0.5
    cmd = [
        FFMPEG_EXE, "-y",
        "-loop", "1",
        "-i", slide_img,
        "-i", audio_file,
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
    print(f"  [+] Video segment {scene_id} created ({total_sec:.1f}s)", flush=True)
    return out_video

def concatenate_all(video_files):
    concat_txt = os.path.join(OUT_DIR, "concat_list.txt")
    with open(concat_txt, "w", encoding="utf-8") as f:
        for vf in video_files:
            normalized = vf.replace("\\", "/")
            f.write(f"file '{normalized}'\n")
            
    final_output = os.path.join(OUT_DIR, "Эффект_Джанибекова_Бородин_БВТ2602.mp4")
    cmd = [
        FFMPEG_EXE, "-y",
        "-f", "concat",
        "-safe", "0",
        "-i", concat_txt,
        "-c", "copy",
        final_output
    ]
    subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print(f"\nFINAL VIDEO CREATED: {final_output}", flush=True)
    return final_output

def main():
    print("=== STARTING DZHANIBEKOV VIDEO BUILD PIPELINE ===\n", flush=True)
    generate_audio_files()
    
    print("\nGenerating numerical simulation of Euler equations in scipy...", flush=True)
    sim_chart_path = generate_simulation_chart()
    print("  [+] Simulation chart rendered successfully.", flush=True)
    
    print("\nRendering high-res 1080p slide graphics...", flush=True)
    slide_paths = []
    for sc in SCENES:
        sp = render_slide(sc, sim_chart_path if sc.get("has_simulation") else None)
        slide_paths.append(sp)
        
    print("\nAssembling audio-video segments...", flush=True)
    segment_videos = []
    total_duration = 0.0
    for sc in SCENES:
        aud = os.path.join(OUT_DIR, f"audio_{sc['id']}.mp3")
        dur = get_audio_duration(aud)
        total_duration += dur
        v_seg = build_scene_video(sc['id'], dur)
        segment_videos.append(v_seg)
        
    print(f"\nTotal video duration: {total_duration:.1f} seconds (~{total_duration/60:.1f} min)", flush=True)
    
    print("\nConcatenating all segments into final video...", flush=True)
    final_mp4 = concatenate_all(segment_videos)
    print("\n=== PIPELINE COMPLETED SUCCESSFULLY ===", flush=True)

if __name__ == "__main__":
    main()
