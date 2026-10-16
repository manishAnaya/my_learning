import streamlit as st
from langchain_groq import ChatGroq
from langchain_ollama import ChatOllama
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

st.title("Q&A Chatbot")

model_type = st.selectbox("Choose your model",["Groq", "Ollama"])

prompt = ChatPromptTemplate([
    ('system', 'You are a helpful AI assistant.'),
    ('human', '{question}')
])

parser = StrOutputParser()

question = st.text_area("Enter your question")

if st.button("Get Answer"):
    if not question.strip():
        st.warning("Please enter a question.")
    else:
        if model_type == 'Groq':
            llm = ChatGroq(model='openai/gpt-oss-120b')
        elif model_type == 'Ollama':
            llm = ChatOllama(model="gemma3:latest", temperature=0.5)

    chain = prompt | llm | parser

    with st.spinner("Generating answer..."):
        answer = chain.invoke({"question": question})

    st.write(answer)