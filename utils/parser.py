import fitz  # PyMuPDF

def extract_text(file, pasted_text):
    if pasted_text:
        return pasted_text.strip()

    if file:
        if file.name.endswith(".pdf"):
            return extract_pdf_text(file)
        elif file.name.endswith(".txt"):
            return file.read().decode("utf-8")
    return ""

def extract_pdf_text(file):
    text = ""
    with fitz.open(stream=file.read(), filetype="pdf") as doc:
        for page in doc:
            text += page.get_text()
    return text
