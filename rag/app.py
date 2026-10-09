import streamlit as st
from langchain_ollama.llms import OllamaLLM
from dotenv import load_dotenv

load_dotenv()

st.title('Gemma Chatbot')

input_txt = st.text_input('Enter your question: ')

model = OllamaLLM(model='gemma3')

if input_txt:
    response = model.invoke(input_txt)
    st.write(response)


