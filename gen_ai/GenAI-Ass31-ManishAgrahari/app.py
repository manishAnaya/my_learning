from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage, AIMessage, trim_messages
from langchain_classic.chains import create_retrieval_chain
from langchain_classic.chains.combine_documents import create_stuff_documents_chain
import streamlit as st

load_dotenv()

st.title("Conversational PDF RAG Chatbot")
st.caption("Upload a PDF and ask questions about its content.")

# Initialize models once
@st.cache_resource
def load_models():
    with st.spinner("Loading HuggingFace Embeddings and Chat Models..."):
        embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
        llm = ChatGroq(model="openai/gpt-oss-120b", temperature=0)
        return embeddings, llm

embeddings, llm = load_models()

if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

if 'retrieval_chain' not in st.session_state:
    st.session_state.retrieval_chain = None

# Upload PDF
uploaded_file = st.file_uploader("Upload your PDF", type=["pdf"])

if st.button('Create Embeddings', disabled=uploaded_file is None):
    temp_pdf = './temp.pdf'
    with open(temp_pdf, 'wb') as f:
        f.write(uploaded_file.getvalue())

    # Initialize PDF loader
    loader = PyPDFLoader(temp_pdf)
    # Load PDF
    with st.spinner("Loading PDF file..."):
        docs = loader.load()

    with st.spinner("Creating embeddings..."):
        # Initialize Recursive Character Text Splitter and splitting docs into chunks
        splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
        chunks = splitter.split_documents(docs)

        # Creating vector store from embedded chunks and making it as retriever
        vector_store = FAISS.from_documents(chunks, embeddings)
        retriever = vector_store.as_retriever()

    # Prompt uses the same chat_history key as Task 5
    system_prompt = '''
    You are a helpful PDF question-answering assistant.
    Answer using only the retrieved PDF context.
    If the answer is not found in the context, say:
    I don't know.

    context:
    {context}
    '''
    prompt = ChatPromptTemplate.from_messages([
        ('system', system_prompt),
        MessagesPlaceholder(variable_name='chat_history'),
        ('human', '{input}')
    ])

    with st.spinner("Processing..."):
        documents_chain = create_stuff_documents_chain(llm, prompt)
        retrieval_chain = create_retrieval_chain(retriever, documents_chain)

        st.session_state.retrieval_chain = retrieval_chain
        st.session_state.chat_history = []

    st.success("PDF processed! You can now ask questions.")


# Display previous chat messages
for message in st.session_state.chat_history:
    role = 'user' if isinstance(message, HumanMessage) else 'assistant'
    with st.chat_message(role):
        st.markdown(message.content)

user_input = st.chat_input("Ask something about your PDF...")

if user_input and st.session_state.retrieval_chain is None:
    st.warning("Upload a PDF and click Create Embeddings first.")
elif user_input:
    with st.chat_message('user'):
        st.markdown(user_input)
    try:
        trimmer = trim_messages(token_counter=llm, max_tokens=2000, strategy='last', include_system=True, allow_partial=False, start_on='human')

        trimmed_history = trimmer.invoke(st.session_state.chat_history)

        with st.chat_message('assistant'):
            with st.spinner("Thinking..."):
                response = st.session_state.retrieval_chain.invoke({
                    'input': user_input,
                    'chat_history': trimmed_history
                })

                answer = response["answer"]
                st.markdown(answer)

        st.session_state.chat_history.append(HumanMessage(content=user_input))
        st.session_state.chat_history.append(AIMessage(content=answer))

    except Exception as e:
            st.error(f"Error generating answer: {e}")