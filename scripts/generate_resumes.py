from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT, TA_RIGHT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    BaseDocTemplate,
    Frame,
    KeepTogether,
    PageTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
)


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "assets" / "resume"
VERSION = "2.0.0"
COMMIT = "109eb0b"
BLUE = colors.HexColor("#1d4f7a")
LIGHT_BLUE = colors.HexColor("#eaf2f8")
TEXT = colors.HexColor("#1b262c")
MUTED = colors.HexColor("#5f6b73")

pdfmetrics.registerFont(TTFont("Tahoma", r"C:\Windows\Fonts\tahoma.ttf"))
pdfmetrics.registerFont(TTFont("Tahoma-Bold", r"C:\Windows\Fonts\tahomabd.ttf"))
pdfmetrics.registerFontFamily("Tahoma", normal="Tahoma", bold="Tahoma-Bold")


RESUMES = {
    "EN": {
        "headline": "Software Engineer | .NET, C++ & Industrial IoT",
        "location": "Bangkok, Thailand",
        "profile_title": "PROFILE",
        "profile": ".NET full-stack developer with software and hardware backgrounds spanning web and desktop applications, REST APIs, embedded systems, IoT, and industrial protocol integration. Experienced in insurance technology, industrial label printing, RFID solutions, rail signaling simulators, and industrial IoT.",
        "experience_title": "WORK EXPERIENCE",
        "skills_title": "TECHNICAL SKILLS",
        "education_title": "EDUCATION",
        "languages_title": "LANGUAGES",
        "jobs": [
            ("Software Developer - Assistant Manager, Business Analyst", "TBROKER CO., LTD.", "Bangkok, Thailand", "Mar 2025 - May 2026", [
                "Developed and maintained a web application supporting agents' sales operations.",
                "Developed and maintained REST APIs integrated with LINE Chatbot, Core Systems, and other external platforms.",
                "Performed SIT and UAT testing to prevent software malfunctions before release.",
                "Collaborated with an external penetration testing vendor to identify and resolve web application security vulnerabilities.",
                "Planned development time and resources and provided technical support to agents and end users.",
            ]),
            ("Software Developer - Customer Service", "SATO Auto-ID (Thailand) Co., Ltd.", "Samutprakarn, Thailand", "Jan 2024 - Feb 2025", [
                "Developed .NET web applications supporting Label Printing and RFID solutions.",
                "Built AEP applications enabling stand-alone printing on SATO printers.",
                "Delivered tailor-made software, on-site installation, and remote troubleshooting.",
                "Produced user manuals, system diagrams, man-day estimates, and wireframe demos.",
            ]),
            ("Engineer - Research & Development (Hardware IoT)", "D.T.C. Enterprise Public Company Limited", "Samutprakarn, Thailand", "Jul 2023 - Sep 2023", [
                "Evaluated sensors and hardware devices in real-world applications.",
                "Developed embedded firmware and data processing pipelines for IoT deployments.",
                "Prepared datasets for AI model training and built IoT proof-of-concept prototypes.",
            ]),
            ("Engineer - Research and Development", "Contrologic Co., Ltd.", "Bangkok, Thailand", "2020 - Jun 2023", [
                "Designed desktop, web, and mobile applications for internal teams and clients.",
                "Processed sensor and controller data via RS232, RS485, Modbus, and LoRaWAN.",
                "Integrated hardware with existing systems and built POC prototypes.",
                "Produced user manuals, system diagrams, man-day estimates, and budget plans.",
            ]),
        ],
        "skills": [
            ("Frontend", "HTML, CSS3, JavaScript, jQuery, Bootstrap, React"),
            ("Backend", "C# (.NET Framework, .NET Core), C++, Python, Lua, Node.js"),
            ("Database", "Microsoft SQL Server, PostgreSQL, MySQL"),
            ("API & Integration", "RESTful APIs, AEP, RFID systems"),
            ("Embedded / IoT", "Arduino, Raspberry Pi, Node-RED, Linux"),
            ("Industrial protocols", "RS232, RS485, Modbus, LoRaWAN"),
            ("Engineering", "SolidWorks, engineering drawing, basic electronics"),
        ],
        "education": [
            ("Bachelor of Engineering, Mechatronics Engineering", "Mahanakorn University of Technology", "2017 - 2020 | GPA 2.81"),
            ("High Vocational Certificate, Technology Computer Hardware", "Eastern Technological College E-TECH", "2015 - 2017 | GPA 3.58"),
            ("Vocational Certificate, Electronics", "Eastern Technological College E-TECH", "2012 - 2015 | GPA 3.89"),
        ],
        "languages": "Thai: Native | English: TOEIC 850 (2023)",
    },
    "TH": {
        "headline": "วิศวกรซอฟต์แวร์ | .NET, C++ และ Industrial IoT",
        "location": "กรุงเทพมหานคร, ประเทศไทย",
        "profile_title": "ประวัติโดยย่อ",
        "profile": "นักพัฒนา .NET Full-stack ที่มีพื้นฐานทั้งซอฟต์แวร์และฮาร์ดแวร์ ครอบคลุมเว็บและเดสก์ท็อปแอปพลิเคชัน REST API ระบบสมองกลฝังตัว IoT และการเชื่อมต่อโปรโตคอลอุตสาหกรรม มีประสบการณ์ในธุรกิจประกันภัย ระบบพิมพ์ฉลากอุตสาหกรรม RFID ระบบจำลองสัญญาณรถไฟ และ IoT อุตสาหกรรม",
        "experience_title": "ประสบการณ์ทำงาน",
        "skills_title": "ทักษะทางเทคนิค",
        "education_title": "การศึกษา",
        "languages_title": "ภาษา",
        "jobs": [
            ("นักพัฒนาซอฟต์แวร์ - ผู้ช่วยผู้จัดการ, นักวิเคราะห์ธุรกิจ", "TBROKER CO., LTD.", "กรุงเทพมหานคร", "มี.ค. 2568 - พ.ค. 2569", [
                "พัฒนาและดูแลเว็บแอปพลิเคชันเพื่อสนับสนุนงานขายของตัวแทน",
                "พัฒนาและดูแล REST API ที่เชื่อมต่อกับ LINE Chatbot, Core Systems และแพลตฟอร์มภายนอก",
                "ดำเนินการทดสอบ SIT และ UAT เพื่อป้องกันข้อผิดพลาดก่อนเผยแพร่",
                "ประสานงานการทดสอบเจาะระบบเพื่อค้นหาและแก้ไขช่องโหว่ของเว็บแอปพลิเคชัน",
                "วางแผนเวลาและทรัพยากร พร้อมให้การสนับสนุนด้านเทคนิคแก่ตัวแทนและผู้ใช้งาน",
            ]),
            ("นักพัฒนาซอฟต์แวร์ - ฝ่ายบริการลูกค้า", "SATO Auto-ID (Thailand) Co., Ltd.", "สมุทรปราการ", "ม.ค. 2567 - ก.พ. 2568", [
                "พัฒนาเว็บแอปพลิเคชันด้วย .NET เพื่อสนับสนุนระบบพิมพ์ฉลากและ RFID",
                "พัฒนาแอปพลิเคชัน AEP สำหรับการพิมพ์แบบ Stand-alone บนเครื่องพิมพ์ SATO",
                "พัฒนาซอฟต์แวร์เฉพาะ ติดตั้งหน้างาน และแก้ไขปัญหาระยะไกล",
                "จัดทำคู่มือผู้ใช้ แผนภาพระบบ การประเมิน Man-day และ Wireframe Demo",
            ]),
            ("วิศวกรวิจัยและพัฒนา (Hardware IoT)", "D.T.C. Enterprise Public Company Limited", "สมุทรปราการ", "ก.ค. 2566 - ก.ย. 2566", [
                "ประเมินและทดสอบเซนเซอร์และอุปกรณ์ฮาร์ดแวร์ในการใช้งานจริง",
                "พัฒนาเฟิร์มแวร์และกระบวนการประมวลผลข้อมูลสำหรับระบบ IoT",
                "เตรียมชุดข้อมูลสำหรับฝึกโมเดล AI และสร้างต้นแบบ IoT เพื่อพิสูจน์แนวคิด",
            ]),
            ("วิศวกรวิจัยและพัฒนา", "Contrologic Co., Ltd.", "กรุงเทพมหานคร", "พ.ศ. 2563 - มิ.ย. 2566", [
                "ออกแบบเดสก์ท็อป เว็บ และโมบายแอปพลิเคชันสำหรับทีมภายในและลูกค้า",
                "ประมวลผลข้อมูลเซนเซอร์และคอนโทรลเลอร์ผ่าน RS232, RS485, Modbus และ LoRaWAN",
                "เชื่อมต่อฮาร์ดแวร์กับระบบเดิมและสร้างต้นแบบ POC",
                "จัดทำคู่มือผู้ใช้ แผนภาพระบบ การประเมิน Man-day และแผนงบประมาณ",
            ]),
        ],
        "skills": [
            ("Frontend", "HTML, CSS3, JavaScript, jQuery, Bootstrap, React"),
            ("Backend", "C# (.NET Framework, .NET Core), C++, Python, Lua, Node.js"),
            ("ฐานข้อมูล", "Microsoft SQL Server, PostgreSQL, MySQL"),
            ("API และการเชื่อมต่อ", "RESTful APIs, AEP, ระบบ RFID"),
            ("Embedded / IoT", "Arduino, Raspberry Pi, Node-RED, Linux"),
            ("โปรโตคอลอุตสาหกรรม", "RS232, RS485, Modbus, LoRaWAN"),
            ("วิศวกรรม", "SolidWorks, การเขียนแบบวิศวกรรม, อิเล็กทรอนิกส์พื้นฐาน"),
        ],
        "education": [
            ("วิศวกรรมศาสตรบัณฑิต สาขาวิศวกรรมเมคคาทรอนิกส์", "มหาวิทยาลัยเทคโนโลยีมหานคร", "พ.ศ. 2560 - 2563 | GPA 2.81"),
            ("ประกาศนียบัตรวิชาชีพชั้นสูง สาขาเทคโนโลยีคอมพิวเตอร์ฮาร์ดแวร์", "วิทยาลัยเทคโนโลยีภาคตะวันออก (อี.เทค)", "พ.ศ. 2558 - 2560 | GPA 3.58"),
            ("ประกาศนียบัตรวิชาชีพ สาขาอิเล็กทรอนิกส์", "วิทยาลัยเทคโนโลยีภาคตะวันออก (อี.เทค)", "พ.ศ. 2555 - 2558 | GPA 3.89"),
        ],
        "languages": "ภาษาไทย: ภาษาแม่ | ภาษาอังกฤษ: TOEIC 850 (พ.ศ. 2566)",
    },
}


