## Project Objective

- Load documents from different sources using LangChain Document Loaders.
- Understand LangChain Document objects.
- Split large documents into smaller chunks.
- Compare different text-splitting techniques.
- Understand structure-based and semantic-based splitting.
- Create a simple document preprocessing pipeline.

## Tasks Covered

### Part 1 — Document Loaders

1. TextLoader

2. CSVLoader

3. PyPDFLoader

4. DirectoryLoader

5. WebBaseLoader

### Part 2 — Text Splitters

6. Why Text Splitting is Required

7. CharacterTextSplitter

8. RecursiveCharacterTextSplitter

9. Document Structure-Based Splitting

10. Semantic Meaning-Based Splitting

### Part 3 — Mini Integration Task

11. Unified Preprocessing Pipeline

12. Observations & Insights


## Project Structure

├── data/
│   ├── sample.txt
│   ├── *.pdf
├── task.ipynb
├── requirements.txt
└── README.md

## Required Python Packages

Create requirements.txt with:

langchain
langchain-community
langchain-text-splitters
langchain-experimental
langchain-huggingface
pypdf

Install:

pip install -r requirements.txt

## Run

Open the notebook:

jupyter notebook task.ipynb

or:

jupyter lab

Run the cells from Task 1 to Task 12.

## RAG Preprocessing Flow

Documents
    ↓
Document Loader
    ↓
LangChain Documents
    ↓
Text Splitting
    ↓
Chunks
    ↓
Embeddings
    ↓
Vector Database
    ↓
Relevant Chunks
    ↓
LLM

