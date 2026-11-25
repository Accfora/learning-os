"""
Скрипт генерации совершенной академической презентации по реферату:
«Миф как мировоззренческая структура» (В. К. Шрейбер)
Дисциплина: Основы российской государственности (ОРГ), МТУСИ.

Учтены все пожелания:
1. План доклада (Слайд 2): строго построчный 6х1 во всю ширину слайда (от 01 до 06 сверху-вниз).
   Чёткие номерные бейджи, полужирный заголовок, золотой дефис и лаконичное пояснение.
2. Тематические смарт-значки (иконки как в презентации по Куликовской битве):
   внедрены на ключевых смысловых слайдах (Слайды 3, 5, 8, 9, 11, 12, 14, 15),
   олицетворяя содержание каждого пункта (🚀, 🔬, 🌐, ⚡, ⚖️, 🧭, ⚙️, 🔗, 🔮, ⏳, 🔄, 🛑, 🛡️, 🏛️ и др.).
   На остальных слайдах сохранён сдержанный академический маркер.
3. Единый формат плашек-подвыводов (Takeaway Box) на лавандово-индиговом фоне с фиолетовой каймой.
4. Полное отсутствие знаков $ во всей презентации.
5. Титульный слайд strictly по образцу Чехов.pptx (без кафедры философии, ОРГ, БВТ2602).
"""

import os
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE

