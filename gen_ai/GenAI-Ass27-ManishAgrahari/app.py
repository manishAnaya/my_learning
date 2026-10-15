import streamlit as st
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser
from langchain_core.messages import HumanMessage, AIMessage, trim_messages

load_dotenv()

# Initialize the LLM and parser 
llm = ChatGroq(model="openai/gpt-oss-120b")
parser = StrOutputParser()

# Create prompt with conversation history
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful Machine Learning assistant. Answer briefly."),
    MessagesPlaceholder(variable_name="history"),
    ("human", "{input}")
])

# Trim older messages to limit history
trimmer = trim_messages(max_tokens=2000, token_counter=llm, include_system=False, allow_partial=False, start_on="human")

# Create the chain
chain = prompt | llm | parser

# Configure the Streamlit app
st.title("Stateful AI Chatbot")

# Initialize chat history
if 'history' not in st.session_state:
    st.session_state.history = []

# Display previous messages
for message in st.session_state.history:
    role = 'user' if isinstance(message, HumanMessage) else 'assistant'
    with st.chat_message(role):
        st.write(message.content)

# Get new user input
user_input = st.chat_input("Ask me anything...")

if user_input:
    # Trim history before sending it to the model
    chat_history = trimmer.invoke(st.session_state.history)

    # Generate the response
    response = chain.invoke({
        'history': chat_history,
        'input': user_input
    })

    # Save messages in session history
    st.session_state.history.append(HumanMessage(content=user_input))
    st.session_state.history.append(AIMessage(content=response))

    with st.chat_message("user"):
        st.write(user_input)

    with st.chat_message("assistant"):
        st.write(response)

