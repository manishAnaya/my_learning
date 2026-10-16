# OpenAI and Ollama Q&A Chatbot using LangChain

## Project Structure

├── .env
├── requirements.txt
├── README.md
├── task.ipynb
└── app.py
```

## Required Python Packages

Create a `requirements.txt` file containing:

```text
langchain
langchain-core
langchain-openai
langchain-groq
langchain-ollama
python-dotenv
streamlit
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

## Environment Configuration

Create a `.env` file in the project root directory.

For OpenAI:

```text
OPENAI_API_KEY=your_openai_api_key
```

For Groq:

```text
GROQ_API_KEY=your_groq_api_key
```

Use only the API key required by your selected provider.

Load environment variables using:

```python
from dotenv import load_dotenv

load_dotenv()
```

### Step 

python -m venv .venv

Activate it on Windows:

.venv\Scripts\activate

pip install -r requirements.txt

Create the `.env` file and add the appropriate provider API key.

Install Ollama, pull the Llama 3 model, and test the local model.

streamlit run app.py

