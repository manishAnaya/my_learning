import tempfile
import os
import streamlit as st
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_classic.chains.combine_documents import create_stuff_documents_chain
from langchain_classic.chains import create_retrieval_chain
from langchain_core.messages import HumanMessage, AIMessage

# Load environment variables
load_dotenv()

st.title("ChatGroq RAG Chatbot")
st.caption("Upload documents and ask questions about their content.")

model =  ChatGroq(model='openai/gpt-oss-120b')

prompt = ChatPromptTemplate.from_messages([
    ("system",
    """You are a helpful AI assistant.
    Answer using the provided context.
    If the answer is unavailable, say "I don't know."

    Context:
    {context}"""
    ),
    MessagesPlaceholder(variable_name="history"),
    ("human", "{input}")
])


# Initialize session state
if "history" not in st.session_state:
    st.session_state.history = []

# Display previous history
for message in st.session_state.history:
    role = 'user' if isinstance(message, HumanMessage) else 'assistant'
    with st.chat_message(role):
        st.markdown(message.content)

def generate_embeddings():
    if 'vectors' not in st.session_state:
        st.session_state.embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

        # Save the uploaded PDF temporarily and load
        temp_path = None
        try:
            with tempfile.NamedTemporaryFile(suffix=".pdf", delete=False) as temp_file:
                temp_file.write(uploaded_file.getvalue())
                temp_path = temp_file.name

            loader = PyPDFLoader(temp_path)
            st.session_state.docs = loader.load()
        finally:
            # Delete the temporary file after loading
            if temp_path and os.path.exists(temp_path):
                os.remove(temp_path)

        st.session_state.splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
        st.session_state.chunks = st.session_state.splitter.split_documents(documents=st.session_state.docs)
        st.session_state.vectors = FAISS.from_documents(documents=st.session_state.chunks, embedding=st.session_state.embeddings)
        st.write('Vector DB is Ready!!!')

with st.sidebar:
    st.header("Document Settings")

    # Upload PDF or TXT documents
    uploaded_file = st.file_uploader('Upload your document', type=['pdf'])

    if uploaded_file:
        st.success("file uploaded successfully.")

    if st.button("Create Embedding"):
        if not uploaded_file:
            st.warning("Please upload a PDF first.")
        else:
            with st.spinner("Creating embeddings..."):
                generate_embeddings()

user_input = st.chat_input('Ask anything from uploaded doc')

if user_input:
    with st.chat_message('user'):
        st.markdown(user_input)

    if "vectors" not in st.session_state:
        st.warning("Please upload a PDF and click Create Embedding first.")
        st.stop()

    doc_context = create_stuff_documents_chain(model, prompt)
    retriever = st.session_state.vectors.as_retriever()
    retrieved_data = create_retrieval_chain(retriever, doc_context)
    

    with st.chat_message('assistant'):
        with st.spinner('Thinking...'):
            response = retrieved_data.invoke({'input': user_input, 'history': st.session_state.history})
            st.markdown(response['answer'])

    st.session_state.history.append(HumanMessage(content=user_input))
    st.session_state.history.append(AIMessage(content=response['answer']))
    

