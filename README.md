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

---

## 📁 Project Structure


exam_generator/
│
├── app.py
├── config.py
│
├── rag/
│ └── rag_engine.py
│
├── agent/
│ └── planner.py
│
├── llm/
│ └── generator.py
│
├── tools/
│ ├── pdf_tool.py
│ └── docx_tool.py
│
├── .env
└── requirements.txt


---

## ⚙️ Installation & Setup

### 1. Clone repository

```bash
git clone https://github.com/yourusername/ai-exam-generator.git
cd ai-exam-generator

2. Create virtual environment
python -m venv venv
venv\Scripts\activate   # Windows

3. Install dependencies
pip install -r requirements.txt

4. Add API Key
Create a .env file:

GROQ_API_KEY=your_api_key_here

5. Run application
streamlit run app.py

🎯 Usage

Enter subject and syllabus
Select difficulty and marks
Provide exam details (year, time, duration)
Click Generate Question Paper
Download as PDF or DOCX

🏆 Key Highlights
Combines RAG + Agent + LLM
Real-world education use case
Clean and scalable architecture
Interactive UI with modern design

🔒 Security Note
.env file is excluded from GitHub
API keys are kept secure

👩‍💻 Author

Priyadharshini V
Computer Science Engineering Student

⭐ Future Improvements

📊 Question difficulty tuning slider
🧠 Save & history of generated papers
🌐 Deploy as web app
🔊 Voice-based input