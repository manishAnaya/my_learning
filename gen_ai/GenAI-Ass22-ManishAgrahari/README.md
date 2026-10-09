## Project Structure

    embedding_assignment/
    ├── task.ipynb
    ├── requirements.txt
    ├── README.md
    ├── .env
    ├── faiss_index/
    └── chroma_db/

## Required Python Packages

Create a `requirements.txt` file with:

    openai
    python-dotenv
    sentence-transformers
    numpy
    scikit-learn
    langchain
    langchain-core
    langchain-community
    langchain-huggingface
    langchain-ollama
    langchain-chroma
    faiss-cpu
    chromadb

Install the required packages:

    pip install -r requirements.txt

## Additional Setup — Ollama

Install Ollama from:

https://ollama.com/

Download the embedding model:

    ollama pull nomic-embed-text

Verify the installed model:

    ollama list

Make sure Ollama is running before generating embeddings.

## OpenAI API Configuration

If you use OpenAI embeddings, create a `.env` file:

    OPENAI_API_KEY=your_api_key_here

Load the API key in Python:

    from dotenv import load_dotenv
    import os

    load_dotenv()

    api_key = os.getenv("OPENAI_API_KEY")

Never upload your actual API key or `.env` file to GitHub.

Note: Hugging Face and Ollama can be used for the embedding tasks without an OpenAI API key.

## Run the Project

Open the notebook using Jupyter Notebook:

    jupyter notebook task.ipynb

Or use JupyterLab:

    jupyter lab

Run the notebook cells sequentially from Task 1 to Task 11.
