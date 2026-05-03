# 📘 AI Exam Paper Generator

An AI-powered system that generates **university-level exam question papers** using modern AI techniques like **RAG (Retrieval-Augmented Generation)** and **Agent-based logic**.

---

## 🚀 Features

- 🧠 Generate exam papers from syllabus input  
- 🎯 Difficulty control (Easy / Medium / Hard)  
- 📝 Automatic marks distribution (2, 5, 10 marks)  
- 🏫 Anna University-style question paper format  
- 📊 Auto total marks calculation  
- 📄 Export as PDF and DOCX  
- 🎨 Modern glassmorphism interface  

---

## 🧠 How It Works

1. **User Input**
   - Subject, syllabus, difficulty, marks pattern  

2. **RAG (Retrieval-Augmented Generation)**
   - Extracts relevant topics using FAISS  

3. **AI Agent**
   - Decides paper structure (sections & marks)

4. **LLM (Groq API)**
   - Generates structured question paper  

5. **Export Tools**
   - Converts output to PDF and DOCX  

---

## 🛠 Tech Stack

- **Frontend:** Streamlit  
- **Backend:** Python  
- **AI Model:** Groq (Llama 3.1)  
- **RAG:** FAISS + SentenceTransformers  
- **PDF:** FPDF  
- **DOCX:** python-docx  

## 📁 Project Structure

```
exam_generator/
├── app.py
├── config.py
│
├── rag/
│   └── rag_engine.py
│
├── agent/
│   └── planner.py
│
├── llm/
│   └── generator.py
│
├── tools/
│   ├── pdf_tool.py
│   └── docx_tool.py
│
├── .env
└── requirements.txt
```
---
## ⚙️ Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/ai-exam-generator.git
cd ai-exam-generator
```

### 2. Create a Virtual Environment
```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Add Your API Key
Create a `.env` file in the root directory:
GROQ_API_KEY=your_api_key_here

### 5. Run the Application
```bash
streamlit run app.py
```

---

## 🎯 Usage

1. Enter **subject** and **syllabus**
2. Select **difficulty level** and **total marks**
3. Provide exam details *(year, time, duration)*
4. Click **Generate Question Paper**
5. **Download** as PDF or DOCX

---

## 🏆 Key Highlights

- 🤖 Combines **RAG + Agent + LLM** for intelligent generation
- 📚 Real-world **education use case**
- 🏗️ Clean and **scalable architecture**
- 🎨 Interactive UI with **modern design**

---

## 🔒 Security Note

- `.env` file is excluded from version control via `.gitignore`
- API keys are never exposed in the codebase

---

## 👩‍💻 Author

**Priyadharshini V**  
Computer Science Engineering Student

---

## ⭐ Future Improvements

- 📊 Question difficulty tuning slider
- 🧠 Save & history of generated papers
- 🌐 Deploy as a web app
- 🔊 Voice-based input
