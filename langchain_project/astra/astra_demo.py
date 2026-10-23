# from langchain_community.vectorstores import Cassandra
# from PyPDF2 import PdfReader
# from langchain_text_splitters import CharacterTextSplitter
# import os
# import cassio
# from typing_extensions import Concatenate
# from langchain_huggingface import HuggingFaceEmbeddings
# from langchain_groq import ChatGroq
# from langchain_classic.indexes.vectorstore import VectorStoreIndexWrapper

# pdf_reader = PdfReader("physical.pdf")

# raw_text = ''

# for i, page in enumerate(pdf_reader.pages):
#     content = page.extract_text()
#     if content:
#         raw_text += content

# # To establish the connection to Astra DB
# cassio.init(token=ASTRA_DB_APPLICATION_TOKEN, database_id=ASTRA_DB_ID)

# llm = ChatGroq(model='openai/gpt-oss-120b', api_key=GROQ_API_KEY)

# embeddings = HuggingFaceEmbeddings(model='sentence-transformers/all-MiniLM-L6-v2')

# astra_vector_store = Cassandra(embedding=embeddings, table_name='qa_demo_one', session=None, keyspace=None)

# text_splitter = CharacterTextSplitter(separator='\n', chunk_size=800, chunk_overlap=200, length_function=len)

# chunks = text_splitter.split_text(raw_text)

# astra_vector_store.add_texts(chunks)

# astra_vector_index = VectorStoreIndexWrapper(vectorstore=astra_vector_store)

# first_question = True

# while True:
#     if first_question:
#         query_text = input('Type your question or type quit to exit').strip()
#     else:
#         query_text = input('What is your next question or type quit to exit').strip()

#     if query_text.lower() == 'quit':
#         break
#     if not query_text:
#         continue

#     first_question = False

#     answer = astra_vector_index.query(query_text, llm=llm)
#     print(answer)

#     for doc, score in astra_vector_store.similarity_search_with_score(query_text, k=4):
#         print(score, doc.page_content)

import os
import cassio

from dotenv import load_dotenv
from PyPDF2 import PdfReader
from langchain_community.vectorstores import Cassandra
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_groq import ChatGroq
from langchain_classic.indexes.vectorstore import VectorStoreIndexWrapper

load_dotenv()

ASTRA_DB_APPLICATION_TOKEN = os.getenv(
    "ASTRA_DB_APPLICATION_TOKEN"
)
ASTRA_DB_ID = os.getenv("ASTRA_DB_ID")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if not all([
    ASTRA_DB_APPLICATION_TOKEN,
    ASTRA_DB_ID,
    GROQ_API_KEY,
]):
    raise ValueError("Please configure the API keys in .env")

# 1. Read PDF
pdf_reader = PdfReader("physical.pdf")

raw_text = "\n".join(
    page.extract_text() or ""
    for page in pdf_reader.pages
)

if not raw_text.strip():
    raise ValueError("No extractable text found in the PDF.")

# 2. Split text into chunks
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=800,
    chunk_overlap=200
)

chunks = text_splitter.split_text(raw_text)

# 3. Initialize Astra DB
cassio.init(
    token=ASTRA_DB_APPLICATION_TOKEN,
    database_id=ASTRA_DB_ID
)

# 4. Initialize models
llm = ChatGroq(
    model="openai/gpt-oss-120b",
    api_key=GROQ_API_KEY
)

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# 5. Create vector store
vector_store = Cassandra(
    embedding=embeddings,
    table_name="qa_demo_one",
    session=None,
    keyspace=None
)

# 6. Insert chunks
# Run this ingestion step only when needed.
vector_store.add_texts(chunks)

# 7. Create index wrapper
vector_index = VectorStoreIndexWrapper(
    vectorstore=vector_store
)

# 8. Ask questions
while True:
    query = input(
        "\nEnter your question (or 'quit' to exit): "
    ).strip()

    if query.lower() == "quit":
        break

    if not query:
        continue

    answer = vector_index.query(query, llm=llm)
    print("\nAnswer:", answer)

    print("\nRelevant chunks:")
    results = vector_store.similarity_search_with_score(
        query,
        k=4
    )

    for doc, score in results:
        print(f"\nScore: {score}")
        print(doc.page_content)