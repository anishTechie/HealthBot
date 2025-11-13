import streamlit as st
from PyPDF2 import PdfReader
import google.generativeai as genai
import os

# --- IMPORTS (Stable "Golden Set" Versions ke liye) ---
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains.question_answering import load_qa_chain
from langchain.prompts import PromptTemplate

# --- 1. CONFIGURATION ---
# API KEY YAHAN DALEIN
os.environ["GOOGLE_API_KEY"] = " "
genai.configure(api_key=os.environ["GOOGLE_API_KEY"])

# --- 2. PAGE SETUP ---
st.set_page_config(page_title="MediBot", page_icon="🩺", layout="wide")

# --- 3. CSS STYLING ---
st.markdown("""
<style>
    .stApp { background-color: #000000; }
    .stChatMessage { padding: 10px; border-radius: 15px; }
    h1 { color: #0f4c75; }
    .stButton button { background-color: #0f4c75; color: white; }
</style>
""", unsafe_allow_html=True)

# --- 4. LOGIC FUNCTIONS (RAG) ---
@st.cache_resource
def get_pdf_text(pdf_docs):
    text = ""
    for pdf in pdf_docs:
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text

@st.cache_resource
def get_text_chunks(text):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=10000, chunk_overlap=1000)
    chunks = text_splitter.split_text(text)
    return chunks

def get_vector_store(text_chunks):
    try:
        embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
        vector_store = FAISS.from_texts(text_chunks, embedding=embeddings)
        vector_store.save_local("faiss_index")
        return True
    except Exception as e:
        st.error(f"Error creating vector store: {e}")
        return False

def get_rag_chain():
    prompt_template = """
    Answer the question as detailed as possible from the provided context only.
    Context: \n{context}?\n
    Question: \n{question}\n
    Answer:
    """
    model = ChatGoogleGenerativeAI(model="gemini-2.0-flash", temperature=0.3)
    prompt = PromptTemplate(template=prompt_template, input_variables=["context", "question"])
    chain = load_qa_chain(model, chain_type="stuff", prompt=prompt)
    return chain

def user_input_rag(user_question):
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    new_db = FAISS.load_local("faiss_index", embeddings, allow_dangerous_deserialization=True)
    docs = new_db.similarity_search(user_question)
    chain = get_rag_chain()
    response = chain({"input_documents": docs, "question": user_question}, return_only_outputs=True)
    return response["output_text"]

# --- 5. LOGIC FUNCTIONS (General AI) ---
def get_general_chat_session():
    system_instruction = """
    You are MediBot, a compassionate and knowledgeable healthcare AI assistant.
    Your goals are:
    1. To provide general health information and wellness tips.
    2. To suggest home remedies for minor issues (like headache, cold).
    3. To ALWAYS advise visiting a doctor for serious symptoms or accurate diagnosis.
    4. Keep your answers concise, empathetic, and easy to understand.
    5. Do NOT answer non-medical questions.
    """
    model = genai.GenerativeModel(
        "gemini-2.0-flash", 
        system_instruction=system_instruction
    )
    return model.start_chat(history=[])

# --- 6. SIDEBAR ---
with st.sidebar:
    st.title("🏥 Health Hub")
    pdf_docs = st.file_uploader("Upload PDFs (Optional)", accept_multiple_files=True, type=['pdf'])
    if st.button("Submit & Process"):
        if pdf_docs:
            with st.spinner("Processing PDF..."):
                raw_text = get_pdf_text(pdf_docs)
                text_chunks = get_text_chunks(raw_text)
                success = get_vector_store(text_chunks)
                if success:
                    st.success("✅ PDF Processed! Ask now.")
                    st.session_state.processed = True
        else:
            st.warning("Please upload a PDF first.")

# --- 7. MAIN CHAT ---
st.title("🩺 MediBot Health Assistant")
st.caption("💡 Tip: Chat for general advice, or upload a PDF for specific analysis.")

# Initialize session state variables
if "messages" not in st.session_state:
    st.session_state.messages = []
if "processed" not in st.session_state:
    st.session_state.processed = False
if "general_chat_session" not in st.session_state:
    st.session_state.general_chat_session = get_general_chat_session()

# Display Chat History
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User Input
if prompt := st.chat_input("Ask your question..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Decide which mode to use (RAG or General)
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response_text = ""
            
            # --- RAG MODE (PDF Uploaded) ---
            if st.session_state.processed:
                try:
                    response_text = user_input_rag(prompt)
                except Exception as e:
                    response_text = f"Error reading from PDF: {e}"
            
            # --- GENERAL AI MODE (No PDF) ---
            else:
                try:
                    response = st.session_state.general_chat_session.send_message(prompt)
                    response_text = response.text
                except Exception as e:
                    response_text = f"Error communicating with AI: {e}"
            
            st.markdown(response_text)
            st.session_state.messages.append({"role": "assistant", "content": response_text})