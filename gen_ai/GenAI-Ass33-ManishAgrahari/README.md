# GenAI Assignment 33

## Project Structure

```text
GenAI-Ass33-ManishAgrahari/
├── task.ipynb
├── requirements.txt
├── README.md
└── .env
```

## Requirements

- Python 3.10 or later, compatible with the installed dependencies.
- A Groq API key.
- SQLite database (`company.db`), created by Task 1.

## Installation

1. Create and activate a virtual environment.
2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the project directory and add your Groq API key:

   ```text
   GROQ_API_KEY=your_groq_api_key_here
   ```

## Run the Application

Open `task.ipynb` in Jupyter Notebook or VS Code and run the cells in order, from Task 1 through Task 8.

## Technologies Used

- Python
- SQLite
- SQLAlchemy
- LangChain
- LangChain Community
- ChatGroq
- python-dotenv
- Jupyter Notebook