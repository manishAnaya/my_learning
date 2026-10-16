from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

prompt = ChatPromptTemplate([
    ('system', '''
        You're an helpful AI Assistant
    '''),
    ('human', 'Question {question}')
])

def generate_response(query, model, temprature, api_key, max_tokens):
    llm = ChatGroq(
        model=model, 
        temperature=temprature,
        api_key=api_key,
        max_tokens=max_tokens
    )
    parser = StrOutputParser()

    chain = prompt | llm | parser

    result = chain.invoke({'question': query})

    return result

st.title('Q & A Chatbot with ChatGroq')

query = st.text_input('Ask anything...')

st.sidebar.title('Settings')

api_key = st.sidebar.text_input('Enter Groq API Key', type='password')

model = st.sidebar.selectbox('Select the Groq Model', ['openai/gpt-oss-120b', 'openai/gpt-oss-20b', 'qwen/qwen3.8-27b', 'openai/gpt-oss-safeguard-20b'])

temprature = st.sidebar.slider('Select Temprature for model', min_value=0.0, max_value=2.0, value=0.8)

max_tokens = st.sidebar.slider('Select Max Tokens', min_value=50.0, max_value=500.0, value=200.0)

if st.button('Send'):
    if query and api_key:
        response = generate_response(query, model, temprature, api_key, max_tokens)
        st.markdown(response)
    else:
        st.warning('Please enter some query and provide API key')