import os
import subprocess
import imageio_ffmpeg
from gtts import gTTS
import re

FFMPEG = imageio_ffmpeg.get_ffmpeg_exe()
WORKDIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Казимир_банана")
SRC_VIDEO = os.path.join(WORKDIR, "casimir_effect_moscowphysics.mp4")
OUT_VIDEO = os.path.join(WORKDIR, "casimir_effect_WITH_VOICEOVER.mp4")
TEMP_DIR = os.path.join(WORKDIR, "temp_audio")
os.makedirs(TEMP_DIR, exist_ok=True)

TIMED_SCRIPT = [
    (0.0, 6.0, "Эффект Казимира. Как абсолютная пустота способна толкать предметы?"),
    (6.0, 13.0, "Представьте две идеально гладкие, незаряженные зеркальные пластины в полном вакууме на расстоянии в несколько нанометров. И вдруг… они сами начинают притягиваться."),
    (13.0, 18.0, "Гравитация здесь ничтожна. Заряда нет. Магнитного поля тоже. Тогда что их толкает?"),
    (18.0, 26.0, "В квантовой физике вакуум вовсе не пустой. Это кипящий океан электромагнитных колебаний, где постоянно рождаются и исчезают виртуальные фотоны."),
    (26.0, 33.0, "Даже при абсолютном нуле поле не может полностью замереть — это запрещает принцип неопределённости Гейзенберга."),
    (33.0, 43.0, "Когда мы ставим две проводящие пластины на расстоянии а, зазор между ними работает как резонатор. Словно струна гитары, он пропускает только стоячие волны с узлами на стенках."),
    (43.0, 49.0, "В результате длинные волны внутрь просто не помещаются, тогда как снаружи разрешён весь спектр колебаний."),
    (49.0, 59.0, "Снаружи виртуальных фотонов оказывается больше, чем внутри. Избыточное давление квантового вакуума буквально сдавливает пластины навстречу друг другу."),
    (59.0, 69.0, "В 1948 году нидерландский физик Хендрик Казимир вычислил эту силу. В одной красивой формуле сошлись постоянная Планка, скорость света и расстояние в четвёртой степени."),
    (69.0, 79.0, "Именно четвёртая степень делает эффект взрывным: сблизили пластины всего вдвое — сила выросла в шестнадцать раз. В десять раз ближе — и она сильнее уже в десять тысяч раз!"),
    (79.0, 88.0, "На одном микроне давление почти незаметно. На ста нанометрах его уже легко измерить. А при зазоре в десять нанометров пустота давит с силой больше одной атмосферы!"),
    (88.0, 96.0, "Долгое время эффект считали чистой теорией, но опыты с крутильным маятником и микромеханикой подтвердили формулу Казимира с точностью выше одного процента."),
    (96.0, 106.0, "Сегодня это уже не экзотика, а головная боль инженеров: в микрочипах и наномеханизмах крошечные детали на наномасштабе могут намертво слипаться."),
    (106.0, 113.0, "А в 2009 году учёные показали обратное: если поместить между телами особую жидкость, притяжение сменяется квантовой левитацией — отталкиванием!"),
    (113.0, 120.0, "Даже абсолютная пустота обладает энергией — и способна совершать реальную работу.")
]

def get_duration(file_path):
    cmd = [FFMPEG, "-i", file_path]
    res = subprocess.run(cmd, stderr=subprocess.PIPE, stdout=subprocess.PIPE, text=True)
    m = re.search(r"Duration:\s*(\d+):(\d+):(\d+\.\d+)", res.stderr)
    if m:
        h, mn, s = m.groups()
        return float(h)*3600 + float(mn)*60 + float(s)
    return 0.0

def build_harmonious_voiceover():
    print("1. Generating voice fragments and adjusting tempos...", flush=True)
    adjusted_files = []
    
    for i, (t_start, t_end, text) in enumerate(TIMED_SCRIPT):
        raw_mp3 = os.path.join(TEMP_DIR, f"raw_{i}.mp3")
        adj_wav = os.path.join(TEMP_DIR, f"adj_{i}.wav")
        
        # Synthesize with gTTS
        if not os.path.exists(raw_mp3):
            tts = gTTS(text, lang='ru')
            tts.save(raw_mp3)
            
        dur = get_duration(raw_mp3)
        available_slot = t_end - t_start - 0.4  # leave 0.4s breathing pause
        
        # Calculate speed ratio
        speed = 1.0
        if dur > available_slot:
            speed = min(1.35, dur / available_slot)
            
        print(f"  [+] Phrase {i+1:02d} [{t_start:03.0f}s - {t_end:03.0f}s]: raw={dur:.1f}s, speed={speed:.2f}x", flush=True)
        
        # Adjust tempo with FFmpeg atempo filter
        cmd_adj = [
            FFMPEG, "-y",
            "-i", raw_mp3,
            "-filter:a", f"atempo={speed:.3f}",
            "-ar", "44100",
            adj_wav
        ]
        subprocess.run(cmd_adj, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        adjusted_files.append((t_start, adj_wav))
        
    print("\n2. Assembling full 120-second voice track aligned to timestamps...", flush=True)
    # Build filter_complex to delay each audio fragment to its t_start
    full_voice_wav = os.path.join(TEMP_DIR, "full_voice_aligned.wav")
    
    inputs = []
    delays = []
    for i, (t_start, adj_wav) in enumerate(adjusted_files):
        inputs.extend(["-i", adj_wav])
        delay_ms = int(t_start * 1000)
        delays.append(f"[{i}:a]adelay={delay_ms}|{delay_ms}[a{i}]")
        
    mix_inputs = "".join([f"[a{i}]" for i in range(len(adjusted_files))])
    filter_complex = ";".join(delays) + f";{mix_inputs}amix=inputs={len(adjusted_files)}:duration=longest:normalize=0[voice_out]"
    
    cmd_assemble = [
        FFMPEG, "-y",
        *inputs,
        "-filter_complex", filter_complex,
        "-map", "[voice_out]",
        "-t", "120",
        "-ar", "44100",
        full_voice_wav
    ]
    subprocess.run(cmd_assemble, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print("  [+] Synchronized voice track created successfully!")
    
    print("\n3. Blending voiceover with the user's background music harmoniously...", flush=True)
    # User's background music is preserved!
    # We slightly duck/lower the background music by -4dB and enhance the voice so they blend like a documentary
    # Video stream is copied directly (0 quality loss, fast!)
    cmd_mix = [
        FFMPEG, "-y",
        "-i", SRC_VIDEO,          # [0:v] and [0:a] (original video and beautiful music)
        "-i", full_voice_wav,      # [1:a] (aligned voiceover)
        "-filter_complex",
        "[0:a]volume=0.6[bg_music];"
        "[1:a]volume=1.35,highpass=f=80,lowpass=f=12000[voice_clean];"
        "[bg_music][voice_clean]amix=inputs=2:duration=first:dropout_transition=2[a_out]",
        "-map", "0:v",             # Original video unchanged!
        "-map", "[a_out]",         # Harmoniously blended audio
        "-c:v", "copy",            # Fast zero-loss video copy
        "-c:a", "aac",
        "-b:a", "256k",
        OUT_VIDEO
    ]
    subprocess.run(cmd_mix, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print(f"\n🎉 SUCCESS! New video created without modifying original:")
    print(f"  --> {OUT_VIDEO}")

if __name__ == "__main__":
    build_harmonious_voiceover()
