from fastapi import FastAPI
from dotenv import load_dotenv
from pydantic import BaseModel
from langchain_groq import ChatGroq

# Load env variables
load_dotenv()

# Initialize FastAPI
app = FastAPI()

# Initialize Groq model
llm = ChatGroq(model="openai/gpt-oss-120b")

class ChatRequest(BaseModel):
    query: str

# Health endpoint
@app.get('/health')
def health():
    return {'health': 'API is running'}

# Chat endpoint
@app.post('/chat')
def chat(request: ChatRequest):
    response = llm.invoke(request.query)
    return {'answer': response.content}
