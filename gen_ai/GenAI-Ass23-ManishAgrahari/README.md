Project Structure

GenAI-Ass23-ManishAgrahari/
├── task.ipynb
├── requirements.txt
├── README.md

Note:

task.ipynb contains the implementation of Tasks 1–11.

.env stores the Groq API key.

The FAISS and Chroma directories are optional unless persistence is implemented.

Technologies Used

Python

LangChain

Groq LLM

Hugging Face Sentence Transformers

FAISS

Chroma

Wikipedia Retriever

YouTube Transcript API

Jupyter Notebook

Required Python Packages

Create a requirements.txt file with the following packages:

python-dotenv
langchain
langchain-core
langchain-classic
langchain-community
langchain-groq
langchain-text-splitters
langchain-huggingface
langchain-chroma
sentence-transformers
faiss-cpu
chromadb
wikipedia
youtube-transcript-api

Install the required packages:

pip install -r requirements.txt