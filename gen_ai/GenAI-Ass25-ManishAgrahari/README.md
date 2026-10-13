# LangChain Assignment: Tasks 1–10

## Project Overview
This project covers LangChain prompt templates, structured outputs, error handling, chains, Runnables, and RAG.

## Tasks Covered

1. **PromptTemplate** – Create prompts with dynamic inputs.
2. **ChatPromptTemplate** – Structure conversations using system and human messages.
3. **Pydantic Output Schema** – Generate structured responses using Pydantic.
4. **Validation & Error Handling** – Handle invalid outputs and exceptions.
5. **Simple Chain** – Connect a prompt, LLM, and output.
6. **Conditional Chain** – Route inputs based on conditions.
7. **Parallel Chain** – Execute multiple chains in parallel.
8. **Runnables Basics** – Use RunnableSequence, RunnablePassthrough, RunnableParallel, and LCEL.
9. **LCEL-Based RAG Chain** – Retrieve relevant documents and generate answers.
10. **Observations & Insights** – Summarize structured output, LCEL, and chain selection.

## Requirements

```bash
pip install langchain-core langchain-groq langchain-community langchain-huggingface faiss-cpu sentence-transformers pydantic python-dotenv
```

## Setup

1. Install the required packages.
2. Add your Groq API key to the `.env` file.
3. Run the tasks in the Jupyter Notebook in order.
