import fitz  

def extract_text_from_file(file):
    if file.name.endswith(".pdf"):
        return extract_from_pdf(file)
    elif file.name.endswith(".txt"):
        return file.read().decode("utf-8")
    else:
        return ""

def extract_from_pdf(file):
    doc = fitz.open(stream=file.read(), filetype="pdf")
    text = ""
    for page in doc:
        text += page.get_text()
    return text
