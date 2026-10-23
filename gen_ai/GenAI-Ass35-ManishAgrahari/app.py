import re
import streamlit as st
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain.agents import create_agent
from langchain_core.tools import tool
import wikipedia
from langchain_community.utilities import WikipediaAPIWrapper

load_dotenv()

st.title("Text-to-Math Agent")
st.caption("Solve arithmetic, percentage, and algebra problems along with general knowledge questions.")

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


# Initialize model
@st.cache_resource
def get_agent():
    model = ChatGroq(model="openai/gpt-oss-120b")
    return create_agent(
        model=model,
        tools=[calculator, wikipedia_tool],
        system_prompt="""
        You are a Text-to-Math assistant and general knowledge Expert

        Understand word problems, explain the solution
        step by step, use the calculator for arithmetic,
        and provide the final answer clearly.

        Remember relevant information from earlier
        messages when answering follow-up questions.
        """
    )


assistant_agent = get_agent()

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": "Hi! I am a Math Chatbot. I can answer math, logical reasoning, and general knowledge questions."
        }
    ]

# Display previous conversation
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Get new question
question = st.chat_input("Enter your math question...")

if question:
    # Save user question
    st.session_state.messages.append({
        "role": "user",
        "content": question
    })

    with st.chat_message("user"):
        st.markdown(question)

    # Send complete conversation history
    with st.chat_message("assistant"):
        with st.spinner("Solving your problem..."):
            response = assistant_agent.invoke({
                "messages": st.session_state.messages
            })
            # Get the final answer
            answer = response["messages"][-1].content
            st.markdown(answer)
    # Save assistant answer
    st.session_state.messages.append({
        "role": "assistant",
        "content": answer
    })
