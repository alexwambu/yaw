import docx
import PyPDF2

def parse_script(file):
    if file.name.endswith(".txt"):
        text = file.read().decode()
    elif file.name.endswith(".docx"):
        doc = docx.Document(file)
        text = "\n".join([p.text for p in doc.paragraphs])
    elif file.name.endswith(".pdf"):
        reader = PyPDF2.PdfReader(file)
        text = "\n".join([page.extract_text() for page in reader.pages])
    else:
        return []

    raw_scenes = text.split("Scene")
    scenes = [{"id": i, "text": s.strip()} for i, s in enumerate(raw_scenes) if len(s.strip()) > 10]
    return scenes
