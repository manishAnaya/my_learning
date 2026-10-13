import streamlit as st
from langchain_ollama import OllamaLLM

st.title('Static Prompting')

model = OllamaLLM(model='gemma3')

input = st.text_input('What is your query')

response = model.invoke(input)

if st.button('Answer'):
    st.write(response)