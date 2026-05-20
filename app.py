from flask import Flask, render_template, request, send_file
from docx import Document
from PyPDF2 import PdfReader
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import cm
import os
import re

# App Setup
app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

LAST_RESULTS = []
LAST_STATS = {}

# Ambiguity Dictionaries
VAGUE_WORDS = [
    "fast", "efficient", "secure", "reliable", "user-friendly",
    "robust", "optimal", "scalable", "flexible", "quick"
]

WEAK_VERBS = ["should", "may", "might", "could", "can", "possibly"]

# Text Extraction
def extract_text(file_path):
    if file_path.endswith(".txt"):
        with open(file_path, encoding="utf-8", errors="ignore") as f:
            return f.read()

    if file_path.endswith(".pdf"):
        reader = PdfReader(file_path)
        return "\n".join(page.extract_text() or "" for page in reader.pages)

    if file_path.endswith(".docx"):
        doc = Document(file_path)
        return "\n".join(p.text for p in doc.paragraphs)

    return ""

def highlight_text(text, vague, weak):
    for w in vague:
        text = re.sub(
            fr"\b({w})\b",
            r"<span class='highlight-ambiguous'>\1</span>",
            text, flags=re.I
        )
    for w in weak:
        text = re.sub(
            fr"\b({w})\b",
            r"<span class='highlight-weak'>\1</span>",
            text, flags=re.I
        )
    return text

# Requirement Analysis
def analyze_requirement(text):
    lower = text.lower()
    vague = [w for w in VAGUE_WORDS if w in lower]
    weak = [w for w in WEAK_VERBS if w in lower]

    if not vague and not weak:
        return {
            "text": text,
            "status": "Clear",
            "severity": "None",
            "category": "Clear",
            "score": 100,
            "explanation": "No vague terms or weak verbs detected."
        }

    count = len(vague) + len(weak)
    severity, score = (
        ("Low", 80) if count == 1 else
        ("Medium", 60) if count == 2 else
        ("High", 40)
    )

    category = (
        "Vague + Weak Verb" if vague and weak else
        "Vague" if vague else
        "Weak Verb"
    )

    explanation = "; ".join(
        [f"Vague term: {v}" for v in vague] +
        [f"Weak verb: {w}" for w in weak]
    )

    return {
        "text": highlight_text(text, vague, weak),
        "status": "Ambiguous",
        "severity": severity,
        "category": category,
        "score": score,
        "explanation": explanation
    }


# Report generator
def header_bar(text):
    table = Table([[text]], colWidths=[16*cm])
    table.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,-1), colors.HexColor("#2c3e50")),
        ("TEXTCOLOR", (0,0), (-1,-1), colors.white),
        ("FONT", (0,0), (-1,-1), "Helvetica-Bold"),
        ("FONTSIZE", (0,0), (-1,-1), 14),
        ("ALIGN", (0,0), (-1,-1), "CENTER"),
        ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
        ("TOPPADDING", (0,0), (-1,-1), 10),
        ("BOTTOMPADDING", (0,0), (-1,-1), 10),
    ]))
    return table

def generate_pdf(results, stats):
    file_path = "verification_report.pdf"

    doc = SimpleDocTemplate(
        file_path,
        pagesize=A4,
        leftMargin=2*cm,
        rightMargin=2*cm,
        topMargin=2*cm,
        bottomMargin=2*cm
    )

    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(
        name="Cell",
        fontSize=9,
        leading=12
    ))

    story = []

    # Title Bar
    story.append(header_bar("Requirement Ambiguity Verification Report"))
    story.append(Spacer(1, 15))

    # Summary Bar
    story.append(header_bar("Summary"))
    story.append(Spacer(1, 8))

    summary_table = Table([
        ["Total Requirements", stats["total"]],
        ["Ambiguous Requirements", stats["ambiguous"]],
        ["Clear Requirements", stats["clear_count"]],
        ["Ambiguity Percentage", f'{stats["percentage"]}%'],
        ["Overall SRS Quality Score", f'{stats["srs_score"]}/100'],
    ], colWidths=[8*cm, 8*cm])

    summary_table.setStyle(TableStyle([
        ("GRID", (0,0), (-1,-1), 0.5, colors.grey),
        ("BACKGROUND", (0,0), (-1,-1), colors.whitesmoke),
        ("FONT", (0,0), (-1,-1), "Helvetica"),
        ("LEFTPADDING", (0,0), (-1,-1), 8),
        ("RIGHTPADDING", (0,0), (-1,-1), 8),
        ("TOPPADDING", (0,0), (-1,-1), 6),
        ("BOTTOMPADDING", (0,0), (-1,-1), 6),
    ]))

    story.append(summary_table)
    story.append(Spacer(1, 20))

    # Details Bar
    story.append(header_bar("Detailed Requirement Analysis"))
    story.append(Spacer(1, 10))

    table_data = [["Requirement", "Status", "Severity", "Score", "Explanation"]]

    for r in results:
        clean_text = re.sub("<.*?>", "", r["text"])
        table_data.append([
            Paragraph(clean_text, styles["Cell"]),
            Paragraph(r["status"], styles["Cell"]),
            Paragraph(r["severity"], styles["Cell"]),
            Paragraph(f'{r["score"]}%', styles["Cell"]),
            Paragraph(r["explanation"], styles["Cell"]),
        ])

    details_table = Table(
        table_data,
        colWidths=[6.5*cm, 2*cm, 2*cm, 1.5*cm, 4*cm],
        repeatRows=1
    )

    details_table.setStyle(TableStyle([
        ("GRID", (0,0), (-1,-1), 0.5, colors.grey),
        ("BACKGROUND", (0,0), (-1,0), colors.HexColor("#34495e")),
        ("TEXTCOLOR", (0,0), (-1,0), colors.white),
        ("FONT", (0,0), (-1,0), "Helvetica-Bold"),
        ("VALIGN", (0,0), (-1,-1), "TOP"),
    ]))

    story.append(details_table)
    doc.build(story)

    return file_path

# App Routes
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/upload", methods=["POST"])
def upload():
    global LAST_RESULTS, LAST_STATS

    file = request.files["srs_file"]
    path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(path)

    text = extract_text(path)
    requirements = [l.strip() for l in text.split("\n") if l.strip()]

    results, score_sum, amb = [], 0, 0
    for r in requirements:
        res = analyze_requirement(r)
        results.append(res)
        score_sum += res["score"]
        if res["status"] == "Ambiguous":
            amb += 1

    total = len(results)
    stats = {
        "total": total,
        "ambiguous": amb,
        "clear_count": total - amb,
        "percentage": round((amb / total) * 100, 2) if total else 0,
        "srs_score": round(score_sum / total, 2) if total else 0
    }

    LAST_RESULTS = results
    LAST_STATS = stats

    return render_template("result.html", results=results, stats=stats)

@app.route("/download_pdf")
def download_pdf():
    pdf = generate_pdf(LAST_RESULTS, LAST_STATS)
    return send_file(pdf, as_attachment=True)

# Main
if __name__ == "__main__":
    app.run(debug=True)
