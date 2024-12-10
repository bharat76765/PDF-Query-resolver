# **PDF Query Resolver**

This project is a **Streamlit-based application** that allows users to upload PDF documents, process their content, and interact with the text using a **Large Language Model (LLM)**. The application leverages **LangChain**, embeddings, and LLMs to extract information and resolve queries about the uploaded PDFs.

---

## **Features**

- **PDF Upload**: Users can upload one or more PDF files.
- **Content Extraction**: Automatically extracts and processes text from PDFs, even multi-page documents.
- **Query Resolution**: Users can type questions about the content of the PDFs, and the app provides precise answers using LLMs.
- **Contextual Understanding**: Uses embeddings and similarity search to focus on relevant parts of the document for each query.

---

## **Tech Stack**

### **Core Libraries**
- **[LangChain](https://github.com/hwchase17/langchain)**: Framework for integrating LLMs and embeddings.
- **[Streamlit](https://streamlit.io/)**: Interactive user interface for uploading and querying PDFs.
- **[FAISS](https://github.com/facebookresearch/faiss)**: Vector database for similarity searches.
- **[PyPDF2](https://pypi.org/project/PyPDF2/)**: Library for extracting text from PDF files.

### **LLM Provider**
- **OpenAI GPT** or **Google Generative AI (Gemini)**: For natural language understanding and answering user queries.

---

## **Setup and Installation**

### **Prerequisites**
- Python 3.8 or higher.
- API keys for your chosen LLM provider (e.g., OpenAI or Google Generative AI).
- Download credentials json file from your gemenai account and include it as environment file to run code seamlessly
- Basic knowledge of Streamlit and Python.

### **Installation Steps**
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-repo/pdf-query-resolver.git
   cd pdf-query-resolver
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set Up API Keys**:
   - For OpenAI:
     ```bash
     export OPENAI_API_KEY="your-openai-api-key"
     ```
   - For Google Generative AI:
     ```bash
     export GOOGLE_APPLICATION_CREDENTIALS="path/to/your-service-account.json"
     ```

4. **Run the Application**:
   ```bash
   streamlit run app.py
   ```

---

## **Usage Instructions**

1. **Upload PDF**:
   - Use the file uploader in the Streamlit interface to upload one or more PDF documents.

2. **Extract Content**:
   - The app automatically extracts the text from the uploaded PDFs and processes it.

3. **Ask Questions**:
   - Type a question about the content of the uploaded PDFs (e.g., "What are the main topics discussed in this document?").
   - The app provides answers based on the context extracted from the PDFs.

---

## **Project Structure**

```
.
├── app.py                    # Main Streamlit app for user interaction
├── process_pdf.py            # Module for extracting text from PDFs
├── query_llm.py              # Module for handling LLM queries and embedding search
├── requirements.txt          # Dependencies for the project
├── README.md                 # Project documentation
```

---

## **Key Features**

### **PDF Processing**
- Extracts text from PDFs using `PyPDF2`.
- Handles multi-page documents and non-standard formats.

### **Embedding and Vector Search**
- Converts text into embeddings using `HuggingFaceEmbeddings`.
- Stores embeddings in a FAISS vector database for efficient similarity searches.

### **LLM Integration**
- Resolves user queries by combining relevant document content with LLMs.
- Supports multiple LLM providers like OpenAI GPT or Google Gemini.

---

## **Future Enhancements**

- **Summarization**: Add functionality to provide concise summaries of uploaded PDFs.
- **Multi-Language Support**: Enable querying PDFs in multiple languages.
- **Deployment**: Host the app on **Streamlit Cloud** for broader accessibility.


---

## **Contributing**

Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a new branch (`feature/your-feature-name`).
3. Submit a pull request with detailed changes.

---

## **License**

This project is licensed under the MIT License. See the `LICENSE` file for more details.