def styles():
    base = getSampleStyleSheet()
    return {
        "name": ParagraphStyle("Name", parent=base["Title"], fontName="Tahoma-Bold", fontSize=23, leading=27, textColor=BLUE, spaceAfter=2),
        "headline": ParagraphStyle("Headline", parent=base["Normal"], fontName="Tahoma", fontSize=10.5, leading=14, textColor=TEXT),
        "contact": ParagraphStyle("Contact", parent=base["Normal"], fontName="Tahoma", fontSize=8.5, leading=11, textColor=MUTED),
        "section": ParagraphStyle("Section", parent=base["Heading2"], fontName="Tahoma-Bold", fontSize=12, leading=15, textColor=BLUE, spaceBefore=7, spaceAfter=5, borderWidth=0, borderPadding=0),
        "body": ParagraphStyle("Body", parent=base["BodyText"], fontName="Tahoma", fontSize=8.6, leading=12.2, textColor=TEXT, wordWrap="CJK", spaceAfter=2),
        "role": ParagraphStyle("Role", parent=base["BodyText"], fontName="Tahoma-Bold", fontSize=9.3, leading=12, textColor=TEXT, wordWrap="CJK"),
        "company": ParagraphStyle("Company", parent=base["BodyText"], fontName="Tahoma-Bold", fontSize=8.7, leading=11, textColor=BLUE, wordWrap="CJK"),
        "meta": ParagraphStyle("Meta", parent=base["BodyText"], fontName="Tahoma", fontSize=8.2, leading=10.5, textColor=MUTED, alignment=TA_RIGHT, wordWrap="CJK"),
        "bullet": ParagraphStyle("Bullet", parent=base["BodyText"], fontName="Tahoma", fontSize=8.2, leading=11.3, textColor=TEXT, leftIndent=10, firstLineIndent=-6, bulletIndent=3, wordWrap="CJK", spaceAfter=1),
        "small": ParagraphStyle("Small", parent=base["BodyText"], fontName="Tahoma", fontSize=7.5, leading=9.5, textColor=MUTED, wordWrap="CJK"),
    }


