from pathlib import Path

from pypdf import PdfReader


DOCS_PATH = Path("docs")


def load_documents():

    documents = []
    print(DOCS_PATH.resolve())
    print(list(DOCS_PATH.glob("*.pdf")))
    for pdf_file in DOCS_PATH.glob("*.pdf"):

        reader = PdfReader(pdf_file)

        text = ""

        for page in reader.pages:
            page_text = page.extract_text()

            if page_text:
                text += page_text + "\n"

        documents.append(
            {
                "filename": pdf_file.name,
                "text": text,
            }
        )

    return documents