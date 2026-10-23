from huggingface_hub import InferenceClient
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
import os

load_dotenv()

HF_TOKEN = os.getenv('HF_TOKEN')

# It initializes the connection to a specific model hosted in hugging face server
client = InferenceClient(token=HF_TOKEN, model='mistralai/Mistral-7B-Instruct-v0.3')

prompt = PromptTemplate(template="""
Question: {question}
Answer: Lets think step by step
""",
input_variables=['question']
)

final_prompt = prompt.format(
    question='Explain RAG in simple words'
)

response = client.chat_completion(
    model='mistralai/Mistral-7B-Instruct-v0.3',
    messages=[
        {"role": "user", "content": final_prompt}
    ],
    max_tokens=150,
    temperature=0.7
)

print(response.choices[0].message.content)

