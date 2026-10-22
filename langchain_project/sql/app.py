import streamlit as st
from pathlib import Path
from langchain_community.agent_toolkits import create_sql_agent, SQLDatabaseToolkit
from langchain_community.callbacks.streamlit import StreamlitCallbackHandler
from sqlalchemy import create_engine
import sqlite3
from langchain_groq import ChatGroq
from urllib.parse import quote_plus
from langchain_community.utilities import SQLDatabase
import os
from dotenv import load_dotenv

load_dotenv()

st.title('Langchain: Chat with SQL Database')

LOCAL_DB = 'USE_LOCALDB'
MYSQLDB = 'USE_MYSQL' 

radio_option = ['Use Sqlite database (student.db)', 'Connect to MySql DB']

selected_option = st.sidebar.radio('Choose the DB you want to get information', options=radio_option)

if selected_option == 'Connect to MySql DB':
    db_uri = MYSQLDB
    mysql_host = st.sidebar.text_input('Provide MySql Hostname', value='localhost')
    mysql_user = st.sidebar.text_input('Provide MySql Username', value='root')
    mysql_password = st.sidebar.text_input('Provide MySql Password', value='password')
    mysql_db = st.sidebar.text_input('Provide MySql DB name')
else:
    db_uri = LOCAL_DB

groq_api = st.text_input('Please provide groq API key: ', type='password')

if not groq_api:
    st.info('Please provide your Groq API key to proceed')
    st.stop()

model = ChatGroq(model='openai/gpt-oss-120b', api_key=groq_api, streaming=True)

@st.cache_resource(ttl=7200)
def configure_db(db_uri, mysql_host=None, mysql_user=None, mysql_pass=None, mysql_db=None):
    if db_uri == LOCAL_DB:
        dbfilepath = (Path(__file__).parent/'student.db').absolute()
        creator = lambda: sqlite3.connect(f"file:{dbfilepath}?mode=ro",uri=True)
        return SQLDatabase(create_engine("sqlite:///", creator=creator))
    
    elif db_uri == MYSQLDB:
        if not (mysql_host and mysql_user and mysql_pass and mysql_db):
            st.error('Please provide all details to proceed')
            st.stop()

        encoded_pass = quote_plus(mysql_pass)
        connection_str = f"mysql+mysqlconnector://{mysql_user}:{encoded_pass}@{mysql_host}/{mysql_db}"

        try:
            db =SQLDatabase(create_engine(connection_str))
            st.success('Successfully connected to MySQL Database')
            return db
        
        except Exception as e:
            st.error(f'Failed to connect to DB: {e}')

if db_uri == MYSQLDB:
    db = configure_db(db_uri, mysql_host, mysql_user, mysql_password, mysql_db)
else:
    db = configure_db(db_uri)

toolkit = SQLDatabaseToolkit(db=db, llm=model)
agent = create_sql_agent(
    llm=model,
    toolkit=toolkit,
    verbose=True,
    agent_type="tool-calling",
    agent_executor_kwargs={"handle_parsing_errors": True},
)

if 'messages' not in st.session_state or st.sidebar.button('clear message history'):
    st.session_state['messages'] = [{'role': 'Assistant', 'content': 'How can I help you today.'}]

    for msg in st.session_state['messages']:
        st.chat_message(msg['role']).write(msg['content'])

user_input = st.chat_input(placeholder='Ask anything from database') 

if user_input:
    st.session_state['messages'].append({'role': 'user', 'content': user_input})
    st.chat_message('user').write(user_input)

    with st.chat_message('assistant'):
        streamlit_callback = StreamlitCallbackHandler(st.container())
        result = agent.invoke(
            {"input": user_input},
            config={"callbacks": [streamlit_callback]},
        )
        response = result["output"]
        st.session_state['messages'].append({'role': 'assistant', 'content': response})
        st.write(response)
