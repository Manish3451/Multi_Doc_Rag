# Multi-Document RAG Application

## Overview

This project is a **Multi-Document Retrieval-Augmented Generation (RAG) System** built using **Streamlit**, **LangChain**, **OpenAI Embeddings**, and **ChromaDB**.
Users can upload multiple documents (PDF, TXT, or DOCX), enter their own OpenAI API key, and ask questions.
The system retrieves relevant document chunks using vector search and generates answers using OpenAI models.

            ┌───────────────────────────┐
            │       User Query          │
            └────────────┬──────────────┘
                         │
                 (1) Retrieve Context
                         │
          ┌──────────────┴──────────────┐
          │       Vector Database       │
          │        (ChromaDB)           │
          └──────────────┬──────────────┘
                         │
                 (2) Top-k Chunks
                         │
                 (3) Pass to LLM
                         │
          ┌──────────────┴──────────────┐
          │     ChatOpenAI / GPT        │
          └──────────────┬──────────────┘
                         │
                 (4) Final Answer
                         │
                 ┌────────▼────────┐
                 │   Streamlit UI  │
                 └─────────────────┘
```
```
## Project Structure

```
multi-doc-rag/
├── app.py
├── requirements.txt
├── .env (optional)
├── static/
│   └── images/
│       ├── system_architecture.png
│       └── model_architecture.png
└── README.md
```

---

## Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/multi-doc-rag.git
cd multi-doc-rag
```

### 2. Create and Activate Virtual Environment

```bash
python -m venv .rag
source .rag/bin/activate   # On Windows: .rag\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Set up OpenAI API Key

You can set your API key either by:

* Creating a `.env` file in the project root:

  ```bash
  OPENAI_API_KEY=your_openai_api_key_here
  ```
* Or entering it directly in the Streamlit interface.

---

## Run the Application

```bash
streamlit run app.py
```

Then open your browser at:

```
http://localhost:8501
```

Upload your documents, process them, and start asking questions.

---

## How It Works

1. **Document Upload:** Users upload multiple files (PDF, TXT, or DOCX).
2. **Chunking:** Documents are split into smaller overlapping chunks.
3. **Embeddings:** Each chunk is converted into an OpenAI vector embedding.
4. **Vector Storage:** Embeddings are stored in ChromaDB for fast retrieval.
5. **Retrieval + Generation:** When a user asks a question, the app retrieves relevant chunks and uses OpenAI's LLM to generate an answer.

---

## Example Query Flow

**User:** "Summarize all uploaded research papers on machine learning."

**App:** Retrieves top relevant chunks from all uploaded documents and generates a concise summary using OpenAI models.

---

## Requirements

Example `requirements.txt`:

```
streamlit
langchain
langchain-community
langchain-openai
chromadb
python-dotenv
PyPDF2
docx2txt
```

---

## Demo

Add your screenshots or architecture diagrams here:

```
![System Architecture](static/images/system_architecture.png)
![Model Architecture](static/images/model_architecture.png)
```

---

## Future Enhancements

* Add persistent vector storage using hosted Chroma or Pinecone
* Enable multiple LLM model selection in UI
* Add conversation history and memory
* Enhance visualization for embeddings and context retrieval

---

## Contributing

Contributions are welcome.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/new-feature`)
3. Commit your changes
4. Push to your branch
5. Open a Pull Request

---

## License

This project is licensed under the **MIT License**.

---

## Acknowledgements

* [LangChain](https://www.langchain.com/)
* [OpenAI](https://platform.openai.com/)
* [ChromaDB](https://www.trychroma.com/)
* [Streamlit](https://streamlit.io/)

---

*Efficient multi-document understanding through retrieval-augmented generation.*
