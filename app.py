import streamlit as st
from process_pdf import extract_text_from_pdf
from query_llm import create_vector_db, query_pdf

st.title("Assignment1 - PDF Question-Answering App")
st.markdown("Upload a PDF, type your question, and Let AI do the work!")

# File uploader
uploaded_file = st.file_uploader("Upload a PDF file")

if uploaded_file is not None:
    # Save uploaded file temporarily
    with open("temp.pdf", "wb") as f:
        f.write(uploaded_file.getbuffer())

    # Extract text from the PDF
    st.info("Processing PDF...")
    pages = extract_text_from_pdf("temp.pdf")
    st.success("PDF successfully processed!")

    # Create vector database
    st.info("Indexing document...")
    db = create_vector_db(pages)
    st.success("Document indexed!")

    # User input for query

    def query():
        query = st.text_input("Enter your question:")
        if query:
            st.info("Querying the LLM...")
            answer = query_pdf(db, query)
            st.success("Answer generated!")
            st.write(f"**Answer:** {answer}")


    st.button("query", on_click=query())

