from fpdf import FPDF

def create_pdf(text):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    for line in text.split("\n"):
        pdf.multi_cell(0, 8, line)

    file_path = "question_paper.pdf"
    pdf.output(file_path)

    return file_path