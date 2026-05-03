import streamlit as st
from config import get_client
from rag.rag_engine import build_rag, retrieve_context
from agent.planner import agent_plan
from llm.generator import generate_paper
from tools.pdf_tool import create_pdf
from tools.docx_tool import create_docx

# ---------- PAGE ----------
st.set_page_config(
    page_title="AI Exam Paper Generator Agent",
    page_icon="📜",
    layout="wide"
)

# ---------- THEME-AWARE CSS ----------
st.markdown("""
<style>

/* Base layout */
.block-container {
    padding-top: 2rem;
}

/* Titles */
h1 {
    text-align: center;
    font-weight: 700;
}

/* Labels (always visible) */
label {
    font-weight: 500 !important;
}

/* ---------- LIGHT MODE ---------- */
@media (prefers-color-scheme: light) {

    .stApp {
        background: linear-gradient(135deg, #f8fafc, #e2e8f0);
        color: #0f172a;
    }

    .section-card {
        background: rgba(255,255,255,0.8);
        backdrop-filter: blur(10px);
        border-radius: 12px;
        padding: 20px;
    }

    .stTextInput input,
    .stTextArea textarea {
        background-color: #ffffff !important;
        color: #0f172a !important;
        border: 1px solid #cbd5e1 !important;
    }

    input::placeholder,
    textarea::placeholder {
        color: #64748b !important;
    }

    .output-box {
        background: #ffffff;
        color: #0f172a;
        border: 1px solid #cbd5e1;
    }
}

/* ---------- DARK MODE ---------- */
@media (prefers-color-scheme: dark) {

    .stApp {
        background: linear-gradient(135deg, #0f172a, #1e293b);
        color: #ffffff;
    }

    .section-card {
        background: rgba(255,255,255,0.05);
        backdrop-filter: blur(12px);
        border-radius: 12px;
        padding: 20px;
    }

    .stTextInput input,
    .stTextArea textarea {
        background-color: #020617 !important;
        color: #ffffff !important;
        border: 1px solid #38bdf8 !important;
    }

    input::placeholder,
    textarea::placeholder {
        color: #94a3b8 !important;
    }

    .output-box {
        background: rgba(2,6,23,0.9);
        color: white;
        border: 1px solid #38bdf8;
    }
}

/* ---------- COMMON ---------- */

/* Button */
.stButton > button {
    background: linear-gradient(90deg, #38bdf8, #0ea5e9);
    color: black;
    border-radius: 12px;
    font-weight: 600;
    height: 3em;
    width: 100%;
}

/* Output box */
.output-box {
    border-radius: 12px;
    padding: 20px;
    white-space: pre-wrap;
}

</style>
""", unsafe_allow_html=True)

# ---------- HEADER ----------
st.markdown("<h1>📘 AI Exam Paper Generator</h1>", unsafe_allow_html=True)

# ---------- INPUT CARD ----------
with st.container():
    st.markdown("<div class='section-card'>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        subject = st.text_input("📚 Subject", placeholder="Enter subject (e.g. DBMS)")

    with col2:
        difficulty = st.selectbox("🎯 Difficulty", ["Easy", "Medium", "Hard"])

    units = st.text_area(
        "🧠 Enter Syllabus (one per line)",
        placeholder="SQL\nNormalization\nTransactions"
    )

    marks = st.multiselect("📝 Marks Distribution", [2, 5, 10], default=[2,5,10])

    col3, col4, col5 = st.columns(3)

    with col3:
        year = st.text_input("📅 Year", placeholder="2026")

    with col4:
        time = st.text_input("⏰ Time", placeholder="10:00 AM")

    with col5:
        duration = st.text_input("⌛ Duration", placeholder="3 Hours")

    st.markdown("</div>", unsafe_allow_html=True)

# ---------- GENERATE ----------
if st.button("🚀 Generate Question Paper"):

    if not subject or not units or not year or not time or not duration:
        st.warning("⚠ Please fill all fields")
    else:
        with st.spinner("Generating AI Paper..."):

            client = get_client()

            index, docs = build_rag(units)
            context = retrieve_context(index, docs)

            plan = agent_plan(marks)

            # TOTAL MARKS
            total_marks = 0
            for k, v in plan.items():
                if "2" in k:
                    total_marks += v * 2
                elif "5" in k:
                    total_marks += v * 5
                elif "10" in k:
                    total_marks += v * 10

            paper = generate_paper(
                client,
                subject,
                context,
                difficulty,
                plan,
                year,
                time,
                duration
            )

            paper = f"TOTAL MARKS: {total_marks}\n\n" + paper

            st.success("✅ Paper Generated!")

            # OUTPUT CARD
            st.markdown("<div class='section-card'>", unsafe_allow_html=True)
            st.markdown(f"<div class='output-box'>{paper}</div>", unsafe_allow_html=True)
            st.markdown("</div>", unsafe_allow_html=True)

            # DOWNLOADS
            pdf_path = create_pdf(paper)
            docx_path = create_docx(paper)

            colA, colB = st.columns(2)

            with colA:
                with open(pdf_path, "rb") as f:
                    st.download_button("📥 Download PDF", f, file_name="Exam_Paper.pdf")

            with colB:
                with open(docx_path, "rb") as f:
                    st.download_button("📄 Download DOCX", f, file_name="Exam_Paper.docx")