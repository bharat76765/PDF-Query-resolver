from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
import os

from google.auth import load_credentials_from_file
from langchain_google_genai.chat_models import ChatGoogleGenerativeAI

# Initialize embeddings and LLM
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "gen-lang-client-0633058873-1c78117e2513.json"

embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash")

def create_vector_db(pages):
    db = FAISS.from_documents(pages, embeddings)
    return db

def query_pdf(db, query):
    # Similarity search
    docs = db.similarity_search(query)
    content = "\n".join([doc.page_content for doc in docs])

    qa_prompt = (
        "Use the following pieces of context to answer the user's question. "
        "If you don't know the answer, try out answering but mention a disclaimer that its in your opinion. "
        "----------------"
    )
    input_text = f"{qa_prompt}\nContext:{content}\nUser question:\n{query}"

    result = llm.invoke(input_text)
    return result.content
