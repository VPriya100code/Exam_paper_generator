from docx import Document

def create_docx(text):
    doc = Document()

    for line in text.split("\n"):
        doc.add_paragraph(line)

    file_path = "question_paper.docx"
    doc.save(file_path)

    return file_path