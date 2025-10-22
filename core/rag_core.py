import os
import streamlit as st
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain.chains import RetrievalQA
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader
import tempfile

def process_documents_and_create_retriever(uploaded_files):
    """
    Processes uploaded PDF files, splits them into chunks, creates embeddings,
    and sets up a retriever for querying.

    This function is designed to be cached by Streamlit to avoid reprocessing
    on every interaction.
    """
    temp_dir = tempfile.mkdtemp()
    documents = []
    for uploaded_file in uploaded_files:
        temp_file_path = os.path.join(temp_dir, uploaded_file.name)
        with open(temp_file_path, "wb") as f:
            f.write(uploaded_file.getvalue())
        
        loader = PyPDFLoader(temp_file_path)
        documents.extend(loader.load())

    # 1. Split documents into chunks
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    chunked_documents = text_splitter.split_documents(documents)

    # 2. Create embeddings and store in ChromaDB
    # The persistent directory will be created in the temp_dir
    vectordb = Chroma.from_documents(
        documents=chunked_documents, 
        embedding=OpenAIEmbeddings(),
        persist_directory=os.path.join(temp_dir, "chroma_db")
    )
    
    # 3. Create a retriever
    retriever = vectordb.as_retriever(search_kwargs={"k": 3})

    return retriever

def query_rag(retriever, query):
    """
    Queries the RAG pipeline with a user's question.
    """
    if not query:
        return ""

    # Create the RAG chain
    qa_chain = RetrievalQA.from_chain_type(
        llm=ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0),
        chain_type="stuff",
        retriever=retriever,
        return_source_documents=True,
    )
    
    # Invoke the chain and get the result
    result = qa_chain.invoke({"query": query})
    
    return result["result"]