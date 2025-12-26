import os
from docx import Document

class DocumentLoader:
    def __init__(self, folder):
        self.folder = folder

    def read_docx(self, path):
        doc = Document(path)
        return " ".join([p.text for p in doc.paragraphs])

    def read_txt(self, path):
        with open(path, "r", encoding="utf-8") as f:
            return f.read()

    def load_documents(self):
        documents = {}
        doc_id = 0
        for file in os.listdir(self.folder):
            if file.startswith("~$"):
                continue
            path = os.path.join(self.folder, file)
            if file.endswith(".txt"):
                text = self.read_txt(path)
            elif file.endswith(".docx"):
                text = self.read_docx(path)
            else:
                continue
            documents[doc_id] = {"name": file, "text": text}
            doc_id += 1
        return documents
