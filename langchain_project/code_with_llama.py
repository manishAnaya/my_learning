import requests
import json
import gradio as gr

url = 'http://localhost:11434/api/generate'

# Http request header

headers = {
    'content-Type': 'application/json'
}

history = []

def generate_response(prompt):
    history.append(prompt)
    final_prompt = '\n'.join(history)

    data = {
        'model': 'ManishCodes',
        'prompt': final_prompt,
        'stream': False
    }

    response = requests.post(url, json=data)

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f'Error: {response.text}')

interface = gr.Interface(
    fn=generate_response,
    inputs=gr.Textbox(lines=4, placeholder='Enter Your Question'),
    outputs='text'
)

interface.launch()