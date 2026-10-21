from langchain_groq import ChatGroq
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_classic.chains import create_retrieval_chain, create_history_aware_retriever
from langchain_classic.chains.combine_documents import create_stuff_documents_chain
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_chroma import Chroma
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

st.title('Conversation RAG with PDF')

api_key = st.text_input('Please enter Groq API key to proceed', type='password')

if api_key:

    model = ChatGroq(model='openai/gpt-oss-120b', api_key=api_key)

    session_id = st.text_input('Please provide your Session Id', value='default_id')

    if 'store' not in st.session_state:
        st.session_state.store = {}

    uploaded_file = st.file_uploader('Upload your pdf file', type=['pdf'])

    if uploaded_file:

        temp_pdf = './temporary.pdf'
        with open(temp_pdf, 'wb') as file:
            file.write(uploaded_file.getvalue())

        loader = PyPDFLoader(temp_pdf)
        with st.spinner('Loading PDF file'):
            document = loader.load()

        splitter = RecursiveCharacterTextSplitter(chunk_size=2000, chunk_overlap=200)
        with st.spinner('Splitting pdf content into chunks'):
            chunks = splitter.split_documents(document)

        with st.spinner('Loading HuggingFace Embeddings model'):
            embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
        with st.spinner('Coverting chunks into embeddings'):
            vector = Chroma.from_documents(documents=chunks, embedding=embeddings, persist_directory='./Chroma.db')

        retriever = vector.as_retriever()

        # Code for storing history
        contextualize_system_prompt = '''
        Given with a chat history and the latest user question,
        reformulate the question to make it standalone. Do not answer, only rephrase
        '''

        contextualize_prompt = ChatPromptTemplate.from_messages([
            ('system', contextualize_system_prompt),
            MessagesPlaceholder(variable_name='chat_history'),
            ('human', '{input}')
        ])

        history_aware_retriever = create_history_aware_retriever(model, retriever, contextualize_prompt)

        system_prompt = '''
            You are an helpful AI Assistant.
            For Question Answering system.
            Answer from the context provided only.
            If Unsure, Say I dont know
            context:
            {context}
            '''

        qa_prompt = ChatPromptTemplate.from_messages([
            ('system', system_prompt),
            MessagesPlaceholder(variable_name='chat_history'),
            ('human', '{input}')
        ])

        documents_chain = create_stuff_documents_chain(model, qa_prompt)

        retrieval_chain = create_retrieval_chain(history_aware_retriever, documents_chain)

        def get_session_history(session_id):
            if session_id not in st.session_state.store:
                st.session_state.store[session_id] = ChatMessageHistory()
            return st.session_state.store[session_id]

        conversational_rag_chain = RunnableWithMessageHistory(
            retrieval_chain,
            get_session_history,
            input_messages_key='input',
            history_messages_key='chat_history',
            output_messages_key='answer'
        )

        user_input = st.text_input('Ask a question from uploaded pdf')

        if user_input:
            session_history = get_session_history(session_id)
            with st.spinner('Thinking...'):
                response = conversational_rag_chain.invoke({
                    'input': user_input,
                },
                config={'configurable': {'session_id': session_id}}
                )

                st.subheader('AI Assistant Answer')
                st.markdown(response['answer'])

            with st.expander('Chat History'):
                st.write(session_history.messages)
else:
    st.write('Please enter your api key to proceed')