import logging
from fastapi import FastAPI, HTTPException
from dotenv import load_dotenv
from pydantic import BaseModel,Field
from langchain_groq import ChatGroq

# Load env variables
load_dotenv()

# TASK 8: Basic Logging
# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize FastAPI
app = FastAPI()

# Initialize Groq model
llm = ChatGroq(model="openai/gpt-oss-120b")

# Request validation
class ChatRequest(BaseModel):
    query: str = Field(min_length=1, max_length=2000)


# Response model
class ChatResponse(BaseModel):
    answer: str

@app.get("/health")
def health():
    return {"status": "API is running"}

@app.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    try:
        logger.info("Received Chat request")
        response = llm.invoke(request.query)
        return ChatResponse(answer=response.content)
    except Exception:
        # TASK 8: Log errors with traceback
        logger.exception("Groq API request failed")
        # Task 6: Handling Error and Exceptions
        raise HTTPException(
            status_code=502,
            detail="Unable to generate response. Please try again."
        )