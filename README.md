# 🤖 AI-Powered eLearning Course Generator

Automatically converts PDF documents into complete eLearning course storyboards using a local AI model (Ollama). No internet required. No API keys needed.

---

## 📌 What It Does

This tool reads any PDF document and automatically generates:

- **Introduction** — A professional course opening paragraph
- **Learning Objectives** — 5 clear learning goals
- **Content Screens** — Bullet-point learning screens for each section
- **Check Your Understanding (CYU)** — Multiple choice quiz questions
- **Summary** — A closing recap paragraph
- **Excel Storyboard** — A colour-coded professional Excel file
- **PowerPoint Presentation** — A professional slide deck

---

## ✅ Prerequisites

Before running this project, make sure you have the following installed:

| Tool | Purpose | Download |
|------|---------|----------|
| Python 3.x | Run the scripts | https://python.org |
| Ollama | Local AI model | https://ollama.com |
| Llama 3.2 Model | AI language model | Run: `ollama pull llama3.2` |
| Node.js | PowerPoint generation | https://nodejs.org |

---

## 🔧 Install Steps

### 1. Clone or download the project
```bash
cd ~/my_ai_project
```

### 2. Install Python libraries
```bash
pip3 install requests pymupdf openpyxl fpdf2 python-pptx
```

### 3. Install Node.js library
```bash
npm install -g pptxgenjs
```

### 4. Pull the AI model
```bash
ollama pull llama3.2
```

### 5. Start Ollama
```bash
ollama serve
```

---

## ▶️ How to Run

### Run the full pipeline on all 3 sample documents:
```bash
python3 export_excel_pro.py
```

### Generate PowerPoint presentation:
```bash
node export_pptx_pro.js
```

### Run end-to-end test:
```bash
python3 e2e_test.py
```

### Generate storyboard script:
```bash
python3 create_storyboard_script.py
```

---

## 📁 Project Structure
---

## 📊 Sample Output

### Excel Storyboard
Each Excel file contains 3 sheets:
- **Cover** — Document title, metadata and legend
- **Storyboard** — All 9 screens colour-coded by type
- **Summary** — Screen count statistics

### Screen Types & Colours
| Screen Type | Colour |
|-------------|--------|
| 📖 Introduction | Navy Blue |
| 🎯 Objectives | Mid Blue |
| 🖥️ Content Screen | Dark Green |
| ❓ Check Your Understanding | Orange |
| 📝 Summary | Purple |

### PowerPoint Presentation
- 10 professional slides
- Dark navy theme
- Colour-coded slides per screen type
- Quiz slides with highlighted correct answers

---

## 🛠️ Built With

- **Python 3** — Core scripting language
- **Ollama + Llama 3.2** — Local AI model (no internet required)
- **PyMuPDF** — PDF reading
- **OpenPyXL** — Excel file generation
- **Python-PPTX / PptxGenJS** — PowerPoint generation
- **FPDF2** — PDF creation

---

## 👤 Author

**Aslin Mike**
- 🏢 Company: Mediant Labs
- 🛠️ Role: AI Developer Intern
- 📅 Year: 2026

---

## 📸 Sample Output Screenshots

### Excel Storyboard
![Excel Storyboard](screenshots/excel_screenshot.png)

### Pipeline Running
![Pipeline Running](screenshots/Screenshot%202026-04-24%20at%2010.45.52%20AM.png)

### PowerPoint Presentation
![PowerPoint Presentation](screenshots/pptx_screenshot.png)
