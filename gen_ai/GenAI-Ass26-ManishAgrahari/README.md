# Groq API and FastAPI Assignment

## Project Structure

```text
├── main.py
├── task.py
├── task.ipynb
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```

## Tasks Completed

### Task 1: Groq API Setup & Basic Chat

### Task 2: Build a Groq Chatbot

### Task 3: Groq-Based RAG Pipeline

### Task 4: Prompt Template for Groq RAG

### Task 5: Create FastAPI Application

### Task 6: FastAPI + Groq Integration

### Task 7: Run & Test FastAPI App Locally

### Task 8: Production Readiness

### Task 9: End-to-End Demo

### Task 10: Observations & Insights

## Installation

Install the required packages:

```bash
pip install -r requirements.txt
```

Create a `.env` file in the project directory:

```env
GROQ_API_KEY=your_groq_api_key_here
```

## Run the FastAPI Application

The FastAPI application for Tasks 6–9 is in `task.py`.

```bash
uvicorn task:app --reload
```

## Test the API

Open Swagger UI:
http://127.0.0.1:8000/docs

### Available Endpoints

- `GET /health` — Checks whether the API is running.
- `POST /chat` — Sends a question to Groq and returns the generated answer.

