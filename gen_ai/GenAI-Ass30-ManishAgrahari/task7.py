import streamlit as st

st.title("ChatGroq RAG Chatbot")
st.caption("Ask questions about your documents")

# Initialize chat history
if 'history' not in st.session_state:
    st.session_state.history = [] 

# Upload PDF or TXT documents
uploaded_file = st.file_uploader('Upload your document', type=['pdf'])

if uploaded_file:
    st.success("file uploaded successfully.")

# Display previous history
for message in st.session_state.history:
    with st.chat_message(message['role']):
        st.markdown(message['content'])

# Get user input
question = st.chat_input("Ask a question...")

if question:
    # Save and display the user message
    st.session_state.history.append({
        "role": "user",
        "content": question
    })

    with st.chat_message("user"):
        st.markdown(question)

    response = (
        "This is a sample response. "
        "The RAG backend will be connected later"
    )

    st.session_state.history.append({
        "role": "assistant",
        "content": response
    })

    with st.chat_message("assistant"):
        st.markdown(response)