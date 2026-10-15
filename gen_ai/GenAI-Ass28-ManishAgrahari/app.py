import streamlit as st
from langchain_chroma import Chroma
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_groq import ChatGroq
from langchain_classic.document_loaders import PyPDFLoader
from langchain_core.messages import AIMessage, HumanMessage, trim_messages
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_classic.chains.combine_documents import create_stuff_documents_chain
from langchain_classic.chains import create_retrieval_chain

load_dotenv()

# Initialize RAG components once
@st.cache_resource
def setup_rag():
    loader = PyPDFLoader('physical.pdf')

    docs = loader.load()

    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)

    chunks = splitter.split_documents(docs)

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    vector_store = Chroma.from_documents(documents=chunks, embedding=embeddings, persist_directory='./chroma_db')

    retriever = vector_store.as_retriever(search_kwargs={"k": 3})

    llm = ChatGroq(model="openai/gpt-oss-120b")

    prompt = ChatPromptTemplate.from_messages([
            (   
            "system",
            """Answer questions using the retrieved document context.
            Use conversation history to understand follow-up questions.
            If the answer is not in the context, say you don't know.

            Context:
            {context}"""
            ),
            MessagesPlaceholder(variable_name="history"),
            ("human", "{input}")
        ])

    ques_ans_chain = create_stuff_documents_chain(llm, prompt)

    rag_chain = create_retrieval_chain(retriever, ques_ans_chain)

    return rag_chain

rag_chain = setup_rag()

trimmer = trim_messages(token_counter=len, max_tokens=2000, strategy='last', include_system=True, allow_partial=False, start_on='human')

st.title("Conversational RAG Assistant")
st.caption("Ask questions about your PDF document.")

# Session-specific conversation history
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

# Display previous messages
for message in st.session_state.chat_history:
    role = 'user' if isinstance(message, HumanMessage) else 'assistant'
    with st.chat_message(role):
        st.markdown(message.content)

# Get new user input
user_input = st.chat_input("Ask something about your document...")

if user_input:
    with st.chat_message('user'):
        st.write(user_input)

    trimmed_history = trimmer.invoke(st.session_state.chat_history)

    with st.chat_message('assistant'):
        with st.spinner('Thinking'):
            response = rag_chain.invoke({
                'history': trimmed_history,
                'input': user_input
            })
            answer = response["answer"]
            st.markdown(answer)

    st.session_state.chat_history.append(HumanMessage(content=user_input))
    st.session_state.chat_history.append(AIMessage(content=answer))