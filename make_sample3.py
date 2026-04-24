from fpdf import FPDF

def clean(text):
    return text.replace('\u2014', '-').replace('\u2013', '-').replace('\u2018', "'").replace('\u2019', "'")

pdf = FPDF()
pdf.set_margins(15, 15, 15)

pages = [
    ("Chapter 1: Foundations of Digital Marketing", [
        "Digital marketing promotes products through digital channels like search engines, social media, email, and websites. It has transformed how businesses reach customers.",
        "Digital marketing allows precise targeting, real-time analytics, and measurable results. Businesses reach specific audiences based on demographics and online behaviour.",
        "The landscape includes SEO, content marketing, social media, pay-per-click advertising, and email marketing. Each channel serves a different purpose.",
        "A strong digital presence is essential for business success. Consumers research products online before purchasing, making visibility and reputation management critical.",
    ]),
    ("Chapter 2: Social Media and Content Strategy", [
        "Platforms like Instagram, LinkedIn, TikTok, and Facebook offer powerful tools for brand building and customer engagement across different audiences.",
        "Content marketing involves creating valuable, relevant content to attract and retain a target audience. It builds trust, drives traffic, and supports conversions.",
        "A content strategy defines the target audience, key messages, content formats, publishing schedule, and success metrics for consistent results.",
        "Video content is the most engaging format across all digital platforms. Short-form videos and live streams drive higher engagement than text or images.",
    ]),
    ("Chapter 3: Analytics, ROI and Future Trends", [
        "Tools like Google Analytics, Meta Business Suite, and HubSpot let marketers track performance and optimise campaigns in real time.",
        "Return on Investment (ROI) is the key metric for marketing effectiveness. Marketers must connect spending to revenue outcomes to justify budgets.",
        "Personalisation is a core consumer expectation. AI-powered tools enable marketers to deliver tailored experiences at scale for better results.",
        "The future of digital marketing will be driven by AI, voice search, augmented reality, and privacy-first strategies for competitive advantage.",
    ]),
]

pdf.add_page()
pdf.set_font("Helvetica", "B", 20)
pdf.cell(0, 15, "Business and Digital Marketing", new_x="LMARGIN", new_y="NEXT", align="C")
pdf.ln(5)
pdf.set_font("Helvetica", size=12)
pdf.multi_cell(0, 8, "A Professional Learning Guide")

for chapter_title, paragraphs in pages:
    pdf.add_page()
    pdf.set_font("Helvetica", "B", 14)
    pdf.cell(0, 10, clean(chapter_title), new_x="LMARGIN", new_y="NEXT")
    pdf.ln(4)
    pdf.set_font("Helvetica", size=11)
    for para in paragraphs:
        pdf.multi_cell(0, 8, clean(para))
        pdf.ln(4)

pdf.output("sample3.pdf")
print("✅ sample3.pdf created!")
