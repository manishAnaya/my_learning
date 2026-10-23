
# GenAI Assignment 37 - AstraDB and LangChain

## Project Structure

GenAI-Assignment/
├── task.ipynb
├── physical.pdf
├── requirements.txt
├── README.md
└── .env

## Requirements

- Python 3.10 or later, compatible with the installed packages
- Astra DB account and database
- Astra DB application token and database ID
- Groq API key
- A PDF file named physical.pdf

## Installation

1. Create and activate a Python virtual environment.
2. Install the required packages:
   pip install -r requirements.txt

3. Create a .env file in the project folder and add the following credentials:
   ASTRA_DB_APPLICATION_TOKEN=your_astra_application_token
   ASTRA_DB_ID=your_astra_database_id
   GROQ_API_KEY=your_groq_api_key

4. Replace the placeholder values with your actual credentials.
5. Keep the .env file private. Do not upload it to GitHub.

## How to Run

1. Make sure Astra DB is available and the credentials in .env are correct.
2. Open task.ipynb in Jupyter Notebook or VS Code.
3. Run the notebook cells in order.
4. Ask questions about the PDF when prompted.

## Technologies Used

- Python
- LangChain
- Astra DB
- CassIO
- Hugging Face Embeddings
- Groq
- PyPDF2
- Jupyter Notebook

