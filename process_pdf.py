from langchain_community.document_loaders import PyPDFLoader

def extract_text_from_pdf(file_path):
    """Extracts text from a PDF file."""
    loader = PyPDFLoader(file_path)
    pages = loader.load_and_split()
    return pages
