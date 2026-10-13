from langchain_core.messages import SystemMessage, HumanMessage
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv

load_dotenv()

# system_msg = SystemMessage(
#     content="""You are a professional YouTuber who helps creators grow their channels.
# Give practical, specific advice with clear next steps.
# """
# )

# human_msg = HumanMessage(
#     content="Please help me grow my channel, Raga Mind, where I post meditation music."
# )

# msgs = [system_msg, human_msg]

# model = ChatGroq(model='openai/gpt-oss-120b', temperature=0.6)

# res = model.invoke(msgs)

# print(res.content)


## Chat prompt

domain = input('Domain:')
query = input('Query:')

messages = ChatPromptTemplate.from_messages([
    ('system', f'''You are a professional {domain} who helps creators grow their channels.
# Give practical, specific advice with clear next steps'''),
    ('human', f'Please help me {query}')
])

prompt = messages.invoke({'domain': domain, 'query': query})

model = ChatGroq(model='openai/gpt-oss-120b', temperature=0.6)

res = model.invoke(prompt)

print(res.content)

# to decide to pick topic for my youtube channel