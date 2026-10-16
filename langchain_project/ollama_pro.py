from langchain_ollama import OllamaLLM
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

prompt = ChatPromptTemplate([
    ('system', '''
        You're an helpful AI Assistant
    '''),
    ('human', 'Question {question}')
])

def generate_response(query, model, temprature):
    llm = OllamaLLM(model=model, temperature=temprature)
    parser = StrOutputParser()

    chain = prompt | llm | parser

    result = chain.invoke({'question': query})
    return result

st.title('Q & A Chatbot with Ollama')

query = st.text_input('Ask anything...')

st.sidebar.title('Settings')

model = st.sidebar.selectbox('Select the Groq Model', ['gemma3:latest'])

temprature = st.sidebar.slider('Select Temprature for model', min_value=0.0, max_value=2.0, value=1.0)

if st.button('Send'):
    if query:
        response = generate_response(query=query, model=model, temprature=temprature)
        st.markdown(response)
    else:
        st.warning('Write some query before sending')
        