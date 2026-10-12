# Ollama Chatbot with LangChain and LangSmith

## Project Overview

This project demonstrates how to build a chatbot using a locally running Large Language Model (LLM) with Ollama and LangChain.
LangSmith is used to trace and monitor model calls, including inputs, outputs, execution status, and latency.

## Project Structure

    ollama_assignment/
    ├── task.ipynb
    ├── requirements.txt


## Required Python Packages

Create a `requirements.txt` file with the following packages:

    langchain
    langchain-ollama
    langsmith
    python-dotenv

Install the required packages:

    pip install -r requirements.txt

## Ollama Setup

### Step 1: Install Ollama

Download and install Ollama from the official website:

https://ollama.com/download

Verify the installation:

    ollama --version

### Step 2: Download a Model

Download the Llama 3 model:

    ollama pull llama3

Alternatively, download Mistral:

    ollama pull mistral

### Step 3: Run the Model

Start an interactive chat session:

    ollama run llama3

Enter a prompt and verify that the model generates a response.

Type `/bye` to exit the interactive session.

Ollama runs the model locally, so an OpenAI API key is not required.

## LangSmith Configuration

### Step 1: Create a LangSmith Account

Visit:

https://smith.langchain.com/

Create an account and generate an API key from your LangSmith settings.

### Step 2: Configure Environment Variables

Create a `.env` file in the project root:

    LANGSMITH_TRACING=true
    LANGSMITH_API_KEY=your_langsmith_api_key
    LANGSMITH_PROJECT=ollama-assignment

Never upload your actual API key or `.env` file to GitHub.

Add the following to `.gitignore`:

    .env
    .venv/
    __pycache__/

## Task 1: Ollama Setup and Basic Chat

### Implementation

The following code initializes the local Ollama model, sends a prompt, and prints the response.

    from dotenv import load_dotenv
    from langchain_ollama import ChatOllama

    # Load LangSmith environment variables
    load_dotenv()

    # Initialize the Ollama chat model
    llm = ChatOllama(
        model="llama3",
        temperature=0.7
    )

    # Send a prompt to the model
    question = "Explain artificial intelligence in simple words."

    response = llm.invoke(question)

    # Print the response
    print("Question:", question)
    print("Response:", response.content)

### Run the Code

Save the code in `task1_ollama.py` or execute it in `task.ipynb`.

Run the Python script:

    python task1_ollama.py

Make sure Ollama is installed, the model is downloaded, and the Ollama service is running.

## Tracking with LangSmith

LangSmith tracing is enabled through the environment variables configured in `.env`.

After executing the LangChain model call:

1. Open the LangSmith dashboard.
2. Open the `ollama-assignment` project.
3. Locate the latest run.
4. Inspect the input prompt and generated output.
5. Review execution status and latency.
6. Capture a screenshot showing the trace details.

Dashboard:

https://smith.langchain.com/

Note: Trace availability depends on successful configuration, network connectivity, and the current LangSmith interface.

## Screenshot Submission

Capture a screenshot of the LangSmith project showing the recorded model execution and relevant trace details.

Upload the screenshot to Google Drive and include the shareable link with your assignment submission.

Ensure the screenshot clearly shows the input, output, and run details. Do not expose API keys or other secrets.

## Run the Project

### Step 1: Create a Virtual Environment

Windows:

    python -m venv .venv
    .venv\Scripts\activate

macOS/Linux:

    python3 -m venv .venv
    source .venv/bin/activate

### Step 2: Install Dependencies

    pip install -r requirements.txt

### Step 3: Configure LangSmith

Create the `.env` file and add your LangSmith API key and project settings.

### Step 4: Start Ollama

Ensure Ollama is running and the selected model is available.

For example:

    ollama run llama3

### Step 5: Execute the Notebook

Open the notebook:

    jupyter notebook task.ipynb

Run the cells sequentially.

## Important Notes

- Ollama runs the selected LLM locally.
- The first model download requires an internet connection.
- Model performance depends on available system memory and hardware.
- LangSmith is used for tracing and monitoring; its hosted dashboard requires network access.
- Do not commit API keys or `.env` files to version control.