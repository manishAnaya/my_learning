from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_community.document_loaders import PyPDFLoader
from langchain_core.prompts import PromptTemplate
from langchain_classic.chains.summarize import load_summarize_chain
from langchain_text_splitters import RecursiveCharacterTextSplitter

load_dotenv()

model = ChatGroq(model='openai/gpt-oss-120b')

loader = PyPDFLoader('manish.pdf')

data = loader.load_and_split()

splitter = RecursiveCharacterTextSplitter(chunk_size=2000, chunk_overlap=200)

docs = splitter.split_documents(data)

prompt = PromptTemplate(template='''
Write a detailed summary of following text: \n {text}
''',    
input_variables=['text'])

initial_prompt = PromptTemplate(
    template='''
Write a concise summary of the following text: \n {text}
''',
input_variables=['text']
)

refine_prompt = PromptTemplate(
    template='''
Your current summary is {existing_answer}
Now refine and improve it using the following new text: {text}
Provide an updated improved summary that include important details from old and new text
''',
input_variables=['existing_answer', 'text']
)

## Stuff Summarization Chain

# chain = load_summarize_chain(llm=model, verbose=True, prompt=prompt)

# response = chain.run(docs)

# print(response)

## Map Reduce Summarization Chain

# chain = load_summarize_chain(llm=model, chain_type='map_reduce', verbose=True, map_prompt=prompt, combine_prompt=prompt)

# response = chain.run(docs)

# print(response)

## Refine Summarization Chain

chain = load_summarize_chain(llm=model, chain_type='refine', verbose=True, question_prompt=initial_prompt, refine_prompt=prompt)

response = chain.run(docs)

print(response)