def build_presentation():
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6]

    base_dir = os.path.dirname(__file__)
    output_path = os.path.join(base_dir, "Миф_как_мировоззренческая_структура_Шрейбер_презентация.pptx")
    assets_dir = os.path.join(base_dir, "assets")

    img_cosmos = os.path.join(assets_dir, "myth_cosmos.jpg")
    img_digital = os.path.join(assets_dir, "digital_media.jpg")
    img_statehood = os.path.join(assets_dir, "russian_statehood.jpg")

    # Палитра
    COLOR_BG = RGBColor(248, 249, 250)         # Теплый светлый фон
    COLOR_PRIMARY = RGBColor(24, 43, 73)       # Благородный академический темно-синий
    COLOR_ACCENT = RGBColor(212, 118, 38)      # Теплый янтарно-золотой
    COLOR_TEXT = RGBColor(43, 45, 66)          # Читаемый графитовый основной текст
    COLOR_MUTED = RGBColor(108, 117, 125)      # Вспомогательный серый
    
    # Единый стиль плашки подвывода (takeaway callout box)
    COLOR_TAG_BG = RGBColor(238, 242, 255)     # Мягкий лавандово-индиго фон
    COLOR_TAG_BORDER = RGBColor(199, 210, 254) # Деликатная фиолетовая кайма
    COLOR_TAG_TEXT = RGBColor(67, 56, 202)     # Глубокий индиго акцентный текст

    CARD_BG = RGBColor(255, 255, 255)
    CARD_BORDER = RGBColor(226, 232, 240)

    COLOR_GREEN_BG = RGBColor(240, 253, 244)
    COLOR_GREEN_BORDER = RGBColor(187, 247, 208)
    COLOR_GREEN_TEXT = RGBColor(22, 101, 52)

    COLOR_RED_BG = RGBColor(254, 242, 242)
    COLOR_RED_BORDER = RGBColor(254, 202, 202)
    COLOR_RED_TEXT = RGBColor(153, 27, 27)

    def set_slide_background(slide):
        bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height)
        bg.fill.solid()
        bg.fill.fore_color.rgb = COLOR_BG
        bg.line.fill.background()

    def add_header(slide, title_text, category="РЕФЕРАТ: МИФ КАК МИРОВОЗЗРЕНЧЕСКАЯ СТРУКТУРА", slide_num=None):
        cat_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.35), Inches(10.5), Inches(0.35))
        ctf = cat_box.text_frame
        ctf.margin_left = ctf.margin_top = ctf.margin_right = ctf.margin_bottom = 0
        p_c = ctf.paragraphs[0]
        p_c.text = category.upper()
        p_c.font.size = Pt(11)
        p_c.font.bold = True
        p_c.font.color.rgb = COLOR_ACCENT
        p_c.font.name = "Arial"

        title_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.65), Inches(11.733), Inches(0.85))
        ttf = title_box.text_frame
        ttf.word_wrap = True
        ttf.margin_left = ttf.margin_top = ttf.margin_right = ttf.margin_bottom = 0
        p_t = ttf.paragraphs[0]
        p_t.text = title_text
        p_t.font.size = Pt(23)
        p_t.font.bold = True
        p_t.font.color.rgb = COLOR_PRIMARY
        p_t.font.name = "Georgia"

        if slide_num:
            num_box = slide.shapes.add_textbox(Inches(11.8), Inches(0.35), Inches(0.8), Inches(0.4))
            ntf = num_box.text_frame
            ntf.margin_left = ntf.margin_top = ntf.margin_right = ntf.margin_bottom = 0
            p_n = ntf.paragraphs[0]
            p_n.text = f"{slide_num:02d}"
            p_n.font.size = Pt(13)
            p_n.font.bold = True
            p_n.font.color.rgb = COLOR_MUTED
            p_n.font.name = "Arial"
            p_n.alignment = PP_ALIGN.RIGHT

    def add_card(slide, left, top, width, height, title=None, bg_color=CARD_BG, border_color=CARD_BORDER):
        card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
        card.fill.solid()
        card.fill.fore_color.rgb = bg_color
        if border_color:
            card.line.color.rgb = border_color
            card.line.width = Pt(1.5)
        else:
            card.line.fill.background()

        if title:
            tb = slide.shapes.add_textbox(left + Inches(0.3), top + Inches(0.22), width - Inches(0.6), Inches(0.45))
            tf = tb.text_frame
            tf.word_wrap = True
            tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0
            p = tf.paragraphs[0]
            p.text = title
            p.font.size = Pt(16)
            p.font.bold = True
            p.font.color.rgb = COLOR_PRIMARY
            p.font.name = "Georgia"
        return card

    def add_takeaway_box(slide, text, top=Inches(6.25), height=Inches(0.85)):
        """Единый гармоничный формат подвывода на всех слайдах."""
        card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), top, Inches(11.733), height)
        card.fill.solid()
        card.fill.fore_color.rgb = COLOR_TAG_BG
        card.line.color.rgb = COLOR_TAG_BORDER
        card.line.width = Pt(1.5)
        tb = slide.shapes.add_textbox(Inches(1.0), top + Inches(0.1), Inches(11.333), height - Inches(0.2))
        tf = tb.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0
        p = tf.paragraphs[0]
        p.text = text
        p.font.size = Pt(15.5)
        p.font.bold = True
        p.font.color.rgb = COLOR_TAG_TEXT
        p.font.name = "Georgia"
        p.alignment = PP_ALIGN.CENTER
        return card

    def add_bullet(tf, bold_lead, body_text, font_size=Pt(15), lead_color=COLOR_PRIMARY, text_color=COLOR_TEXT, bullet_icon="• ", space_after=Pt(8)):
        """Смарт-пункт списка: тематический значок/иконка, полужирный термин и пояснение."""
        if len(tf.paragraphs) == 1 and tf.paragraphs[0].text == "":
            p = tf.paragraphs[0]
        else:
            p = tf.add_paragraph()
        p.space_after = space_after
        p.font.size = font_size
        p.font.name = "Arial"

        if bullet_icon:
            r0 = p.add_run()
            icon_str = bullet_icon if bullet_icon.endswith(" ") else f"{bullet_icon} "
            r0.text = icon_str
            r0.font.bold = True
            # Для стандартных маркеров (точка, стрелка) ставим акцентный цвет
            if bullet_icon.strip() in ["•", "▸", "→"]:
                r0.font.color.rgb = COLOR_ACCENT
            # Для эмодзи задаем шрифт Segoe UI Emoji для максимальной четкости
            if any(ord(c) > 0x2000 for c in bullet_icon):
                r0.font.name = "Segoe UI Emoji"
            else:
                r0.font.name = "Arial"

        if bold_lead:
            r1 = p.add_run()
            r1.text = f"{bold_lead} " if not bold_lead.endswith(" ") else bold_lead
            r1.font.bold = True
            r1.font.color.rgb = lead_color
            r1.font.name = "Arial"

        r2 = p.add_run()
        r2.text = body_text
        r2.font.bold = False
        r2.font.color.rgb = text_color
        r2.font.name = "Arial"
        return p

    def add_arrow(slide, left, top, width, height, color=COLOR_ACCENT):
        arrow = slide.shapes.add_shape(MSO_SHAPE.RIGHT_ARROW, left, top, width, height)
        arrow.fill.solid()
        arrow.fill.fore_color.rgb = color
        arrow.line.fill.background()
        return arrow

    # ==================== СЛАЙД 1: ТИТУЛЬНЫЙ (КАК В ЧЕХОВ.PPTX) ====================
    s1 = prs.slides.add_slide(blank_layout)
    set_slide_background(s1)

    top_bar = s1.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), Inches(0.7), Inches(11.733), Inches(0.06))
    top_bar.fill.solid()
    top_bar.fill.fore_color.rgb = COLOR_ACCENT
    top_bar.line.fill.background()

    tb_header = s1.shapes.add_textbox(Inches(0.8), Inches(0.9), Inches(11.733), Inches(1.3))
    tf_h = tb_header.text_frame
    tf_h.word_wrap = True
    tf_h.margin_left = tf_h.margin_top = tf_h.margin_right = tf_h.margin_bottom = 0
    p_h = tf_h.paragraphs[0]
    p_h.text = ("МИНИСТЕРСТВО ЦИФРОВОГО РАЗВИТИЯ, СВЯЗИ И МАССОВЫХ КОММУНИКАЦИЙ РОССИЙСКОЙ ФЕДЕРАЦИИ\n"
                "Ордена трудового Красного Знамени федеральное государственное бюджетное\n"
                "образовательное учреждение высшего образования\n"
                "«Московский технический университет связи и информатики»")
    p_h.font.size = Pt(11)
    p_h.font.bold = True
    p_h.font.color.rgb = COLOR_MUTED
    p_h.font.name = "Arial"
    p_h.alignment = PP_ALIGN.CENTER

    tb_title = s1.shapes.add_textbox(Inches(0.8), Inches(2.6), Inches(11.733), Inches(2.2))
    tf_t = tb_title.text_frame
    tf_t.word_wrap = True
    tf_t.margin_left = tf_t.margin_top = tf_t.margin_right = tf_t.margin_bottom = 0

    p_badge = tf_t.paragraphs[0]
    p_badge.text = "РЕФЕРАТ ПО ДИСЦИПЛИНЕ «ОСНОВЫ РОССИЙСКОЙ ГОСУДАРСТВЕННОСТИ»"
    p_badge.font.size = Pt(12)
    p_badge.font.bold = True
    p_badge.font.color.rgb = COLOR_ACCENT
    p_badge.font.name = "Arial"
    p_badge.alignment = PP_ALIGN.CENTER
    p_badge.space_after = Pt(10)

    p_main = tf_t.add_paragraph()
    p_main.text = "Миф как мировоззренческая структура"
    p_main.font.size = Pt(32)
    p_main.font.bold = True
    p_main.font.color.rgb = COLOR_PRIMARY
    p_main.font.name = "Georgia"
    p_main.alignment = PP_ALIGN.CENTER
    p_main.space_after = Pt(10)

    p_sub = tf_t.add_paragraph()
    p_sub.text = "Концепция В. К. Шрейбера: от архаического сознания к принятию решений в XXI веке"
    p_sub.font.size = Pt(16)
    p_sub.font.color.rgb = COLOR_MUTED
    p_sub.font.name = "Georgia"
    p_sub.alignment = PP_ALIGN.CENTER

    tb_bottom = s1.shapes.add_textbox(Inches(0.8), Inches(5.1), Inches(11.733), Inches(1.6))
    tf_b = tb_bottom.text_frame
    tf_b.word_wrap = True
    tf_b.margin_left = tf_b.margin_top = tf_b.margin_right = tf_b.margin_bottom = 0

    p_disc = tf_b.paragraphs[0]
    p_disc.text = "Дисциплина: Основы российской государственности"
    p_disc.font.size = Pt(14)
    p_disc.font.bold = True
    p_disc.font.color.rgb = COLOR_PRIMARY
    p_disc.font.name = "Arial"
    p_disc.alignment = PP_ALIGN.CENTER
    p_disc.space_after = Pt(6)

    p_stud = tf_b.add_paragraph()
    p_stud.text = "Выполнил: студент группы БВТ2602  Бородин Леонид Сергеевич"
    p_stud.font.size = Pt(15)
    p_stud.font.color.rgb = COLOR_TEXT
    p_stud.font.name = "Arial"
    p_stud.alignment = PP_ALIGN.CENTER
    p_stud.space_after = Pt(14)

    p_city = tf_b.add_paragraph()
    p_city.text = "Москва, 2026"
    p_city.font.size = Pt(13)
    p_city.font.bold = True
    p_city.font.color.rgb = COLOR_MUTED
    p_city.font.name = "Arial"
    p_city.alignment = PP_ALIGN.CENTER

    # ==================== СЛАЙД 2: ПЛАН ДОКЛАДА (СТРОГО 6х1 ПОСТРОЧНО) ====================
    # Строго линейная вертикальная композиция: 6 горизонтальных карточек во всю ширину
    s2 = prs.slides.add_slide(blank_layout)
    set_slide_background(s2)
    add_header(s2, "План доклада: логика исследования", slide_num=2)

    plan_items = [
        ("01", "Введение. Парадокс XXI века", 
         "Почему век искусственного интеллекта и науки сопровождается всплеском мифологизации? Фокус В. К. Шрейбера."),
        ("02", "Глава 1. Мировоззрение как схема выбора", 
         "Анатомия ситуации принятия решений: триада онтологии (мир), аксиологии (ценности) и праксиологии (действие)."),
        ("03", "Глава 2. Специфика мифологической онтологии", 
         "Познание по аналогии («макрокосм = микрокосм»), всеобщий антропоморфизм, тождество имени и вещи, сакральный прецедент."),
        ("04", "Глава 3. Ценности и регуляция поведения", 
         "Нормативный статус мифа, преодоление релятивизма. Ритуал как борьба с энтропией и институт табу как коллективный барьер."),
        ("05", "Глава 4. Неомифология и государственность", 
         "Конспирология, медиа и алгоритмы соцсетей. Роль ценностного каркаса цивилизации и защита когнитивного суверенитета России."),
        ("06", "Заключение и выводы исследования", 
         "Миф как базовая константа психики при кризисах. Инструменты диагностики манипуляций и защиты личного выбора.")
    ]

    card_w = Inches(11.733)
    row_h = Inches(0.78)
    x_left = Inches(0.8)

    for i, (num, p_title, p_desc) in enumerate(plan_items):
        cur_y = Inches(1.60 + i * 0.89)

        card = s2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x_left, cur_y, card_w, row_h)
        card.fill.solid()
        card.fill.fore_color.rgb = CARD_BG
        card.line.color.rgb = CARD_BORDER
        card.line.width = Pt(1.5)

        # Номерной бейдж
        badge = s2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x_left + Inches(0.15), cur_y + Inches(0.14), Inches(0.65), Inches(0.50))
        badge.fill.solid()
        badge.fill.fore_color.rgb = COLOR_PRIMARY
        badge.line.fill.background()
        p_num = badge.text_frame.paragraphs[0]
        p_num.text = num
        p_num.font.size = Pt(14)
        p_num.font.bold = True
        p_num.font.color.rgb = RGBColor(255, 255, 255)
        p_num.font.name = "Arial"
        p_num.alignment = PP_ALIGN.CENTER

        # Текстовый блок (Заголовок — Пояснение)
        tb = s2.shapes.add_textbox(x_left + Inches(0.95), cur_y + Inches(0.09), card_w - Inches(1.15), row_h - Inches(0.18))
        tf = tb.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0
        p = tf.paragraphs[0]

        r1 = p.add_run()
        r1.text = p_title
        r1.font.size = Pt(14.5)
        r1.font.bold = True
        r1.font.color.rgb = COLOR_PRIMARY
        r1.font.name = "Georgia"

        r_sep = p.add_run()
        r_sep.text = " — "
        r_sep.font.size = Pt(14)
        r_sep.font.bold = True
        r_sep.font.color.rgb = COLOR_ACCENT

        r2 = p.add_run()
        r2.text = p_desc
        r2.font.size = Pt(13)
        r2.font.color.rgb = COLOR_TEXT
        r2.font.name = "Arial"

    # ==================== СЛАЙД 3: ПАРАДОКС XXI ВЕКА (С КАРТИНКОЙ КОСМОСА И СМАРТ-ЗНАЧКАМИ) ====================
    s3 = prs.slides.add_slide(blank_layout)
    set_slide_background(s3)
    add_header(s3, "Парадокс XXI века: почему наука не победила миф?", slide_num=3)

    if os.path.exists(img_cosmos):
        s3.shapes.add_picture(img_cosmos, Inches(0.8), Inches(1.6), Inches(4.8), Inches(5.3))

    add_card(s3, Inches(5.8), Inches(1.6), Inches(6.733), Inches(2.5), title="Ожидание эпохи Просвещения")
    tb = s3.shapes.add_textbox(Inches(6.1), Inches(2.25), Inches(6.1), Inches(1.7))
    tf = tb.text_frame
    tf.word_wrap = True
    add_bullet(tf, "Триумф разума:", "эпоха искусственного интеллекта, квантовых вычислений и покорения космоса.", bullet_icon="🚀")
    add_bullet(tf, "Иллюзия Просвещения:", "предполагалось, что рациональная наука окончательно истребит мифы и предрассудки.", bullet_icon="🔬")

    add_card(s3, Inches(5.8), Inches(4.3), Inches(6.733), Inches(2.6), title="Реальность информационного общества", border_color=COLOR_ACCENT)
    tb = s3.shapes.add_textbox(Inches(6.1), Inches(4.95), Inches(6.1), Inches(1.8))
    tf = tb.text_frame
    tf.word_wrap = True
    add_bullet(tf, "Всплеск неомифологии:", "лавинообразный рост теорий заговора, фейков и сетевых манипуляций.", bullet_icon="🌐")
    add_bullet(tf, "Рефлекс архаики:", "в моменты стресса и кризисов сознание мгновенно возвращается к древнейшим мифологическим схемам мышления!", bullet_icon="⚡")

    # ==================== СЛАЙД 4: В. К. ШРЕЙБЕР И ЕГО ПОДХОД ====================
    s4 = prs.slides.add_slide(blank_layout)
    set_slide_background(s4)
    add_header(s4, "Автор концепции: Виктор Константинович Шрейбер", slide_num=4)

    add_card(s4, Inches(0.8), Inches(1.6), Inches(5.6), Inches(5.3), title="Исследовательский контекст")
    tb = s4.shapes.add_textbox(Inches(1.1), Inches(2.3), Inches(5.0), Inches(4.3))
    tf = tb.text_frame
    tf.word_wrap = True
    add_bullet(tf, "Автор концепции:", "доктор философских наук, профессор Челябинского государственного университета.")
    add_bullet(tf, "Ключевой труд:", "программная статья «Миф как мировоззренческая структура» (Вестник УдГУ, 2016).")
    add_bullet(tf, "Исторический вызов:", "слом советской идеологии породил смысловой вакуум и процесс стихийной архаизации массового сознания.")

    add_card(s4, Inches(6.9), Inches(1.6), Inches(5.6), Inches(5.3), title="Новизна взгляда Шрейбера", border_color=COLOR_ACCENT)
    tb = s4.shapes.add_textbox(Inches(7.2), Inches(2.3), Inches(5.0), Inches(4.3))
    tf = tb.text_frame
    tf.word_wrap = True
    add_bullet(tf, "1. Не сказка и не глупость:", "миф — это не архаическая ошибка, а базовая практическая структура человеческого мышления.", bullet_icon="▸ ")
    add_bullet(tf, "2. Схема принятия решений:", "мировоззрение существует исключительно для выбора действий в ситуации неопределённости.", bullet_icon="▸ ")
    add_bullet(tf, "3. Психологическая матрица:", "миф — самая древняя, прочная и психологически комфортная операционная система выбора.", bullet_icon="▸ ")

    # ==================== СЛАЙД 5: СТРУКТУРА СИТУАЦИИ ВЫБОРА (ИНФОГРАФИКА СО ЗНАЧКАМИ) ====================
    s5 = prs.slides.add_slide(blank_layout)
    set_slide_background(s5)
    add_header(s5, "Анатомия выбора: как человек принимает решения?", slide_num=5)

    card_w_5 = Inches(3.4)
    card_h_5 = Inches(4.2)
    top_pos_5 = Inches(1.8)

    add_card(s5, Inches(0.8), top_pos_5, card_w_5, card_h_5, title="1. Поле возможностей")
    tb = s5.shapes.add_textbox(Inches(1.05), top_pos_5 + Inches(0.8), card_w_5 - Inches(0.5), Inches(3.0))
    tf = tb.text_frame
    tf.word_wrap = True
    add_bullet(tf, "Внешняя среда:", "объективные физические условия и реальные границы мира.", bullet_icon="🌍")
    add_bullet(tf, "Спектр альтернатив:", "перечень того, что вообще физически осуществимо в данной ситуации.", bullet_icon="🧭")

    add_arrow(s5, Inches(4.35), top_pos_5 + Inches(1.8), Inches(0.5), Inches(0.4))

    add_card(s5, Inches(4.95), top_pos_5, card_w_5, card_h_5, title="2. Шкала ценностей", border_color=COLOR_ACCENT)
    tb = s5.shapes.add_textbox(Inches(5.2), top_pos_5 + Inches(0.8), card_w_5 - Inches(0.5), Inches(3.0))
    tf = tb.text_frame
    tf.word_wrap = True
    add_bullet(tf, "Внутренний компас:", "система критериев предпочтения и аксиологических координат.", bullet_icon="⚖️")
    add_bullet(tf, "Селекция блага:", "отделяет добро от зла, определяет, во имя чего стоит действовать.", bullet_icon="🎯")

    add_arrow(s5, Inches(8.5), top_pos_5 + Inches(1.8), Inches(0.5), Inches(0.4))

    add_card(s5, Inches(9.1), top_pos_5, card_w_5, card_h_5, title="3. Программа действия")
    tb = s5.shapes.add_textbox(Inches(9.35), top_pos_5 + Inches(0.8), card_w_5 - Inches(0.5), Inches(3.0))
    tf = tb.text_frame
    tf.word_wrap = True
    add_bullet(tf, "Операционный алгоритм:", "конкретные сценарии, правила, нормы и регламенты.", bullet_icon="⚙️")
    add_bullet(tf, "Воплощение в результат:", "перевод идеального выбора в практическое реальное действие.", bullet_icon="🏁")

    add_takeaway_box(s5, "Вывод Шрейбера: если повреждён хоть один блок — волевое действие человека парализуется!")

    # ==================== СЛАЙД 6: ТРИАДА БЛОКОВ МИРОВОЗЗРЕНИЯ (ИНФОГРАФИКА) ====================
    s6 = prs.slides.add_slide(blank_layout)
    set_slide_background(s6)
    add_header(s6, "Триада мировоззренческих блоков по Шрейберу", slide_num=6)

    blocks = [
        ("ОНТОЛОГИЧЕСКИЙ БЛОК", "Картина мира", "«Что существует и что возможно?»", 
         "Задаёт модель законов природы и социума, определяя объективные координаты физической реальности.", Inches(1.6)),
        ("АКСИОЛОГИЧЕСКИЙ БЛОК", "Система ценностей", "«Что значимо и во имя чего жить?»", 
         "Выступает селективным фильтром: из множества действий отбирает те, что признаются высшим благом.", Inches(3.15)),
        ("ПРАКСИОЛОГИЧЕСКИЙ БЛОК", "Программы поведения", "«Какими алгоритмами действовать?»", 
         "Переводит ценности в сценарии: законы, традиции, моральные заповеди, священные ритуалы и табу.", Inches(4.7))
    ]

    for cat, title, q, desc, y_pos in blocks:
        card = add_card(s6, Inches(0.8), y_pos, Inches(11.733), Inches(1.35))
        tb = s6.shapes.add_textbox(Inches(1.1), y_pos + Inches(0.12), Inches(11.1), Inches(1.1))
        tf = tb.text_frame
        tf.word_wrap = True
        p1 = tf.paragraphs[0]
        p1.text = f"{cat}  •  {title}  →  {q}"
        p1.font.size = Pt(16)
        p1.font.bold = True
        p1.font.color.rgb = COLOR_PRIMARY
        p1.font.name = "Georgia"
        
        p2 = tf.add_paragraph()
        p2.text = desc
        p2.font.size = Pt(14.5)
        p2.font.color.rgb = COLOR_TEXT
        p2.font.name = "Arial"

    add_takeaway_box(s6, "Специфика мифа: все три блока спаяны в абсолютный, нерушимый синкретичный монолит!")

    # ==================== СЛАЙД 7: МЕТОД АНАЛОГИИ И АНТРОПОМОРФИЗМ ====================
    s7 = prs.slides.add_slide(blank_layout)
    set_slide_background(s7)
    add_header(s7, "Онтология мифа: познание через аналогию", slide_num=7)

    add_card(s7, Inches(0.8), Inches(1.8), Inches(4.8), Inches(4.1), title="Микрокосм: Семья и Род")
    tb = s7.shapes.add_textbox(Inches(1.05), Inches(2.55), Inches(4.3), Inches(3.1))
    tf = tb.text_frame
    tf.word_wrap = True
    add_bullet(tf, "Первичный опыт:", "семейно-родовой уклад как самое освоенное и понятное пространство.")
    add_bullet(tf, "Личные отношения:", "воля, любовь, гнев, родительская опека и взаимный сыновний долг.")

    add_arrow(s7, Inches(5.8), Inches(3.4), Inches(0.7), Inches(0.4), color=COLOR_ACCENT)
    tb_eq = s7.shapes.add_textbox(Inches(5.7), Inches(3.9), Inches(0.9), Inches(0.5))
    p_eq = tb_eq.text_frame.paragraphs[0]
    p_eq.text = "АНАЛОГИЯ"
    p_eq.font.size = Pt(11)
    p_eq.font.bold = True
    p_eq.font.color.rgb = COLOR_ACCENT
    p_eq.alignment = PP_ALIGN.CENTER

    add_card(s7, Inches(6.7), Inches(1.8), Inches(5.8), Inches(4.1), title="Макрокосм: Природа и Стихии", border_color=COLOR_PRIMARY)
    tb = s7.shapes.add_textbox(Inches(6.95), Inches(2.55), Inches(5.3), Inches(3.1))
    tf = tb.text_frame
    tf.word_wrap = True
    add_bullet(tf, "Тотальный антропоморфизм:", "стихии, небо, леса и реки мыслятся как живые одушевлённые существа.")
    add_bullet(tf, "Этизация природы:", "нет слепых стихий: засуха или буря — это персональная кара духов за нарушение табу!")

    add_takeaway_box(s7, "Главный эффект: одушевление мира делает стихии этически понятными и доступными для диалога!")

    # ==================== СЛАЙД 8: СЕМИОТИКА: НЕРАЗРЫВНОСТЬ ЗНАКА И ВЕЩИ (СО ЗНАЧКАМИ) ====================
    s8 = prs.slides.add_slide(blank_layout)
    set_slide_background(s8)
    add_header(s8, "Семиотика мифа: нерасчленённость знака и вещи", slide_num=8)

    add_card(s8, Inches(0.8), Inches(1.8), Inches(5.4), Inches(4.15), title="Рациональное: Знак ≠ Вещь")
    tb = s8.shapes.add_textbox(Inches(1.05), Inches(2.55), Inches(4.9), Inches(3.2))
    tf = tb.text_frame
    tf.word_wrap = True
    add_bullet(tf, "Чёткая дихотомия:", "строгое разделение между условным символом и физическим объектом.", bullet_icon="📐")
    add_bullet(tf, "Слово ≠ вещь:", "слово «пламя» не обжигает пальцы, а произнесение «яд» не вызывает отравления.", bullet_icon="💬")
    add_bullet(tf, "Условность знака:", "язык и метафоры воспринимаются как удобные договорные абстракции.", bullet_icon="📜")

    vs_circle = s8.shapes.add_shape(MSO_SHAPE.OVAL, Inches(6.3), Inches(3.4), Inches(0.8), Inches(0.8))
    vs_circle.fill.solid()
    vs_circle.fill.fore_color.rgb = COLOR_ACCENT
    vs_circle.line.fill.background()
    p_vs = vs_circle.text_frame.paragraphs[0]
    p_vs.text = "VS"
    p_vs.font.size = Pt(14)
    p_vs.font.bold = True
    p_vs.font.color.rgb = RGBColor(255, 255, 255)
    p_vs.alignment = PP_ALIGN.CENTER

    add_card(s8, Inches(7.2), Inches(1.8), Inches(5.333), Inches(4.15), title="Мифологическое: Имя ≡ Вещь", border_color=COLOR_PRIMARY)
    tb = s8.shapes.add_textbox(Inches(7.45), Inches(2.55), Inches(4.8), Inches(3.2))
    tf = tb.text_frame
    tf.word_wrap = True
    add_bullet(tf, "Субстанциональное тождество:", "имя, образ и сама вещь слиты в неразрывное физическое целое.", bullet_icon="🔗")
    add_bullet(tf, "Магия имени:", "знать тайное имя существа — значит обладать над ним прямой реальной властью.", bullet_icon="🔮")
    add_bullet(tf, "Действие через образ:", "ритуальное повреждение изображения врага наносит прямой физический вред.", bullet_icon="🕯️")

    add_takeaway_box(s8, "Следствие по Шрейберу: миф невозможно критиковать изнутри — для сомнения нужно отделить знак от вещи!")

    # ==================== СЛАЙД 9: САКРАЛЬНЫЙ ПРЕЦЕДЕНТ (СО ЗНАЧКАМИ) ====================
    s9 = prs.slides.add_slide(blank_layout)
    set_slide_background(s9)
    add_header(s9, "Сакральный прецедент (in illo tempore) и время", slide_num=9)

    add_card(s9, Inches(0.8), Inches(1.8), Inches(5.6), Inches(4.15), title="Циклическое время мифа")
    tb = s9.shapes.add_textbox(Inches(1.05), Inches(2.55), Inches(5.1), Inches(3.2))
    tf = tb.text_frame
    tf.word_wrap = True
    add_bullet(tf, "Отказ от линейности:", "время мыслится не как стрела развития, а как вечный природный круговорот.", bullet_icon="🔄")
    add_bullet(tf, "In illo tempore:", "точка высшей сакральности — изначальное время первотворения богами («во время о́но»).", bullet_icon="⏳")
    add_bullet(tf, "Качественное время:", "ритуалы и праздники позволяют человеку заново войти в первозданный святой исток.", bullet_icon="🌅")

    add_card(s9, Inches(6.9), Inches(1.8), Inches(5.6), Inches(4.15), title="Механизм обоснования порядка", border_color=COLOR_ACCENT)
    tb = s9.shapes.add_textbox(Inches(7.15), Inches(2.55), Inches(5.1), Inches(3.2))
    tf = tb.text_frame
    tf.word_wrap = True
    add_bullet(tf, "Логика прецедента:", "«Так надо поступать, потому что в начале времён первопредок поступил именно так».", bullet_icon="🏛️")
    add_bullet(tf, "Легитимность через повтор:", "истинно лишь то, что безукоризненно воспроизводит сакральный первообразец.", bullet_icon="📜")
    add_bullet(tf, "Табу на инновации:", "любая непроверенная самовольная новация грозит крушением всего мироздания.", bullet_icon="🚫")

    add_takeaway_box(s9, "Сакральный прецедент освобождает от мук выбора: истинный ответ уже дан богами в начале времён!")

    # ==================== СЛАЙД 10: НОРМАТИВНЫЙ СТАТУС ЦЕННОСТЕЙ ====================
    s10 = prs.slides.add_slide(blank_layout)
    set_slide_background(s10)
    add_header(s10, "Аксиология мифа: устранение морального релятивизма", slide_num=10)

    add_card(s10, Inches(0.8), Inches(1.8), Inches(5.6), Inches(4.15), title="Современная этика: свобода и сомнения")
    tb = s10.shapes.add_textbox(Inches(1.05), Inches(2.55), Inches(5.1), Inches(3.2))
    tf = tb.text_frame
    tf.word_wrap = True
    add_bullet(tf, "Индивидуальный поиск:", "человек вынужден сам мучительно определять и отстаивать критерии добра и зла.")
    add_bullet(tf, "Моральный релятивизм:", "ценности постоянно подвергаются критике, рефлексии, сомнениям и пересмотру.")
    add_bullet(tf, "Бремя сомнений:", "постоянная экзистенциальная тревога и тяжёлый груз единоличной ответственности.")

    add_card(s10, Inches(6.9), Inches(1.8), Inches(5.6), Inches(4.15), title="Мифологическая этика: космический закон", border_color=COLOR_ACCENT)
    tb = s10.shapes.add_textbox(Inches(7.15), Inches(2.55), Inches(5.1), Inches(3.2))
    tf = tb.text_frame
    tf.word_wrap = True
    add_bullet(tf, "Статус физического закона:", "моральные ценности непререкаемы и абсолютны, как восход солнца.")
    add_bullet(tf, "Исключение произвола:", "выбор возможен лишь между соблюдением нормы и гибелью всего рода.")
    add_bullet(tf, "Коллективная порука:", "грех одного человека навлекает стихийную катастрофу на всю общину.")

    add_takeaway_box(s10, "Вывод: ценности в мифе — не предмет торга или рефлексии, а священный закон выживания общины!")

    # ==================== СЛАЙД 11: РИТУАЛ И ТАБУ (СО ЗНАЧКАМИ) ====================
    s11 = prs.slides.add_slide(blank_layout)
    set_slide_background(s11)
    add_header(s11, "Праксиология мифа: ритуал и табу", slide_num=11)

    add_card(s11, Inches(0.8), Inches(1.8), Inches(5.6), Inches(4.15), title="РИТУАЛ (Позитивное предписание)", bg_color=COLOR_GREEN_BG, border_color=COLOR_GREEN_BORDER)
    tb = s11.shapes.add_textbox(Inches(1.05), Inches(2.55), Inches(5.1), Inches(3.2))
    tf = tb.text_frame
    tf.word_wrap = True
    add_bullet(tf, "Преодоление энтропии:", "мир со временем изнашивается и рискует сползти в первозданный хаос.", lead_color=COLOR_GREEN_TEXT, bullet_icon="⏳")
    add_bullet(tf, "Перезапуск космоса:", "ритуал заново воссоздаёт порядок, циклически воспроизводя дела богов.", lead_color=COLOR_GREEN_TEXT, bullet_icon="🔄")
    add_bullet(tf, "Жизнеобеспечение:", "гарантирует смену времён года, плодородие земли и единство племени.", lead_color=COLOR_GREEN_TEXT, bullet_icon="🌱")

    add_card(s11, Inches(6.9), Inches(1.8), Inches(5.6), Inches(4.15), title="ТАБУ (Категорический запрет)", bg_color=COLOR_RED_BG, border_color=COLOR_RED_BORDER)
    tb = s11.shapes.add_textbox(Inches(7.15), Inches(2.55), Inches(5.1), Inches(3.2))
    tf = tb.text_frame
    tf.word_wrap = True
    add_bullet(tf, "Абсолютный барьер:", "непререкаемый запрет без права на рациональное обсуждение и сомнение.", lead_color=COLOR_RED_TEXT, bullet_icon="🛑")
    add_bullet(tf, "Социальная гигиена:", "защита рода от кровосмешения, внутренней агрессии и осквернения святынь.", lead_color=COLOR_RED_TEXT, bullet_icon="🛡️")
    add_bullet(tf, "Предтеча права:", "древнейший фундамент коллективной безопасности задолго до писаных законов.", lead_color=COLOR_RED_TEXT, bullet_icon="⚖️")

    add_takeaway_box(s11, "Вместе ритуал и табу создавали абсолютную социальную дисциплину и предсказуемость поведения!")

    # ==================== СЛАЙД 12: ПОЧЕМУ НАУКА НЕ ВЫТЕСНИЛА МИФ (СО ЗНАЧКАМИ) ====================
    s12 = prs.slides.add_slide(blank_layout)
    set_slide_background(s12)
    add_header(s12, "Почему наука не заменила миф: структурный разрыв", slide_num=12)

    add_card(s12, Inches(0.8), Inches(1.8), Inches(5.6), Inches(4.15), title="Триумф науки в «Картине мира»")
    tb = s12.shapes.add_textbox(Inches(1.05), Inches(2.55), Inches(5.1), Inches(3.2))
    tf = tb.text_frame
    tf.word_wrap = True
    add_bullet(tf, "Ответ на вопрос «КАК?»:", "исчерпывающее объяснение законов физики, химии и космологии.", bullet_icon="🔬")
    add_bullet(tf, "Технологический триумф:", "расщепление атома, расшифровка генома человека, глобальные цифровые сети.", bullet_icon="💡")
    add_bullet(tf, "Победа в онтологии:", "рациональное знание полностью вытеснило миф из описания материального мира.", bullet_icon="🔭")

    add_card(s12, Inches(6.9), Inches(1.8), Inches(5.6), Inches(4.15), title="Бессилие науки в «Блоке ценностей»", border_color=COLOR_ACCENT)
    tb = s12.shapes.add_textbox(Inches(7.15), Inches(2.55), Inches(5.1), Inches(3.2))
    tf = tb.text_frame
    tf.word_wrap = True
    add_bullet(tf, "Аксиологическая немота:", "наука принципиально молчит о смысле жизни, добре, зле и предназначении человека.", bullet_icon="❓")
    add_bullet(tf, "Нейтральность формул:", "уравнения физики не объясняют, ради чего стоит жить, бороться и созидать.", bullet_icon="📄")
    add_bullet(tf, "Ценностный вакуум:", "кризис светских идеологий породил смысловую пустоту, которую мгновенно занял миф!", bullet_icon="🕳️")

    add_takeaway_box(s12, "Вывод Шрейбера: пока наука молчит о высших смыслах, человек неизбежно будет искать их в мифе!")

    # ==================== СЛАЙД 13: МЕХАНИЗМ АРХАИЗАЦИИ (ИНФОГРАФИЧЕСКАЯ ЦЕПОЧКА) ====================
    s13 = prs.slides.add_slide(blank_layout)
    set_slide_background(s13)
    add_header(s13, "Механизм архаизации: бегство от тревоги", slide_num=13)

    step_w = Inches(2.6)
    step_h = Inches(4.15)
    top_pos = Inches(1.8)

    steps = [
        ("1. Смысловой вакуум", "Крах прежних идеологий и ценностная растерянность человека в сложном обществе.", Inches(0.8)),
        ("2. Экзистенц. тревога", "Неспособность выносить неопределённость и груз постоянных личных сомнений.", Inches(3.8)),
        ("3. Стихийный регресс", "Отказ от сложного анализа и включение древнейших защитных программ психики.", Inches(6.8)),
        ("4. Триумф неомифа", "Возврат к готовым чёрно-белым схемам: спасение от тревоги найдено!", Inches(9.8))
    ]

    for idx, (st_t, st_desc, x_pos) in enumerate(steps):
        is_last = (idx == 3)
        add_card(s13, x_pos, top_pos, step_w, step_h, title=st_t, border_color=(COLOR_ACCENT if is_last else CARD_BORDER))
        tb = s13.shapes.add_textbox(x_pos + Inches(0.2), top_pos + Inches(0.95), step_w - Inches(0.4), Inches(3.0))
        tf = tb.text_frame
        tf.word_wrap = True
        p = tf.paragraphs[0]
        p.text = st_desc
        p.font.size = Pt(16)
        p.font.color.rgb = (COLOR_PRIMARY if is_last else COLOR_TEXT)
        p.font.name = "Arial"
        if is_last:
            p.font.bold = True

        if idx < 3:
            add_arrow(s13, x_pos + step_w + Inches(0.1), top_pos + Inches(1.8), Inches(0.25), Inches(0.35))

    add_takeaway_box(s13, "Миф активизируется не от глупости, а как аварийный психологический предохранитель сознания!")

    # ==================== СЛАЙД 14: НЕОМИФОЛОГИЯ XXI ВЕКА (С КАРТИНКОЙ ЦИФРОВЫХ МЕДИА И ЗНАЧКАМИ) ====================
    s14 = prs.slides.add_slide(blank_layout)
    set_slide_background(s14)
    add_header(s14, "Неомифология вокруг нас: медиа и цифровые сети", slide_num=14)

    if os.path.exists(img_digital):
        s14.shapes.add_picture(img_digital, Inches(0.8), Inches(1.6), Inches(4.8), Inches(5.3))

    items_neo = [
        ("Теории заговора (Новый антропоморфизм)", 
         "Новый антропоморфизм:", 
         "сложные кризисы объясняются тайной злой волей кукловодов. Это прямой аналог первобытного поиска злого шамана!", 
         "🕵️", Inches(1.6)),
        ("Политические демиурги (Культурный герой)", 
         "Культурный герой:", 
         "образ лидера строится не на сухих цифрах, а по архетипу спасителя космоса, побеждающего наступающий мировой хаос.", 
         "👑", Inches(3.4)),
        ("Алгоритмические ритуалы соцсетей", 
         "Цифровые ритуалы:", 
         "лайки, репосты, травля и «культура отмены» — прямые аналоги племенных обрядов сплочения своих и изгнания нарушителей табу.", 
         "📱", Inches(5.2))
    ]

    for title_n, lead_n, text_n, icon_n, y_pos in items_neo:
        add_card(s14, Inches(5.8), y_pos, Inches(6.733), Inches(1.6), title=title_n)
        tb = s14.shapes.add_textbox(Inches(6.05), y_pos + Inches(0.55), Inches(6.3), Inches(0.95))
        tf = tb.text_frame
        tf.word_wrap = True
        add_bullet(tf, lead_n, text_n, font_size=Pt(14), bullet_icon=icon_n)

    # ==================== СЛАЙД 15: РОССИЙСКАЯ ГОСУДАРСТВЕННОСТЬ (СО ЗНАЧКАМИ) ====================
    s15 = prs.slides.add_slide(blank_layout)
    set_slide_background(s15)
    add_header(s15, "Мировоззренческий миф и российская государственность", slide_num=15)

    if os.path.exists(img_statehood):
        s15.shapes.add_picture(img_statehood, Inches(0.8), Inches(1.6), Inches(4.8), Inches(5.3))

    add_card(s15, Inches(5.8), Inches(1.6), Inches(6.733), Inches(2.5), title="Ценностный каркас цивилизации", border_color=COLOR_ACCENT)
    tb = s15.shapes.add_textbox(Inches(6.05), Inches(2.25), Inches(6.3), Inches(1.75))
    tf = tb.text_frame
    tf.word_wrap = True
    add_bullet(tf, "Смысловой фундамент:", "государство держится не только на кодексах и экономике, но и на общих идеалах народа.", bullet_icon="🏛️")
    add_bullet(tf, "Опоры единства:", "историческая память, служение общему благу, соборность и священная память о Великой Победе.", bullet_icon="🇷🇺")

    add_card(s15, Inches(5.8), Inches(4.3), Inches(6.733), Inches(2.6), title="Когнитивный суверенитет России", border_color=COLOR_PRIMARY)
    tb = s15.shapes.add_textbox(Inches(6.05), Inches(4.95), Inches(6.3), Inches(1.85))
    tf = tb.text_frame
    tf.word_wrap = True
    add_bullet(tf, "Уязвимость вакуума:", "утрата мировоззренческого ядра делает общество беззащитным перед внешними манипуляциями.", bullet_icon="⚠️")
    add_bullet(tf, "Стратегический щит:", "защита культурного кода и традиционных духовно-нравственных ориентиров — базис национальной безопасности!", bullet_icon="🛡️")

    # ==================== СЛАЙД 16: ИТОГИ ИССЛЕДОВАНИЯ ====================
    s16 = prs.slides.add_slide(blank_layout)
    set_slide_background(s16)
    add_header(s16, "Концептуальные итоги: почему это важно для нас?", slide_num=16)

    itogi = [
        ("1. Функциональность мировоззрения", "Практическая схема:", 
         "мировоззрение — это практический инструмент и алгоритм принятия решений в условиях дефицита информации."),
        ("2. Психологическая устойчивость", "Снятие тревоги:", 
         "через аналогию, прецедент и тождество знака с вещью миф спасает человека от разрушительных мук выбора."),
        ("3. Фундамент социальной дисциплины", "Охрана порядка:", 
         "ритуал воссоздаёт гармонию против энтропии мира, а табу блокирует гибельные для общества сценарии поведения."),
        ("4. Неустранимость мифа из культуры", "Вечность мифа:", 
         "наука отвечает на вопрос «Как?», но молчит о «Зачем?». Поэтому мифологическое мышление неизбежно возрождается.")
    ]

    for idx, (h_itog, lead_itog, t_itog) in enumerate(itogi):
        y_pos = Inches(1.6 + idx * 1.3)
        add_card(s16, Inches(0.8), y_pos, Inches(11.733), Inches(1.15))
        tb = s16.shapes.add_textbox(Inches(1.1), y_pos + Inches(0.12), Inches(11.1), Inches(0.9))
        tf = tb.text_frame
        tf.word_wrap = True
        p1 = tf.paragraphs[0]
        p1.text = h_itog
        p1.font.size = Pt(16)
        p1.font.bold = True
        p1.font.color.rgb = COLOR_PRIMARY
        p1.font.name = "Georgia"
        
        add_bullet(tf, lead_itog, t_itog, font_size=Pt(14.5), bullet_icon="▸ ")

    # ==================== СЛАЙД 17: ГЛАВНЫЙ ВЫВОД ====================
    s17 = prs.slides.add_slide(blank_layout)
    set_slide_background(s17)
    add_header(s17, "Главный вывод: когнитивный суверенитет личности", slide_num=17)

    add_card(s17, Inches(0.8), Inches(1.7), Inches(11.733), Inches(5.1), title="Чему учит нас работа В. К. Шрейбера?", border_color=COLOR_ACCENT)
    tb = s17.shapes.add_textbox(Inches(1.2), Inches(2.45), Inches(10.9), Inches(4.1))
    tf = tb.text_frame
    tf.word_wrap = True

    add_bullet(tf, "1. Не признак отсталости:", 
               "миф — это естественный базовый режим человеческой психики при кризисе смыслов и ценностных ориентиров.", 
               font_size=Pt(16.5), bullet_icon="", space_after=Pt(14))
    add_bullet(tf, "2. Диагностический инструмент:", 
               "раскладывая любое явление на триаду (Картина мира → Шкала ценностей → Программа действий), мы сразу видим, где и как нами пытаются манипулировать.", 
               font_size=Pt(16.5), bullet_icon="", space_after=Pt(14))
    add_bullet(tf, "3. Когнитивный суверенитет в XXI веке:", 
               "способность сохранять критический разум, понимать скрытые механизмы архаизации и осознанно опираться на созидательные ценности своего народа.", 
               font_size=Pt(16.5), bullet_icon="", space_after=Pt(10))

    # ==================== СЛАЙД 18: ЗАКЛЮЧИТЕЛЬНЫЙ ====================
    s18 = prs.slides.add_slide(blank_layout)
    set_slide_background(s18)

    add_card(s18, Inches(1.5), Inches(1.2), Inches(10.333), Inches(5.2), bg_color=CARD_BG, border_color=COLOR_ACCENT)

    tb = s18.shapes.add_textbox(Inches(1.8), Inches(1.6), Inches(9.733), Inches(4.4))
    tf = tb.text_frame
    tf.word_wrap = True

    p1 = tf.paragraphs[0]
    p1.text = "Спасибо за внимание!"
    p1.font.size = Pt(36)
    p1.font.bold = True
    p1.font.color.rgb = COLOR_PRIMARY
    p1.font.name = "Georgia"
    p1.alignment = PP_ALIGN.CENTER
    p1.space_after = Pt(16)

    p2 = tf.add_paragraph()
    p2.text = "Готов ответить на ваши вопросы и обсудить тему доклада"
    p2.font.size = Pt(20)
    p2.font.color.rgb = COLOR_ACCENT
    p2.font.name = "Georgia"
    p2.alignment = PP_ALIGN.CENTER
    p2.space_after = Pt(28)

    p3 = tf.add_paragraph()
    p3.text = ("Докладчик: Бородин Леонид Сергеевич\n"
               "Группа: БВТ2602  •  Кафедра «Информационные технологии»\n"
               "Дисциплина: Основы российской государственности\n"
               "МТУСИ, Москва, 2026")
    p3.font.size = Pt(16)
    p3.font.color.rgb = COLOR_TEXT
    p3.font.name = "Arial"
    p3.alignment = PP_ALIGN.CENTER

    prs.save(output_path)
    print("18-slide presentation rebuilt successfully at:", output_path)

if __name__ == '__main__':
    build_presentation()
