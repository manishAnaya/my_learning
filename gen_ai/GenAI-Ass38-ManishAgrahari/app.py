from langchain_ollama import ChatOllama
import streamlit as st

model = ChatOllama(model="codellama:latest", temperature=0)

def code_assistant(task, user_input):
    prompts = {
        "Generate Code": f"""
        Generate Python code for the following requirement:
        {user_input}
        """,
        "Explain Code": f"""
        Explain the following code step by step in simple language:
        {user_input}
        """,
        "Debug Code": f"""
        Find and fix bugs in the following code.
        Explain the issue and provide corrected code:
        {user_input}
        """,
        "Optimize Code": f"""
        Improve the readability and efficiency of the following code.
        Provide the improved version and explain the changes:
        {user_input}
        """
    }

    if task not in prompts:
        return "Invalid task selected."

    response = model.invoke(prompts[task])
    return response.content

st.title("CodeLlama Code Assistant")
st.write("Generate, explain, debug, and optimize Python code.")

task = st.selectbox("Select a task", ["Generate Code", "Explain Code", "Debug Code", "Optimize Code"])

user_input = st.text_area(
    "Enter your requirement or code",
    placeholder="Enter your prompt or paste your code here..."
)

if st.button("Submit"):
    if user_input.strip():
        with st.spinner("Generating response..."):
            try:
                result = code_assistant(task, user_input)
                st.subheader("Response")
                st.markdown(result)
            except Exception as e:
                st.error(f"Error: {e}")
    else:
        st.warning("Please enter a requirement or code.")