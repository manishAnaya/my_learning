import streamlit as st
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

st.title('RGC')

role = st.selectbox('Please select your Role', ['AI Engineer', 'Flutter Engineer', 'Electrical Engineer', 'Doctor', 'Youtuber'])
goal = st.text_input('What is your goal')
context = st.text_area('What is your experince')

prompt = PromptTemplate(
    template='You are senior {role} working in a company, your goal is {goal} and you have {context}',
    input_variables=['role', 'goal', 'context']
)

final_prompt = prompt.invoke({'role': role, 'goal': goal, 'context': context})

model = ChatGroq(model='openai/gpt-oss-120b', temperature=0.6)

response = model.invoke(final_prompt)

if st.button('Send'):
    st.write(response.content)
