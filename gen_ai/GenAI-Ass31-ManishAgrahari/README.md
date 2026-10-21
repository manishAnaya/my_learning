# GenAI Assignment 31

## Project Structure
GenAI-Ass31-ManishAgrahari/
├── task.ipynb
├── app.py
├── requirements.txt
├── README.md
└── .env                

## Requirements
- Python 3.10+ (use a version supported by your installed dependencies)
- A Groq API key

## Installation
1. Create and activate a virtual environment.
2. Install dependencies:
   pip install -r requirements.txt
3. Create a .env file containing:
   GROQ_API_KEY=your_groq_api_key_here
4. Add .env and .venv/ to .gitignore.

## Run the Application
streamlit run app.py

## Notes
- The embedding model is sentence-transformers/all-MiniLM-L6-v2.
- The chat model used in the assignment is openai/gpt-oss-120b via Groq, subject to model availability.
- Chat history is stored in Streamlit session state and may be lost when the session ends.