def section_heading(text, style):
    table = Table([[Paragraph(text, style)]], colWidths=[176 * mm])
    table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), LIGHT_BLUE),
        ("LINEBELOW", (0, 0), (-1, -1), 0.8, BLUE),
        ("LEFTPADDING", (0, 0), (-1, -1), 5),
        ("RIGHTPADDING", (0, 0), (-1, -1), 5),
        ("TOPPADDING", (0, 0), (-1, -1), 3),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
    ]))
    return table


def job_block(job, st):
    role, company, location, dates, bullets = job
    header = Table([
        [Paragraph(role, st["role"]), Paragraph(dates, st["meta"])],
        [Paragraph(company, st["company"]), Paragraph(location, st["meta"])],
    ], colWidths=[126 * mm, 50 * mm])
    header.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 0),
        ("RIGHTPADDING", (0, 0), (-1, -1), 0),
        ("TOPPADDING", (0, 0), (-1, -1), 0),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 1),
    ]))
    content = [header]
    content.extend(Paragraph(item, st["bullet"], bulletText="•") for item in bullets)
    content.append(Spacer(1, 3 * mm))
    return KeepTogether(content)


def build_pdf(language, data):
    st = styles()
    output_path = OUTPUT / f"Korakod-Phongdee-Resume-{language}.pdf"
    doc = BaseDocTemplate(
        str(output_path), pagesize=A4,
        leftMargin=17 * mm, rightMargin=17 * mm,
        topMargin=14 * mm, bottomMargin=15 * mm,
        title=f"Korakod Phongdee Resume ({language})",
        author="Korakod Phongdee",
    )
    frame = Frame(doc.leftMargin, doc.bottomMargin, doc.width, doc.height, id="main")

    def footer(canvas, document):
        canvas.saveState()
        canvas.setStrokeColor(colors.HexColor("#d9e2e8"))
        canvas.line(17 * mm, 11 * mm, 193 * mm, 11 * mm)
        canvas.setFont("Tahoma", 7)
        canvas.setFillColor(MUTED)
        canvas.drawString(17 * mm, 7 * mm, f"Version {VERSION} | Commit {COMMIT}")
        canvas.drawRightString(193 * mm, 7 * mm, f"{document.page}")
        canvas.restoreState()

    doc.addPageTemplates(PageTemplate(id="resume", frames=[frame], onPage=footer))

    story = [
        Paragraph("KORAKOD PHONGDEE (BLACK)", st["name"]),
        Paragraph(data["headline"], st["headline"]),
        Paragraph(f'{data["location"]} | 095-971-8562 | black.bkp@gmail.com', st["contact"]),
        Spacer(1, 4 * mm),
        section_heading(data["profile_title"], st["section"]),
        Spacer(1, 2 * mm),
        Paragraph(data["profile"], st["body"]),
        Spacer(1, 2 * mm),
        section_heading(data["experience_title"], st["section"]),
        Spacer(1, 2 * mm),
    ]
    story.extend(job_block(job, st) for job in data["jobs"])
    story.extend([
        section_heading(data["skills_title"], st["section"]),
        Spacer(1, 2 * mm),
    ])
    for label, value in data["skills"]:
        story.append(Paragraph(f"<b>{label}:</b> {value}", st["body"]))
    story.extend([
        Spacer(1, 2 * mm),
        section_heading(data["education_title"], st["section"]),
        Spacer(1, 2 * mm),
    ])
    for qualification, school, details in data["education"]:
        story.append(KeepTogether([
            Paragraph(f"<b>{qualification}</b>", st["body"]),
            Paragraph(f"{school} | {details}", st["small"]),
            Spacer(1, 2 * mm),
        ]))
    story.extend([
        section_heading(data["languages_title"], st["section"]),
        Spacer(1, 2 * mm),
        Paragraph(data["languages"], st["body"]),
    ])
    doc.build(story)
    return output_path


if __name__ == "__main__":
    OUTPUT.mkdir(parents=True, exist_ok=True)
    for code, resume in RESUMES.items():
        print(build_pdf(code, resume))
