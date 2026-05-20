# 🚀 Requirement Ambiguity Detection and Verification System

A Software Verification and Validation (SV&V) project that automatically detects ambiguity in Software Requirement Specification (SRS) documents using rule-based Natural Language Processing (NLP).

---

# 📌 Project Overview

Requirement ambiguity is one of the major causes of software failure.  
Ambiguous requirements can lead to:

- Misinterpretation
- Incorrect implementation
- Increased development cost
- Project delays

This project helps identify ambiguous requirements automatically and generates professional verification reports.

---

# 🎯 Objectives

- Detect ambiguous requirements automatically
- Identify vague words and weak verbs
- Classify ambiguity severity
- Generate SRS quality score
- Produce downloadable PDF verification reports
- Validate system behavior using Selenium automation

---

# ✨ Features

## ✅ Core Features
- Upload SRS documents
- Support for:
  - TXT
  - PDF
  - DOCX
- Requirement extraction
- Ambiguity detection
- Weak verb detection
- Highlight ambiguous terms

---

## 🔥 Advanced Features
- Severity classification
  - Low
  - Medium
  - High
- Confidence scoring
- Overall SRS Quality Score
- Interactive dashboard
- Enhanced PDF report generation
- Selenium automated testing

---

# 🧠 Technologies Used

| Technology | Purpose |
|------------|---------|
| Python | Core programming |
| Flask | Web framework |
| Selenium | Automation testing |
| ReportLab | PDF generation |
| PyPDF2 | PDF text extraction |
| python-docx | DOCX extraction |
| HTML/CSS | Frontend UI |

---

# 🏗️ System Architecture

```text
User
   ↓
Flask Web Interface
   ↓
File Upload Module
   ↓
Text Extraction Engine
   ↓
Requirement Parsing
   ↓
Ambiguity Detection Engine
   ↓
Severity & Scoring
   ↓
Dashboard + PDF Report
```

---

# ⚙️ Working Flow

1. User uploads SRS document
2. System extracts text
3. Requirements are parsed
4. Ambiguous words are detected
5. Severity and scores are assigned
6. Dashboard results are displayed
7. PDF verification report is generated

---

# 📂 Project Structure

```text
requirement_ambiguity_system/
│
├── app.py
├── requirements.txt
├── README.md
├── chromedriver.exe
│
├── templates/
│   ├── index.html
│   └── result.html
│
├── tests/
│   └── test_upload.py
│
├── uploads/
│
└── static/
```

---

# ▶️ How to Run the Project

## 1️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 2️⃣ Run Flask Application

```bash
python app.py
```

Open browser:

```text
http://127.0.0.1:5000
```

---

# 🧪 Selenium Automated Testing

Run:

```bash
python tests/test_upload.py srs_document.pdf
```

This automatically:
- Opens browser
- Uploads file
- Validates dashboard
- Confirms successful analysis

---

# 📊 Example Output

The system provides:

- Total requirements
- Ambiguous requirements
- Clear requirements
- Ambiguity percentage
- Overall SRS quality score
- Severity classification
- Downloadable PDF report

---

# 📘 SDLC Model Used

## Incremental SDLC Model

The project was developed incrementally in modules:

1. File Upload Module
2. Text Extraction Module
3. Ambiguity Detection Module
4. Severity & Scoring Module
5. Reporting Module
6. Selenium Validation Module

Each module was independently developed, tested, and integrated.

---

# 🔍 Why This Project Is Unique

- Focuses on **verification**, not just detection
- Uses explainable rule-based NLP
- Includes severity and quality scoring
- End-to-end automation
- Generates professional reports
- Aligns strongly with SV&V concepts

---

# 🧠 Is This Text Mining?

Partially uses NLP concepts, but this project primarily focuses on:

- Requirement Engineering
- Software Verification & Validation
- Rule-based Requirement Analysis

rather than statistical text mining.

---

# 📌 Future Enhancements

- AI-based requirement rewriting
- Section-wise SRS quality analysis
- Advanced NLP integration
- Cloud deployment
- Multi-user support

---

# 👨‍💻 Developed By

- Adithyan P R

# 📜 License

This project is developed for academic and educational purposes.

---

# ⭐ GitHub Repository

If you like this project, consider giving it a ⭐ on GitHub.
