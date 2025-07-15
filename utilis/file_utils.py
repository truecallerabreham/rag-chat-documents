import fitz  # PyMuPDF

def extract_text(filepath):
    if filepath.endswith(".pdf"):
        doc = fitz.open(filepath)
        text = ""
        for page in doc:
            text += page.get_text()
        return text
    else:
        with open(filepath, "r", encoding="utf-8") as f:
            return f.read()
