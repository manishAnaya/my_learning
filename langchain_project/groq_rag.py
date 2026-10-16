from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain_groq import ChatGroq
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_classic.chains.combine_documents import create_stuff_documents_chain
from langchain_classic.chains import create_retrieval_chain
from langchain_core.prompts import ChatPromptTemplate
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

model =  ChatGroq(model='openai/gpt-oss-120b')

prompt = ChatPromptTemplate.from_template('''
    You are an helpful AI Assistant.
    Please provide the most accurate result from the context below only.
    If its out of the context just say I dont know

    Context:
    {context}

    Question: {input}
    ''')

def generate_embeddings():
    if 'vectors' not in st.session_state:
        st.session_state.embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
        st.session_state.loader = PyPDFDirectoryLoader('data')
        st.session_state.docs = st.session_state.loader.load()
        st.session_state.splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
        st.session_state.chunks = st.session_state.splitter.split_documents(documents=st.session_state.docs)
        st.session_state.vectors = FAISS.from_documents(documents=st.session_state.chunks, embedding=st.session_state.embeddings)
        st.write('Vector DB is Ready!!!')

st.title('Groq LPU Chatbot')

st.write('Please Click below to add embedding of your personal data')

if st.button('Create Embedding'):
    with st.spinner('creating ebeddings'):
        generate_embeddings()



user_input = st.text_input('Ask anything from doc')

if st.button('Send'):
    if user_input:
        doc_context = create_stuff_documents_chain(model, prompt)
        retriever = st.session_state.vectors.as_retriever()
        retrieved_data = create_retrieval_chain(retriever, doc_context)
        response = retrieved_data.invoke({'input': user_input})

    st.write('AI Answer')
    st.markdown(response['answer'])

    with st.expander('Context from the document'):
        if 'context' in response:
            for i, doc in enumerate(response['context']):
                st.write(doc.page_content)