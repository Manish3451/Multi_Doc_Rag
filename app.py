import streamlit as st
from core.rag_core import process_documents_and_create_retriever, query_rag
import os

# Set OpenAI API key from Streamlit secrets
try:
    os.environ["OPENAI_API_KEY"] = st.secrets["OPENAI_API_KEY"]
except KeyError:
    st.error("OPENAI_API_KEY not found. Please set it in your Streamlit secrets.")
    st.stop()

# --- Streamlit App Layout ---

st.set_page_config(page_title="Multi-Doc RAG Assistant", layout="wide")
st.title("📄 Multi-Document RAG Assistant")

# Use session state to store the retriever
if 'retriever' not in st.session_state:
    st.session_state.retriever = None

# Sidebar for document uploads
with st.sidebar:
    st.header("Upload Your Documents")
    uploaded_files = st.file_uploader(
        "Upload PDF files", 
        type=["pdf"], 
        accept_multiple_files=True,
        help="Upload one or more PDF documents to chat with."
    )
    
    process_button = st.button("Process Documents")

    if process_button and uploaded_files:
        with st.spinner("Processing documents... This might take a moment."):
            try:
                # Cache the retriever creation process
                @st.cache_resource
                def create_retriever_cached(_uploaded_files):
                    return process_documents_and_create_retriever(_uploaded_files)

                st.session_state.retriever = create_retriever_cached(uploaded_files)
                st.success("Documents processed successfully!")
            except Exception as e:
                st.error(f"An error occurred during document processing: {e}")
    
    if st.session_state.retriever:
        st.success("Documents are ready to be queried.")

# Main chat interface
st.header("Ask a Question")

if st.session_state.retriever is None:
    st.warning("Please upload and process documents in the sidebar to begin.")
else:
    user_query = st.text_input("What would you like to know about your documents?")

    if user_query:
        with st.spinner("Searching for answers..."):
            try:
                answer = query_rag(st.session_state.retriever, user_query)
                st.write("### Answer")
                st.write(answer)
            except Exception as e:
                st.error(f"An error occurred while fetching the answer: {e}")