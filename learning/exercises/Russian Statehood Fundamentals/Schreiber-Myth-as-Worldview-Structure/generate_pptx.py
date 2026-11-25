# -*- coding: utf-8 -*-
import os
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.enum.shapes import MSO_SHAPE

def build_presentation():
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6]

    output_dir = os.path.dirname(os.path.abspath(__file__))
    output_path = os.path.join(output_dir, "Миф_как_мировоззренческая_структура_Шрейбер_презентация.pptx")

    # Палитра академического стиля МТУСИ (Cobalt / Deep Navy / Gold / Slate)
    BG_COLOR = RGBColor(248, 250, 252)          # Мягкий светлый фон
    CARD_BG = RGBColor(255, 255, 255)           # Белая карточка
    CARD_BORDER = RGBColor(226, 232, 240)       # Граница карточки
    COLOR_PRIMARY = RGBColor(26, 43, 76)        # Глубокий темно-синий
    COLOR_ACCENT = RGBColor(194, 138, 38)       # Золотисто-охристый
    COLOR_MUTED = RGBColor(100, 116, 139)       # Серый служебный
    COLOR_TEXT = RGBColor(30, 41, 59)           # Основной темный текст
    COLOR_TAG_BG = RGBColor(238, 242, 255)      # Фоновый цвет плашки
    COLOR_TAG_TEXT = RGBColor(67, 56, 202)      # Текст плашки

    def set_slide_background(slide):
        bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height)
        bg.fill.solid()
        bg.fill.fore_color.rgb = BG_COLOR
        bg.line.fill.background()

    def add_header(slide, title, category="ОСНОВЫ РОССИЙСКОЙ ГОСУДАРСТВЕННОСТИ • МТУСИ • В. К. ШРЕЙБЕР", slide_num=None):
        cat_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.4), Inches(10.5), Inches(0.3))
        ctf = cat_box.text_frame
        ctf.word_wrap = True
        ctf.margin_left = ctf.margin_top = ctf.margin_right = ctf.margin_bottom = 0
        p_c = ctf.paragraphs[0]
        p_c.text = category.upper()
        p_c.font.size = Pt(10)
        p_c.font.bold = True
        p_c.font.color.rgb = COLOR_ACCENT
        p_c.font.name = "Arial"

        title_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.7), Inches(10.8), Inches(0.65))
        ttf = title_box.text_frame
        ttf.word_wrap = True
        ttf.margin_left = ttf.margin_top = ttf.margin_right = ttf.margin_bottom = 0
        p_t = ttf.paragraphs[0]
        p_t.text = title
        p_t.font.size = Pt(21)
        p_t.font.bold = True
        p_t.font.color.rgb = COLOR_PRIMARY
        p_t.font.name = "Georgia"

        if slide_num:
            num_box = slide.shapes.add_textbox(Inches(11.8), Inches(0.4), Inches(0.8), Inches(0.4))
            ntf = num_box.text_frame
            p_n = ntf.paragraphs[0]
            p_n.text = f"{slide_num:02d}"
            p_n.font.size = Pt(12)
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
            card.line.width = Pt(1.2)
        else:
            card.line.fill.background()

        if title:
            tb = slide.shapes.add_textbox(left + Inches(0.25), top + Inches(0.2), width - Inches(0.5), Inches(0.4))
            tf = tb.text_frame
            tf.word_wrap = True
            tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0
            p = tf.paragraphs[0]
            p.text = title
            p.font.size = Pt(13)
            p.font.bold = True
            p.font.color.rgb = COLOR_PRIMARY
            p.font.name = "Georgia"
        return card

    # ==================== СЛАЙД 1: ТИТУЛЬНЫЙ ====================
    s1 = prs.slides.add_slide(blank_layout)
    set_slide_background(s1)

    # Декоративная плашка
    top_bar = s1.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), Inches(1.0), Inches(11.733), Inches(0.06))
    top_bar.fill.solid()
    top_bar.fill.fore_color.rgb = COLOR_ACCENT
    top_bar.line.fill.background()

    tb1 = s1.shapes.add_textbox(Inches(0.8), Inches(1.3), Inches(11.733), Inches(4.5))
    tf1 = tb1.text_frame
    tf1.word_wrap = True

    p_univ = tf1.paragraphs[0]
    p_univ.text = "МОСКОВСКИЙ ТЕХНИЧЕСКИЙ УНИВЕРСИТЕТ СВЯЗИ И ИНФОРМАТИКИ\nКАФЕДРА «ИНФОРМАЦИОННЫЕ ТЕХНОЛОГИИ» • ДИСЦИПЛИНА «ОРГ»"
    p_univ.font.size = Pt(11)
    p_univ.font.bold = True
    p_univ.font.color.rgb = COLOR_MUTED
    p_univ.font.name = "Arial"
    p_univ.space_after = Pt(24)

    p_main = tf1.add_paragraph()
    p_main.text = "Миф как мировоззренческая структура"

    p_univ.font.size = Pt(11)
    p_univ.font.bold = True
    p_univ.font.color.rgb = COLOR_MUTED
    p_univ.font.name = "Arial"
    p_univ.space_after = Pt(24)

    p_main = tf1.add_paragraph()
    p_main.text = "Миф как мировоззренческая структура"
    p_main.font.size = Pt(32)
    p_main.font.bold = True
    p_main.font.color.rgb = COLOR_PRIMARY
    p_main.font.name = "Georgia"
    p_main.space_after = Pt(12)

    p_sub = tf1.add_paragraph()
    p_sub.text = "Концепция В. К. Шрейбера: от архаического сознания к принятию решений в XXI веке"
    p_sub.font.size = Pt(16)
    p_sub.font.color.rgb = COLOR_ACCENT
    p_sub.font.name = "Georgia"
    p_sub.space_after = Pt(36)

    p_stud = tf1.add_paragraph()
    p_stud.text = "Выполнил: студент группы БВТ2602  Бородин Леонид Сергеевич\nПроверил: преподаватель кафедры философии"
    p_stud.font.size = Pt(13)
    p_stud.font.color.rgb = COLOR_TEXT
    p_stud.font.name = "Arial"

    # ==================== СЛАЙД 2: ПАРАДОКС XXI ВЕКА ====================
    s2 = prs.slides.add_slide(blank_layout)
    set_slide_background(s2)
    add_header(s2, "Парадокс XXI века: почему наука не победила миф?", slide_num=2)

    add_card(s2, Inches(0.8), Inches(1.7), Inches(5.6), Inches(4.8), title="Ожидания эпохи Просвещения")
    tb2_a = s2.shapes.add_textbox(Inches(1.05), Inches(2.3), Inches(5.1), Inches(4.0))
    tf2_a = tb2_a.text_frame
    tf2_a.word_wrap = True
    p = tf2_a.paragraphs[0]
    p.text = "• Век высоких технологий: нейросети, квантовые вычисления, космос, генная инженерия.\n\n• Предпосылка: победа науки должна была навсегда искоренить суеверия и архаичные предрассудки.\n\n• Человек мыслился как рациональный субъект, действующий на основе фактов и логики."
    p.font.size = Pt(13)
    p.font.color.rgb = COLOR_TEXT
    p.font.name = "Arial"

    add_card(s2, Inches(6.9), Inches(1.7), Inches(5.6), Inches(4.8), title="Реальность постиндустриального мира")
    tb2_b = s2.shapes.add_textbox(Inches(7.15), Inches(2.3), Inches(5.1), Inches(4.0))
    tf2_b = tb2_b.text_frame
    tf2_b.word_wrap = True
    p = tf2_b.paragraphs[0]
    p.text = "• Взрывной рост конспирологии: теории плоской Земли, тайные правительства, «чипирование».\n\n• Расцвет псевдонауки: астрология, таро, марафоны желаний у образованных людей.\n\n• Поведение в кризис: люди мгновенно переключаются на эмоциональные мифы вместо объективного анализа."
    p.font.size = Pt(13)
    p.font.color.rgb = COLOR_TEXT
    p.font.name = "Arial"

    # ==================== СЛАЙД 3: В. К. ШРЕЙБЕР И ЗАМЫСЕЛ СТАТЬИ ====================
    s3 = prs.slides.add_slide(blank_layout)
    set_slide_background(s3)
    add_header(s3, "В. К. Шрейбер: исходный вопрос и замысел исследования", slide_num=3)

    add_card(s3, Inches(0.8), Inches(1.7), Inches(3.6), Inches(4.8), title="Контекст эпохи")
    tb = s3.shapes.add_textbox(Inches(1.05), Inches(2.3), Inches(3.1), Inches(4.0))
    tf = tb.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = "• Распад советской идеологии оставил ценностный вакуум.\n\n• Общество секулярно (в храм ходят не все), но и рациональным не стало.\n\n• Наблюдение Шрейбера: дефицит общей идеи ведёт к архаизации сознания."
    p.font.size = Pt(12)
    p.font.color.rgb = COLOR_TEXT

    add_card(s3, Inches(4.8), Inches(1.7), Inches(3.7), Inches(4.8), title="Традиционный тупик")
    tb = s3.shapes.add_textbox(Inches(5.05), Inches(2.3), Inches(3.2), Inches(4.0))
    tf = tb.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = "• Миф часто сводили к фольклору или сказке о древних богах.\n\n• Границы между религией и мифом размыты.\n\n• Непонятно, почему современные инженеры и юристы верят мифам."
    p.font.size = Pt(12)
    p.font.color.rgb = COLOR_TEXT

    add_card(s3, Inches(8.9), Inches(1.7), Inches(3.6), Inches(4.8), title="Новаторский ход")
    tb = s3.shapes.add_textbox(Inches(9.15), Inches(2.3), Inches(3.1), Inches(4.0))
    tf = tb.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = "• Взглянуть на миф через теорию принятия решений!\n\n• Мировоззрение — это практическая инструкция выбора.\n\n• Миф — это алгоритмическая матрица поступков."
    p.font.size = Pt(12)
    p.font.bold = True
    p.font.color.rgb = COLOR_PRIMARY

    # ==================== СЛАЙД 4: КРИТИКА СОЗЕРЦАТЕЛЬНОСТИ ====================
    s4 = prs.slides.add_slide(blank_layout)
    set_slide_background(s4)
    add_header(s4, "Переосмысление мировоззрения: от созерцания к выбору", slide_num=4)

    add_card(s4, Inches(0.8), Inches(1.7), Inches(5.6), Inches(4.8), title="Школьное / пассивное определение")
    tb = s4.shapes.add_textbox(Inches(1.05), Inches(2.3), Inches(5.1), Inches(4.0))
    tf = tb.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = "«Совокупность взглядов, принципов, оценок и идеалов человека относительно мира и своего места в нём».\n\nВ чём изъян по Шрейберу?\n• Человек выглядит как пассивный зритель в кинотеатре.\n• Оторвано от реального поведения: взгляды есть, а почему человек поступает именно так — не объясняется."
    p.font.size = Pt(13)
    p.font.color.rgb = COLOR_TEXT

    add_card(s4, Inches(6.9), Inches(1.7), Inches(5.6), Inches(4.8), title="Определение В. К. Шрейбера")
    tb = s4.shapes.add_textbox(Inches(7.15), Inches(2.3), Inches(5.1), Inches(4.0))
    tf = tb.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = "Мировоззрение — это когнитивно-практическая схема принятия решений.\n\nЗачем человеку мировоззрение?\n• Не ради любования природой, а ради ежедневного выбора в условиях неполной информации.\n• Справляться с рисками, отделять своё от чужого, находить направление в кризисе."
    p.font.size = Pt(13)
    p.font.color.rgb = COLOR_PRIMARY

    # ==================== СЛАЙД 5: АНАТОМИЯ СИТУАЦИИ ВЫБОРА ====================
    s5 = prs.slides.add_slide(blank_layout)
    set_slide_background(s5)
    add_header(s5, "Анатомия ситуации принятия решения", slide_num=5)

    add_card(s5, Inches(0.8), Inches(1.8), Inches(3.6), Inches(4.6), title="1. Поле возможностей")
    tb = s5.shapes.add_textbox(Inches(1.05), Inches(2.4), Inches(3.1), Inches(3.8))
    tf = tb.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = "Вопрос: Что мне доступно?\n\n• Объективный веер альтернатив.\n• Условия и границы внешней среды.\n• Понимание законов физики и общества (что возможно, а что нет)."
    p.font.size = Pt(12)
    p.font.color.rgb = COLOR_TEXT

    add_card(s5, Inches(4.8), Inches(1.8), Inches(3.7), Inches(4.6), title="2. Критерии предпочтения")
    tb = s5.shapes.add_textbox(Inches(5.05), Inches(2.4), Inches(3.2), Inches(3.8))
    tf = tb.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = "Вопрос: Что ценнее?\n\n• Шкала приоритетов и идеалов.\n• Отделение «блага» от «зла», «должного» от «постыдного».\n• Фильтр: из 10 возможных путей выбрать один достойный."
    p.font.size = Pt(12)
    p.font.color.rgb = COLOR_TEXT

    add_card(s5, Inches(8.9), Inches(1.8), Inches(3.6), Inches(4.6), title="3. Программа реализации")
    tb = s5.shapes.add_textbox(Inches(9.15), Inches(2.4), Inches(3.1), Inches(3.8))
    tf = tb.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = "Вопрос: Как действовать?\n\n• Конкретные правила, инструкции, шаги.\n• Допустимые и запретные приёмы.\n• Ритуалы, традиции, практические алгоритмы достижения цели."
    p.font.size = Pt(12)
    p.font.color.rgb = COLOR_TEXT

    # ==================== СЛАЙД 6: ТРИАДА ШРЕЙБЕРА ====================
    s6 = prs.slides.add_slide(blank_layout)
    set_slide_background(s6)
    add_header(s6, "Триада мировоззренческой структуры Шрейбера", slide_num=6)

    add_card(s6, Inches(0.8), Inches(1.8), Inches(3.6), Inches(4.6), title="КАРТИНА МИРА\n(Онтологический блок)", border_color=COLOR_PRIMARY)
    tb = s6.shapes.add_textbox(Inches(1.05), Inches(2.6), Inches(3.1), Inches(3.6))
    tf = tb.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = "Отвечает за ситуацию выбора:\nПоле возможностей\n\nМоделирует реальность: объясняет законы природы, происхождение космоса, границы физического мира."
    p.font.size = Pt(12)
    p.font.color.rgb = COLOR_TEXT

    add_card(s6, Inches(4.8), Inches(1.8), Inches(3.7), Inches(4.6), title="ЦЕННОСТИ\n(Аксиологический блок)", border_color=COLOR_ACCENT)
    tb = s6.shapes.add_textbox(Inches(5.05), Inches(2.6), Inches(3.2), Inches(3.6))
    tf = tb.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = "Отвечает за ситуацию выбора:\nКритерии предпочтения\n\nСмысловые доминанты: фильтруют возможные действия, ранжируют цели, задают этические ориентиры."
    p.font.size = Pt(12)
    p.font.color.rgb = COLOR_TEXT

    add_card(s6, Inches(8.9), Inches(1.8), Inches(3.6), Inches(4.6), title="ПРОГРАММЫ ДЕЙСТВИЙ\n(Праксиологический блок)", border_color=COLOR_PRIMARY)
    tb = s6.shapes.add_textbox(Inches(9.15), Inches(2.6), Inches(3.1), Inches(3.6))
    tf = tb.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = "Отвечает за ситуацию выбора:\nАлгоритм исполнения\n\nПрактические сценарии: ритуалы, обычаи, законы, технологии, кодексы чести, табу."
    p.font.size = Pt(12)
    p.font.color.rgb = COLOR_TEXT

    # ==================== СЛАЙД 7: БАЛАНС БЛОКОВ ====================
    s7 = prs.slides.add_slide(blank_layout)
    set_slide_background(s7)
    add_header(s7, "Что происходит при выпадении одного из блоков?", slide_num=7)

    add_card(s7, Inches(0.8), Inches(1.8), Inches(3.6), Inches(4.6), title="Нет картины мира")
    tb = s7.shapes.add_textbox(Inches(1.05), Inches(2.4), Inches(3.1), Inches(3.8))
    tf = tb.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = "Слепота субъекта\n\n• Человек полон идеалов и готов действовать, но не понимает законов реальности.\n• Итог: утопизм, фатальные ошибки, столкновение с непреодолимыми фактами."
    p.font.size = Pt(12)
    p.font.color.rgb = COLOR_TEXT

    add_card(s7, Inches(4.8), Inches(1.8), Inches(3.7), Inches(4.6), title="Нет ценностей")
    tb = s7.shapes.add_textbox(Inches(5.05), Inches(2.4), Inches(3.2), Inches(3.8))
    tf = tb.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = "Паралич выбора\n\n• Субъект видит 100 вариантов и знает, как их реализовать, но не знает зачем.\n• «Буриданов осёл», апатия, депрессия, потеря смысла жизни."
    p.font.size = Pt(12)
    p.font.color.rgb = COLOR_TEXT

    add_card(s7, Inches(8.9), Inches(1.8), Inches(3.6), Inches(4.6), title="Нет программ действий")
    tb = s7.shapes.add_textbox(Inches(9.15), Inches(2.4), Inches(3.1), Inches(3.8))
    tf = tb.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = "Бессилие идеалиста\n\n• Есть понимание мира и великие цели, но нет практических навыков и инструментов.\n• Итог: бесплодные мечтания и неспособность выжить в кризисе."
    p.font.size = Pt(12)
    p.font.color.rgb = COLOR_TEXT

    # ==================== СЛАЙД 8: МИФ: АНАЛОГИЯ ====================
    s8 = prs.slides.add_slide(blank_layout)
    set_slide_background(s8)
    add_header(s8, "Мифологическая картина мира: метод аналогии", slide_num=8)

    add_card(s8, Inches(0.8), Inches(1.7), Inches(5.6), Inches(4.8), title="Как мыслит первобытный человек?")
    tb = s8.shapes.add_textbox(Inches(1.05), Inches(2.3), Inches(5.1), Inches(4.0))
    tf = tb.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = "• Научного понятийного аппарата ещё нет.\n• Скрытые законы физики (атмосферное давление, электромагнетизм) невидимы.\n• Как объяснить незнакомое? Уподобить его знакомому!\n\nФормула мифа: Природа = Социум\nМакрокосм Вселенной устроен в точности как микрокосм родового племени."
    p.font.size = Pt(13)
    p.font.color.rgb = COLOR_TEXT

    add_card(s8, Inches(6.9), Inches(1.7), Inches(5.6), Inches(4.8), title="Аналогия в действии")
    tb = s8.shapes.add_textbox(Inches(7.15), Inches(2.3), Inches(5.1), Inches(4.0))
    tf = tb.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = "• Солнце и Луна — муж и жена, которые поссорились.\n• Звёзды — дети неба.\n• Засуха — дух обиделся на неуважение.\n• Смена времён года — смерть и возрождение божества.\n\nВ мифе нет слепой материи — есть только одушевлённые отношения родства и власти."
    p.font.size = Pt(13)
    p.font.color.rgb = COLOR_TEXT

    # ==================== СЛАЙД 9: АНТРОПОМОРФИЗМ ====================
    s9 = prs.slides.add_slide(blank_layout)
    set_slide_background(s9)
    add_header(s9, "Антропоморфизм: этический космос", slide_num=9)

    add_card(s9, Inches(0.8), Inches(1.8), Inches(3.6), Inches(4.6), title="Природа одушевлена")
    tb = s9.shapes.add_textbox(Inches(1.05), Inches(2.4), Inches(3.1), Inches(3.8))
    tf = tb.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = "Реки, горы, ветер, гроза наделены волей, страстями, хитростью и благосклонностью.\n\nВ мире нет безразличных предметов."
    p.font.size = Pt(12)
    p.font.color.rgb = COLOR_TEXT

    add_card(s9, Inches(4.8), Inches(1.8), Inches(3.7), Inches(4.6), title="Слияние физики и этики")
    tb = s9.shapes.add_textbox(Inches(5.05), Inches(2.4), Inches(3.2), Inches(3.8))
    tf = tb.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = "Стихийные бедствия происходят не случайно.\n\nНаводнение или падёж скота — это прямое наказание за совершённый грех или нарушение табу."
    p.font.size = Pt(12)
    p.font.color.rgb = COLOR_TEXT

    add_card(s9, Inches(8.9), Inches(1.8), Inches(3.6), Inches(4.6), title="Предсказуемость мира")
    tb = s9.shapes.add_textbox(Inches(9.15), Inches(2.4), Inches(3.1), Inches(3.8))
    tf = tb.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = "С природой можно договориться!\n\nЕсли природа — живой субъект, её можно задобрить жертвой, почтительным словом или ритуалом."
    p.font.size = Pt(12)
    p.font.color.rgb = COLOR_TEXT

    # ==================== СЛАЙД 10: СЛИТНОСТЬ СЛОВА И ВЕЩИ ====================
    s10 = prs.slides.add_slide(blank_layout)
    set_slide_background(s10)
    add_header(s10, "Семиотика мифа: слитность знака и объекта", slide_num=10)

    add_card(s10, Inches(0.8), Inches(1.7), Inches(5.6), Inches(4.8), title="Рациональное сознание")
    tb = s10.shapes.add_textbox(Inches(1.05), Inches(2.3), Inches(5.1), Inches(4.0))
    tf = tb.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = "• Знак отделён от вещи: слово «огонь» не обжигает.\n• Метафора — это литературный приём («сердце как камень» — просто поэтическое сравнение).\n• Возможна критика: мы можем подвергать сомнению слова и проверять их фактами."
    p.font.size = Pt(13)
    p.font.color.rgb = COLOR_TEXT

    add_card(s10, Inches(6.9), Inches(1.7), Inches(5.6), Inches(4.8), title="Мифологическое сознание")
    tb = s10.shapes.add_textbox(Inches(7.15), Inches(2.3), Inches(5.1), Inches(4.0))
    tf = tb.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = "• Имя вещи тождественно самой вещи: произнести имя духа — значит призвать его сущность.\n• Буквальность метафоры: солнце — это буквальный глаз первопредка, а не аллегория.\n• Нет сомнений: у человека нет дистанции по отношению к языку, миф — это сама реальность."
    p.font.size = Pt(13)
    p.font.color.rgb = COLOR_PRIMARY

    # ==================== СЛАЙД 11: САКРАЛЬНЫЙ ПРЕЦЕДЕНТ ====================
    s11 = prs.slides.add_slide(blank_layout)
    set_slide_background(s11)
    add_header(s11, "Время мифа: категория сакрального прецедента", slide_num=11)

    add_card(s11, Inches(0.8), Inches(1.7), Inches(5.6), Inches(4.8), title="In illo tempore («Во время о́но»)")
    tb = s11.shapes.add_textbox(Inches(1.05), Inches(2.3), Inches(5.1), Inches(4.0))
    tf = tb.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = "• В мифе время не линейно (прошлое $\\rightarrow$ настоящее $\\rightarrow$ будущее), а циклично.\n\n• Центр Вселенной — точка первотворения, когда боги и культурные герои создавали мир.\n\n• Всё, что произошло тогда — стало образцом навсегда."
    p.font.size = Pt(13)
    p.font.color.rgb = COLOR_TEXT

    add_card(s11, Inches(6.9), Inches(1.7), Inches(5.6), Inches(4.8), title="Прецедент как высшее доказательство")
    tb = s11.shapes.add_textbox(Inches(7.15), Inches(2.3), Inches(5.1), Inches(4.0))
    tf = tb.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = "• Почему нужно охотиться именно так?\n  Ответ: «Так впервые поохотился Первопредок».\n\n• Почему человек смертен?\n  Ответ: «Потому что первочеловек совершил такую ошибку».\n\n• Прецедент не требует логики — он легитимен фактом своего первого свершения."
    p.font.size = Pt(13)
    p.font.color.rgb = COLOR_TEXT

    # ==================== СЛАЙД 12: ОБОСНОВАНИЕ ЦЕННОСТЕЙ ====================
    s12 = prs.slides.add_slide(blank_layout)
    set_slide_background(s12)
    add_header(s12, "Обоснование ценностей: норма без сомнений", slide_num=12)

    add_card(s12, Inches(0.8), Inches(1.8), Inches(3.6), Inches(4.6), title="Философская этика")
    tb = s12.shapes.add_textbox(Inches(1.05), Inches(2.4), Inches(3.1), Inches(3.8))
    tf = tb.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = "• Сомнение и рефлексия.\n• Индивидуальный моральный выбор.\n• Необходимость логического доказательства добродетели."
    p.font.size = Pt(12)
    p.font.color.rgb = COLOR_TEXT

    add_card(s12, Inches(4.8), Inches(1.8), Inches(3.7), Inches(4.6), title="Мифологическая этика")
    tb = s12.shapes.add_textbox(Inches(5.05), Inches(2.4), Inches(3.2), Inches(3.8))
    tf = tb.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = "• Безальтернативность ценностей.\n• Авторитет первопредков: «Так заповедано от начала».\n• Субъективный каприз исключён."
    p.font.size = Pt(12)
    p.font.color.rgb = COLOR_TEXT

    add_card(s12, Inches(8.9), Inches(1.8), Inches(3.6), Inches(4.6), title="Детерминация выбора")
    tb = s12.shapes.add_textbox(Inches(9.15), Inches(2.4), Inches(3.1), Inches(3.8))
    tf = tb.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = "• Отклонение от образца — космическое преступление.\n• Коллективная ответственность рода.\n• Нулевой уровень ценностного релятивизма."
    p.font.size = Pt(12)
    p.font.color.rgb = COLOR_TEXT

    # ==================== СЛАЙД 13: РИТУАЛ ====================
    s13 = prs.slides.add_slide(blank_layout)
    set_slide_background(s13)
    add_header(s13, "Ритуал: как миф становится программой действий", slide_num=13)

    add_card(s13, Inches(0.8), Inches(1.7), Inches(5.6), Inches(4.8), title="Сущность ритуала по Шрейберу")
    tb = s13.shapes.add_textbox(Inches(1.05), Inches(2.3), Inches(5.1), Inches(4.0))
    tf = tb.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = "• Ритуал — это не просто спектакль или память о прошлом.\n\n• Это буквальное повторение жестов первотворения: во время обряда сакральное время оживает здесь и сейчас.\n\n• Цель: восстановить космический порядок и победить энтропию (хаос)."
    p.font.size = Pt(13)
    p.font.color.rgb = COLOR_TEXT

    add_card(s13, Inches(6.9), Inches(1.7), Inches(5.6), Inches(4.8), title="Правила мифологического действия")
    tb = s13.shapes.add_textbox(Inches(7.15), Inches(2.3), Inches(5.1), Inches(4.0))
    tf = tb.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = "1. Строгий канон: ошибся в одном слове или движении — обряд провален, боги разгневаны.\n\n2. Коллективность: действует не отдельный человек, а всё племя как единый организм.\n\n3. Прагматизм: ритуал совершается ради конкретной пользы (урожай, здоровье, победа)."
    p.font.size = Pt(13)
    p.font.color.rgb = COLOR_TEXT

    # ==================== СЛАЙД 14: ТАБУ ====================
    s14 = prs.slides.add_slide(blank_layout)
    set_slide_background(s14)
    add_header(s14, "Табу: древнейшие стоп-краны человечества", slide_num=14)

    add_card(s14, Inches(0.8), Inches(1.8), Inches(3.6), Inches(4.6), title="Абсолютный запрет")
    tb = s14.shapes.add_textbox(Inches(1.05), Inches(2.4), Inches(3.1), Inches(3.8))
    tf = tb.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = "Табу не объясняется логически.\n\nНельзя трогать вождя, входить в священную рощу, нарушать пищевые границы."
    p.font.size = Pt(12)
    p.font.color.rgb = COLOR_TEXT

    add_card(s14, Inches(4.8), Inches(1.8), Inches(3.7), Inches(4.6), title="Автоматизм наказания")
    tb = s14.shapes.add_textbox(Inches(5.05), Inches(2.4), Inches(3.2), Inches(3.8))
    tf = tb.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = "Нарушение табу загрязняет космос скверной.\n\nКара наступает неотвратимо — не только на нарушителя, но и на всё племя."
    p.font.size = Pt(12)
    p.font.color.rgb = COLOR_TEXT

    add_card(s14, Inches(8.9), Inches(1.8), Inches(3.6), Inches(4.6), title="Функция выживания")
    tb = s14.shapes.add_textbox(Inches(9.15), Inches(2.4), Inches(3.1), Inches(3.8))
    tf = tb.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = "Табу защищали род от кровосмешения, ядовитой пищи и внутренних распрей задолго до появления уголовных кодексов."
    p.font.size = Pt(12)
    p.font.color.rgb = COLOR_TEXT

    # ==================== СЛАЙД 15: ПОЧЕМУ НАУКА НЕ УБИЛА МИФ ====================
    s15 = prs.slides.add_slide(blank_layout)
    set_slide_background(s15)
    add_header(s15, "Почему наука бессильна против мифа?", slide_num=15)

    add_card(s15, Inches(0.8), Inches(1.7), Inches(5.6), Inches(4.8), title="Триумф науки в блоке «Картины мира»")
    tb = s15.shapes.add_textbox(Inches(1.05), Inches(2.3), Inches(5.1), Inches(4.0))
    tf = tb.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = "• Наука блестяще объясняет КАК устроен мир.\n• Даёт формулы, уравнения, технологии, медицину, связь.\n• Но наука принципиально аксиологически нейтральна: атомная физика не говорит, хорошо ли создавать бомбу."
    p.font.size = Pt(13)
    p.font.color.rgb = COLOR_TEXT

    add_card(s15, Inches(6.9), Inches(1.7), Inches(5.6), Inches(4.8), title="Провал науки в блоке «Ценностей»")
    tb = s15.shapes.add_textbox(Inches(7.15), Inches(2.3), Inches(5.1), Inches(4.0))
    tf = tb.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = "• Наука молчит о том, ЗАЧЕМ жить, во имя чего умирать и в чём смысл страданий.\n• Пустой блок ценностей не может долго пустовать.\n• Как только рушатся рациональные идеалы, вакуум мгновенно заполняется мифом!"
    p.font.size = Pt(13)
    p.font.color.rgb = COLOR_PRIMARY

    # ==================== СЛАЙД 16: НЕОМИФОЛОГИЯ XXI ВЕКА ====================
    s16 = prs.slides.add_slide(blank_layout)
    set_slide_background(s16)
    add_header(s16, "Неомифология вокруг нас: мифы в эпоху соцсетей", slide_num=16)

    add_card(s16, Inches(0.8), Inches(1.8), Inches(3.6), Inches(4.6), title="Теории заговора")
    tb = s16.shapes.add_textbox(Inches(1.05), Inches(2.4), Inches(3.1), Inches(3.8))
    tf = tb.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = "Современный антропоморфизм:\n\nСложные системные кризисы (инфляция, пандемии) объясняются злой волей персонифицированных злодеев («тайное правительство»). В точности как поиск злого шамана."
    p.font.size = Pt(12)
    p.font.color.rgb = COLOR_TEXT

    add_card(s16, Inches(4.8), Inches(1.8), Inches(3.7), Inches(4.6), title="Политические демиурги")
    tb = s16.shapes.add_textbox(Inches(5.05), Inches(2.4), Inches(3.2), Inches(3.8))
    tf = tb.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = "Культурные герои:\n\nПолитические медиа строят образ лидера не через программы реформ, а через архетип спасителя космоса, бьющегося с чудовищами хаоса."
    p.font.size = Pt(12)
    p.font.color.rgb = COLOR_TEXT

    add_card(s16, Inches(8.9), Inches(1.8), Inches(3.6), Inches(4.6), title="Цифровые ритуалы")
    tb = s16.shapes.add_textbox(Inches(9.15), Inches(2.4), Inches(3.1), Inches(3.8))
    tf = tb.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = "Обряды сети:\n\nЛайки, флешмобы, ритуальное осуждение и «отмена» — современные эквиваленты племенных ритуалов сплочения и наложения табу."
    p.font.size = Pt(12)
    p.font.color.rgb = COLOR_TEXT

    # ==================== СЛАЙД 17: ВЫВОД ====================
    s17 = prs.slides.add_slide(blank_layout)
    set_slide_background(s17)
    add_header(s17, "Главный вывод: зачем нам концепция В. К. Шрейбера?", slide_num=17)

    add_card(s17, Inches(0.8), Inches(1.7), Inches(11.733), Inches(4.8), title="Итог: когнитивный суверенитет личности", border_color=COLOR_ACCENT)
    tb = s17.shapes.add_textbox(Inches(1.1), Inches(2.3), Inches(11.1), Inches(4.0))
    tf = tb.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = "1. Миф — это не признак глупости. Это базовый, бессознательный режим работы человеческого мозга в условиях нехватки ценностей и информации.\n\n2. Концепция Шрейбера даёт диагностический инструмент: разложив любое явление на триаду (Картина мира $\\rightarrow$ Ценности $\\rightarrow$ Программы), мы сразу видим, где нами пытаются манипулировать через готовые прецеденты.\n\n3. Когнитивный суверенитет в XXI веке: способность сохранять критический разум, понимать механизмы архаизации и осознанно формировать свои ценности, а не слепо следовать древним мифологическим программам."
    p.font.size = Pt(14)
    p.font.color.rgb = COLOR_TEXT
    p.font.name = "Georgia"

    prs.save(output_path)
    print("Presentation saved successfully at:", output_path)

build_presentation()
