# Requirement Ambiguity Detection and Verification System

<div align="center">

![Python](https://img.shields.io/badge/Python-3.9+-blue?style=for-the-badge&logo=python)
![Flask](https://img.shields.io/badge/Flask-Web%20Application-black?style=for-the-badge&logo=flask)
![NLP](https://img.shields.io/badge/NLP-Requirement%20Analysis-purple?style=for-the-badge)
![SV&V](https://img.shields.io/badge/Domain-SV%26V-green?style=for-the-badge)
![Automation](https://img.shields.io/badge/Selenium-Test%20Automation-orange?style=for-the-badge)

### 🧠 Intelligent Software Requirement Verification using Rule-Based NLP

*A Software Verification & Validation (SV&V) system that automatically detects ambiguity in Software Requirement Specification (SRS) documents.*

</div>

---

# 🌌 Overview

Requirement ambiguity is one of the leading causes of software project failure.

Poorly written requirements can introduce:

- ❌ Misinterpretation
- ⚠️ Incorrect implementation
- 💸 Increased development cost
- 🕒 Project delays
- 🔁 Rework during SDLC phases

This project introduces an intelligent **Requirement Ambiguity Detection & Verification System** that automatically analyzes Software Requirement Specification (SRS) documents using rule-based Natural Language Processing (NLP).

The platform detects:
- Ambiguous statements
- Weak verbs
- Vague terminology
- Requirement quality issues

and generates professional verification reports with severity analysis and quality scoring.

---

# 🎯 Project Objectives

## 🔹 Primary Goals

✅ Automatically detect ambiguous requirements  
✅ Identify vague words and weak verbs  
✅ Classify ambiguity severity  
✅ Generate SRS quality score  
✅ Produce downloadable PDF verification reports  
✅ Validate system behavior using Selenium automation  

---

# 🚀 Features

---

# ✅ Core Features

- 📄 Upload SRS documents
- 📚 Multi-format support:
  - TXT
  - PDF
  - DOCX
- 🧠 Requirement extraction
- 🔍 Ambiguity detection
- ⚠️ Weak verb identification
- ✨ Highlight ambiguous terms

---

# 🔥 Advanced Features

## 📊 Severity Classification
Requirements are classified as:
- 🟢 Low
- 🟡 Medium
- 🔴 High

---

## 📈 Confidence Scoring
Each detected ambiguity receives:
- Detection confidence
- Severity intensity
- Validation metrics

---

## 🏆 SRS Quality Score
The platform computes an overall software requirement quality index based on:
- Requirement clarity
- Ambiguity density
- Weak terminology usage
- Requirement consistency

---

## 📑 Professional PDF Reports
Generates downloadable:
- Requirement verification reports
- Ambiguity summaries
- Severity analysis sheets
- SRS quality metrics

---

## 🤖 Selenium Automation Testing
Automated browser testing validates:
- File uploads
- Dashboard rendering
- End-to-end workflow behavior

---

# 🧠 Technologies Used

<div align="center">

| Technology | Purpose |
|---|---|
| 🐍 Python | Core Programming |
| 🌐 Flask | Web Application Framework |
| 🤖 Selenium | Automated Testing |
| 📄 ReportLab | PDF Report Generation |
| 📘 PyPDF2 | PDF Text Extraction |
| 📝 python-docx | DOCX Parsing |
| 🎨 HTML/CSS | Frontend Interface |

</div>

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

## 🪜 Step-by-Step Process

### 1️⃣ Document Upload
User uploads an SRS document.

### 2️⃣ Text Extraction
The system extracts textual content from:
- PDF
- DOCX
- TXT

### 3️⃣ Requirement Parsing
Requirements are segmented and processed individually.

### 4️⃣ Ambiguity Detection
The NLP engine detects:
- Weak verbs
- Vague terminology
- Ambiguous phrases

### 5️⃣ Severity Classification
Requirements are scored based on ambiguity intensity.

### 6️⃣ Dashboard Visualization
Interactive analytics are displayed to the user.

### 7️⃣ PDF Verification Report
Professional verification reports are generated automatically.

---

# 🧬 Project Structure

```bash
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

---

# 1️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 2️⃣ Run Flask Application

```bash
python app.py
```

---

# 3️⃣ Open Browser

```text
http://127.0.0.1:5000
```

---

# 🧪 Selenium Automated Testing

Run automated validation using:

```bash
python tests/test_upload.py srs_document.pdf
```

---

# 🤖 Selenium Automatically Performs

✅ Browser launch  
✅ File upload validation  
✅ Dashboard verification  
✅ Workflow testing  
✅ End-to-end analysis confirmation  

---

# 📊 Example System Output

The platform generates:

- 📄 Total requirements
- ⚠️ Ambiguous requirements
- ✅ Clear requirements
- 📈 Ambiguity percentage
- 🏆 Overall SRS quality score
- 🔥 Severity classification
- 📑 Downloadable PDF verification reports

---

# 📘 SDLC Model Used

## 🔄 Incremental SDLC Model

The project was developed incrementally through modular phases:

1. File Upload Module
2. Text Extraction Module
3. Requirement Parsing Module
4. Ambiguity Detection Engine
5. Severity & Scoring Engine
6. Reporting System
7. Selenium Validation Module

Each module was:
- Independently designed
- Tested separately
- Integrated progressively

---

# 🔍 Why This Project Is Unique

Unlike traditional text-analysis projects, this system focuses heavily on:

✅ Software Verification & Validation (SV&V)  
✅ Requirement Engineering principles  
✅ Explainable rule-based NLP  
✅ Quality scoring mechanisms  
✅ End-to-end automated verification  
✅ Professional report generation  

---

# 🧠 NLP & Requirement Engineering

This project partially incorporates NLP concepts, but primarily emphasizes:

- 📘 Requirement Engineering
- 🧪 Software Verification & Validation
- 🔍 Rule-Based Requirement Analysis

rather than large-scale statistical text mining.

---

# 📈 System Capabilities

| Capability | Status |
|---|---|
| PDF Requirement Parsing | ✅ |
| DOCX Parsing | ✅ |
| TXT Support | ✅ |
| Ambiguity Detection | ✅ |
| Severity Classification | ✅ |
| Quality Scoring | ✅ |
| PDF Report Generation | ✅ |
| Selenium Validation | ✅ |

---

# 🌍 Real-World Applications

This project can be extended for:

- 📄 SRS quality auditing
- 🏢 Software quality assurance systems
- 🧪 Requirement verification pipelines
- 🤖 Intelligent requirement review tools
- 📊 SDLC quality analytics
- 🧠 AI-assisted requirement engineering
- 🛡️ Enterprise software validation systems

---

# 🔭 Future Enhancements

## Planned Extensions

- AI-based requirement rewriting
- Deep NLP integration
- Transformer-based ambiguity detection
- Section-wise SRS quality analysis
- Multi-user cloud deployment
- Real-time collaborative review systems
- Requirement recommendation engine

---

# 🎓 Intended Use

This project is ideal for:

- Software engineering students
- SV&V coursework
- Final-year engineering projects
- Research internships
- NLP beginners
- Requirement engineering studies
- Academic GitHub portfolios

---

# 📄 License

This project is developed for:

- Academic use
- Educational purposes
- Research experimentation
- Portfolio development

Feel free to:
- Fork 🍴
- Modify 🛠️
- Extend 🚀
- Experiment 🧠

---

# 👨‍💻 Author

<div align="center">

## Made with ❤️ by Adithyan P R

📧 **Email:** adithyanprupasana@gmail.com  

🔗 **LinkedIn:**  
[Adithyan P R](https://www.linkedin.com/in/adithyan-p-r-36b79a250)

</div>

---

# 🙌 Acknowledgement

Developed as a Software Verification & Validation (SV&V) project combining:

- Requirement Engineering
- Rule-Based NLP
- Automated Verification
- Selenium Testing
- Quality Scoring Systems

Designed to improve software requirement clarity and reduce ambiguity during early SDLC phases.

---

<div align="center">

# 🚀 From Ambiguous Requirements → Verified Software Specifications

### *Where requirement engineering meets intelligent verification.*

</div>

---

# ⭐ GitHub Support

If you found this project useful:

⭐ Star the repository  
🍴 Fork the project  
📢 Share it with others  

</div>
