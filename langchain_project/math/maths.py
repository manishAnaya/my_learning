import streamlit as st
from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.tools import tool
from langchain.agents import create_agent
from langchain_community.utilities import WikipediaAPIWrapper
from langchain_community.callbacks import StreamlitCallbackHandler
import re
import wikipedia

load_dotenv()

st.title('Text to Math Problem Solver')

with st.sidebar:
    api_key = st.text_input('Please enter your Groq API key', type='password')

    if not api_key:
        st.info('Please provide API key to proceed')
        st.stop()

model = ChatGroq(model='openai/gpt-oss-120b')

# Wikipedia tool
wikipedia.set_user_agent("MyLearningApp/1.0 (your-email@example.com)")
wikipedia_wrapper = WikipediaAPIWrapper()

@tool
def wikipedia_tool(query: str) -> str :
    """Search Wikipedia for information using Internet."""
    return wikipedia_wrapper.run(query)

# Calculator tool
@tool
def calculator(expression: str) -> str :
    """Use this tool for mathematical questions."""
    math_expr = ''.join(re.findall(r'[\d\.\+\-\*\/\(\)\s]+', expression))
    return str(eval(math_expr, {"__builtins__": {}}, {}))

prompt = """
You are an assistant tasked with solving mathematical and logical problems.
Logically arrive at the solution and display it pointwise.

Question: {question}
Answer:
"""

prompt_template = PromptTemplate(template=prompt, input_variables=['question'])

chain = prompt_template | model

@tool
def reasoning(question: str) -> str:
    """Answer logic-based and reasoning questions step by step."""
    response = chain.invoke({"question": question})
    return response.content

tools = [wikipedia_tool, calculator, reasoning]

agent = create_agent(model=model, tools=tools)

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = [{
        'role': 'assistant',
        'content': "Hi! I am a Math Chatbot. I can answer math, logical reasoning, and general knowledge questions."
    }]

# Display previous messages
for msg in st.session_state.messages:
    with st.chat_message('role'):
        st.write(msg['content'])

# Get user questions
question = st.chat_input("Ask me anything...")

if question:
     # Display user message
    with st.chat_message('user'):
        st.write(question)
    # Save user message
    st.session_state.messages.append({
        "role": "user",
        "content": question
    })

    # Get agent response
    with st.chat_message('assistant'):
        with st.spinner('Thinking...'):
            response = agent.invoke({
                'messages': [{
                    "role": "user", "content": question
                }]
            })
            answer = response['messages'][-1].content
            st.write(answer)
    
    # Save assistant response
    st.session_state.messages.append({
        "role": "assistant",
        "content": answer
    })