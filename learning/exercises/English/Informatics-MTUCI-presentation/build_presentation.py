import os
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.enum.shapes import MSO_SHAPE
from PIL import Image

def generate_presentation():
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6]

    base_dir = r"c:\Users\borod\OneDrive\Рабочий стол\МТУСИ\ОК&ВМ\learning-os-template\learning\exercises\English\Informatics-MTUCI-presentation"
    assets_dir = os.path.join(base_dir, "assets")
    output_path = os.path.join(base_dir, "Informatics_at_MTUCI.pptx")

    COLOR_BG = RGBColor(11, 19, 38)          # Slate Navy
    COLOR_CARD_BG = RGBColor(21, 32, 54)     # Slate 900 Card
    COLOR_CARD_BORDER = RGBColor(45, 62, 95) # Card Border
    COLOR_CYAN = RGBColor(56, 189, 248)      # Tech Cyan
    COLOR_TEAL = RGBColor(45, 212, 191)      # Vibrant Teal
    COLOR_GOLD = RGBColor(251, 191, 36)      # Amber Accent
    COLOR_TEXT_MAIN = RGBColor(241, 245, 249)# Pure Off-White
    COLOR_TEXT_MUTED = RGBColor(148, 163, 184) # Muted Slate
    COLOR_BADGE_BG = RGBColor(30, 58, 95)   # Subdued Badge Blue

    def set_slide_background(slide):
        bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height)
        bg.fill.solid()
        bg.fill.fore_color.rgb = COLOR_BG
        bg.line.fill.background()

    def add_header(slide, title_text, category_text="MTUCI • INFORMATICS & COMPUTER SCIENCE"):
        cat_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.4), Inches(11.7), Inches(0.35))
        tf_c = cat_box.text_frame
        tf_c.word_wrap = True
        tf_c.margin_left = tf_c.margin_top = tf_c.margin_right = tf_c.margin_bottom = 0
        p_c = tf_c.paragraphs[0]
        p_c.text = category_text.upper()
        p_c.font.size = Pt(11)
        p_c.font.bold = True
        p_c.font.color.rgb = COLOR_CYAN
        p_c.font.name = "Segoe UI"

        title_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.75), Inches(11.7), Inches(0.75))
        tf_t = title_box.text_frame
        tf_t.word_wrap = True
        tf_t.margin_left = tf_t.margin_top = tf_t.margin_right = tf_t.margin_bottom = 0
        p_t = tf_t.paragraphs[0]
        p_t.text = title_text
        p_t.font.size = Pt(24)
        p_t.font.bold = True
        p_t.font.color.rgb = COLOR_TEXT_MAIN
        p_t.font.name = "Segoe UI"

        divider = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), Inches(1.5), Inches(11.733), Inches(0.02))
        divider.fill.solid()
        divider.fill.fore_color.rgb = COLOR_CARD_BORDER
        divider.line.fill.background()

    def add_card(slide, left, top, width, height, title, items, badge=""):
        card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
        card.fill.solid()
        card.fill.fore_color.rgb = COLOR_CARD_BG
        card.line.color.rgb = COLOR_CARD_BORDER
        card.line.width = Pt(1.5)

        tb = slide.shapes.add_textbox(left + Inches(0.35), top + Inches(0.3), width - Inches(0.7), height - Inches(0.6))
        tf = tb.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0

        p_title = tf.paragraphs[0]
        p_title.text = title
        p_title.font.size = Pt(17)
        p_title.font.bold = True
        p_title.font.color.rgb = COLOR_CYAN if not badge else COLOR_TEAL
        p_title.font.name = "Segoe UI"
        p_title.space_after = Pt(12)

        for item in items:
            p = tf.add_paragraph()
            p.text = "• " + item
            p.font.size = Pt(13)
            p.font.color.rgb = COLOR_TEXT_MAIN
            p.font.name = "Segoe UI"
            p.space_after = Pt(8)

    def add_image_card(slide, filename, left, top, width, height, title="", caption=""):
        card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
        card.fill.solid()
        card.fill.fore_color.rgb = COLOR_CARD_BG
        card.line.color.rgb = COLOR_CARD_BORDER
        card.line.width = Pt(1.5)

        cur_top = top + Inches(0.25)
        card_content_w = width - Inches(0.5)

        if title:
            tb = slide.shapes.add_textbox(left + Inches(0.25), cur_top, card_content_w, Inches(0.35))
            tf = tb.text_frame
            tf.word_wrap = True
            tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0
            p = tf.paragraphs[0]
            p.text = title
            p.font.size = Pt(15)
            p.font.bold = True
            p.font.color.rgb = COLOR_GOLD
            p.font.name = "Segoe UI"
            cur_top += Inches(0.4)

        img_full_path = os.path.join(assets_dir, filename)
        if os.path.exists(img_full_path):
            with Image.open(img_full_path) as im:
                iw, ih = im.size
            aspect = iw / ih

            avail_w = card_content_w
            avail_h = (height - (cur_top - top)) - (Inches(0.65) if caption else Inches(0.25))

            target_w = avail_w
            target_h = target_w / aspect

            if target_h > avail_h:
                target_h = avail_h
                target_w = target_h * aspect

            img_left = left + (width - target_w) / 2
            img_top = cur_top + (avail_h - target_h) / 2

            frame = slide.shapes.add_shape(
                MSO_SHAPE.RECTANGLE, img_left - Inches(0.03), img_top - Inches(0.03),
                target_w + Inches(0.06), target_h + Inches(0.06)
            )
            frame.fill.background()
            frame.line.color.rgb = COLOR_CARD_BORDER
            frame.line.width = Pt(1.2)

            slide.shapes.add_picture(img_full_path, img_left, img_top, width=target_w, height=target_h)
            cur_top += avail_h

        if caption:
            cap_box = slide.shapes.add_textbox(left + Inches(0.25), top + height - Inches(0.55), card_content_w, Inches(0.45))
            ctf = cap_box.text_frame
            ctf.word_wrap = True
            ctf.margin_left = ctf.margin_top = ctf.margin_right = ctf.margin_bottom = 0
            p = ctf.paragraphs[0]
            p.alignment = PP_ALIGN.CENTER
            p.text = caption
            p.font.size = Pt(10)
            p.font.italic = True
            p.font.color.rgb = COLOR_TEXT_MUTED
            p.font.name = "Segoe UI"

    # ==================== SLIDE 1 ====================
    s1 = prs.slides.add_slide(blank_layout)
    set_slide_background(s1)

    top_badge = s1.shapes.add_textbox(Inches(1.0), Inches(0.9), Inches(11.333), Inches(0.4))
    tf1 = top_badge.text_frame
    p1 = tf1.paragraphs[0]
    p1.text = "MOSCOW TECHNICAL UNIVERSITY OF COMMUNICATIONS AND INFORMATICS (MTUCI)"
    p1.font.size = Pt(12)
    p1.font.bold = True
    p1.font.color.rgb = COLOR_CYAN
    p1.font.name = "Segoe UI"

    title_box = s1.shapes.add_textbox(Inches(1.0), Inches(1.3), Inches(11.333), Inches(1.3))
    tf_main = title_box.text_frame
    p_main = tf_main.paragraphs[0]
    p_main.text = "Informatics & Computer Science at MTUCI"
    p_main.font.size = Pt(36)
    p_main.font.bold = True
    p_main.font.color.rgb = COLOR_TEXT_MAIN
    p_main.font.name = "Segoe UI"

    sub_box = s1.shapes.add_textbox(Inches(1.0), Inches(2.5), Inches(11.333), Inches(0.5))
    tf_sub = sub_box.text_frame
    p_sub = tf_sub.paragraphs[0]
    p_sub.text = "Academic Studies, Modern Laboratories & Key Innovations"
    p_sub.font.size = Pt(16)
    p_sub.font.color.rgb = COLOR_TEAL
    p_sub.font.name = "Segoe UI"

    add_image_card(s1, "prev_Главное_здание_МТУСИ.jpg", Inches(1.0), Inches(3.2), Inches(7.5), Inches(3.6),
                   title="MTUCI Main Campus",
                   caption="Authentic view of MTUCI main building on Aviamotornaya Street")

    add_card(s1, Inches(8.8), Inches(3.2), Inches(3.533), Inches(3.6),
             "Key Facts",
             [
                 "Founded in 1921",
                 "Over 11,000 students enrolled",
                 "1,000+ IT graduates annually",
                 "1,500+ budget places",
                 "Employment rate: 85% – 97%"
             ],
             badge="INFO")

    s1.notes_slide.notes_text_frame.text = (
        "Good afternoon! Today's presentation focuses on Informatics and Computer Science at MTUCI. "
        "Founded in 1921, the university has become one of Russia's leading centers in telecommunications and IT, "
        "educating over 11,000 students across multiple technical faculties."
    )

    # ==================== SLIDE 2 ====================
    s2 = prs.slides.add_slide(blank_layout)
    set_slide_background(s2)
    add_header(s2, "Faculty of Information Technologies: Studies & Curriculum", "1. ACADEMIC STRUCTURE • STUDIES AT MTUCI")

    add_card(s2, Inches(0.8), Inches(1.8), Inches(6.0), Inches(5.0),
             "Academic Program & Core Disciplines",
             [
                 "Core disciplines: Software development, discrete mathematics, and algorithms.",
                 "Professional focus: Mechanics, electronics, programming, and data science.",
                 "Admission scale: More than 1,500 state-funded budget places annually.",
                 "Employment statistics: Official 85% to 97% employment rate for graduates in their field.",
                 "Teaching staff: Highly qualified professors, associate professors, and industry specialists."
             ])

    add_image_card(s2, "redsoft_1.jpg", Inches(7.1), Inches(1.8), Inches(5.433), Inches(5.0),
                   title="Computer Laboratory at MTUCI",
                   caption="Students working at desktop computer workstations inside MTUCI IT lab")

    s2.notes_slide.notes_text_frame.text = (
        "The Faculty of Information Technologies provides comprehensive training in software engineering, programming, and algorithms. "
        "The university offers more than 1,500 state-funded budget places each year, and official reports show that between 85 and 97 percent of graduates secure employment directly in their field."
    )

    # ==================== SLIDE 3 ====================
    s3 = prs.slides.add_slide(blank_layout)
    set_slide_background(s3)
    add_header(s3, "Laboratory Infrastructure & Technical Facilities", "2. EDUCATIONAL FACILITIES • HARDWARE & LABS")

    add_card(s3, Inches(0.8), Inches(1.8), Inches(6.0), Inches(5.0),
             "Specialized Educational Centers",
             [
                 "Academic Computer Center: Computational clusters supporting student research.",
                 "Cyber Test Site (Киберполигон): Specialized facility for cybersecurity training.",
                 "Quantum Center: Advanced laboratory exploring quantum communications and cryptography.",
                 "Advanced technology centers: Modern facilities spanning tens of thousands of square meters.",
                 "Equipment: Industrial-grade servers, network public exchanges, and testing grounds."
             ])

    add_image_card(s3, "prev_lab_12309_0.jpg", Inches(7.1), Inches(1.8), Inches(5.433), Inches(5.0),
                   title="Quantum Center & Optical Racks at MTUCI",
                   caption="Actual MTUCI quantum communications research setup and fiber-optic test racks")

    s3.notes_slide.notes_text_frame.text = (
        "The academic structure comprises modern research facilities spanning tens of thousands of square meters. "
        "Key centers include the Academic Computer Center, the Cyber Test Site, and the Quantum Center. "
        "As demonstrated at the Russian Quantum Communications Forum, MTUCI researchers actively develop high-speed quantum key distribution over multi-core optical fibers."
    )

    # ==================== SLIDE 4 ====================
    s4 = prs.slides.add_slide(blank_layout)
    set_slide_background(s4)
    add_header(s4, "Notable Achievement: The P-Vision Software", "3. SCIENTIFIC RESEARCH • APPLIED INNOVATION")

    add_card(s4, Inches(0.8), Inches(1.8), Inches(6.0), Inches(5.0),
             "Intelligent Streaming Data Monitoring",
             [
                 "Key university project: The P-Vision software system, highlighted in lesson materials.",
                 "Core purpose: Intelligent streaming data monitoring and real-time video analytics.",
                 "Applied research: Part of MTUCI’s secured systems development for extended objects.",
                 "Object detection: Automated recognition of safety gear, personnel, and access events.",
                 "Practical value: Real-time object tracking and anomaly detection in streaming video."
             ])

    add_image_card(s4, "p_vision_clean.png", Inches(7.1), Inches(1.8), Inches(5.433), Inches(5.0),
                   title="P-Vision: Video Analytics at MTUCI",
                   caption="Real-time object and safety gear detection at MTUCI entrance turnstiles")

    s4.notes_slide.notes_text_frame.text = (
        "Among notable applied research projects highlighted in our study materials is the P-Vision software system. "
        "Developed for intelligent streaming data monitoring and real-time computer vision, it automatically detects personnel, safety equipment, and access events at university entry points. "
        "This project demonstrates MTUCI’s practical focus on secured systems for critical infrastructure."
    )

    # ==================== SLIDE 5 ====================
    s5 = prs.slides.add_slide(blank_layout)
    set_slide_background(s5)
    add_header(s5, "Industry Partnerships & Career Prospects", "4. CAREER PROSPECTS • CORPORATE COOPERATION")

    add_card(s5, Inches(0.8), Inches(1.8), Inches(6.0), Inches(5.0),
             "Corporate Collaboration & Practical Experience",
             [
                 "Industry partners: Established ties with Kaspersky Lab, Yandex, VK, and Infotecs.",
                 "Hands-on experience: Practical projects, student hackathons, and corporate workshops.",
                 "Probation & theses: Opportunities to defend practical diploma theses with industry partners.",
                 "Workforce readiness: Prepares graduates for careers in IT, robotics, and the digital economy."
             ])

    add_image_card(s5, "prev_lab_12882_0.jpg", Inches(7.1), Inches(1.8), Inches(5.433), Inches(5.0),
                   title="Cyber Craft & IT Hackathon in MTUCI Hall",
                   caption="Student developer teams solving practical corporate challenges inside MTUCI")

    s5.notes_slide.notes_text_frame.text = (
        "Furthermore, MTUCI maintains strategic partnerships with major technology companies like Kaspersky Lab, Yandex, and VK. "
        "These partnerships provide students with corporate hackathons, specialized workshops, and opportunities to complete probation for a degree."
    )

    # ==================== SLIDE 6 ====================
    s6 = prs.slides.add_slide(blank_layout)
    set_slide_background(s6)
    add_header(s6, "Summary: Informatics at MTUCI", "5. CONCLUSION • RETELLING HIGHLIGHTS")

    card_w = Inches(3.644)
    gap = Inches(0.399)

    add_card(s6, Inches(0.8), Inches(1.8), card_w, Inches(4.2),
             "1. Academic Studies",
             [
                 "Rigorous curriculum",
                 "Algorithms & software",
                 "1,500+ budget places",
                 "85% - 97% employment"
             ])

    add_card(s6, Inches(0.8) + card_w + gap, Inches(1.8), card_w, Inches(4.2),
             "2. Laboratory Base",
             [
                 "Computer center clusters",
                 "Cyber test polygon",
                 "Quantum technologies",
                 "Industrial server racks"
             ])

    add_card(s6, Inches(0.8) + (card_w + gap) * 2, Inches(1.8), card_w, Inches(4.2),
             "3. Real Innovations",
             [
                 "P-Vision software R&D",
                 "Secured telemetry",
                 "Kaspersky & Yandex ties",
                 "Industry-ready skills"
             ])

    foot_card = s6.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(6.2), Inches(11.733), Inches(0.8))
    foot_card.fill.solid()
    foot_card.fill.fore_color.rgb = COLOR_BADGE_BG
    foot_card.line.color.rgb = COLOR_CYAN
    foot_card.line.width = Pt(1.0)

    tb_foot = s6.shapes.add_textbox(Inches(1.0), Inches(6.3), Inches(11.333), Inches(0.6))
    tf_foot = tb_foot.text_frame
    p_foot = tf_foot.paragraphs[0]
    p_foot.alignment = PP_ALIGN.CENTER
    p_foot.text = "Thank you for your attention! | Ready for your questions."
    p_foot.font.size = Pt(16)
    p_foot.font.bold = True
    p_foot.font.color.rgb = COLOR_TEXT_MAIN
    p_foot.font.name = "Segoe UI"

    s6.notes_slide.notes_text_frame.text = (
        "In conclusion, the Informatics track at MTUCI combines solid academic theory, specialized laboratory equipment, and strong industry connections. "
        "Thank you for your attention, and I am glad to answer your questions!"
    )
    p_foot.font.name = "Segoe UI"

    prs.save(output_path)
    print(f"Presentation updated with 100% authentic MTUCI photos at: {output_path}")

if __name__ == "__main__":
    generate_presentation()
