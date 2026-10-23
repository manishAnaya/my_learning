from huggingface_hub import InferenceClient
from dotenv import load_dotenv
import os

load_dotenv()

HF_TOKEN = os.getenv('HF_TOKEN')

# It initializes the connection to a specific model hosted in hugging face server
client = InferenceClient(token=HF_TOKEN, provider='auto')

prompt = 'What is Machine Learning'

response = client.chat_completion(
    model="openai/gpt-oss-120b:fastest",
    messages=[
        {"role": "user", "content": prompt}
    ],
    max_tokens=150,
    temperature=0.7
)

print(response.choices[0].message.content)

