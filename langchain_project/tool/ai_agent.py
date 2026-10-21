
# from dotenv import load_dotenv
# from langchain_groq import ChatGroq
# from langchain_community.tools import DuckDuckGoSearchRun
# from langchain_core.prompts import PromptTemplate
# from langchain.agents import create_react_agent, AgentExecutor

# load_dotenv()

# # Initialize LLM
# llm = ChatGroq(model="openai/gpt-oss-120b")

# # Define the prompt
# prompt = PromptTemplate.from_template("""
# Answer the question using the tools below.

# You have access to these tools:
# {tools}

# Use this format:
# Question: the question
# Thought: decide what information is needed
# Action: one of [{tool_names}]
# Action Input: the input for the tool
# Observation: the tool result
# ...repeat as needed...
# Thought: I know the answer
# Final Answer: the answer

# Question: {input}
# Thought:{agent_scratchpad}
# """)

# # Initialize search tool
# search_tool = DuckDuckGoSearchRun()
# tools = [search_tool]

# # Create ReAct agent
# agent = create_react_agent(
#     llm=llm,
#     tools=tools,
#     prompt=prompt
# )

# # Create agent executor
# executor = AgentExecutor(
#     agent=agent,
#     tools=tools,
#     verbose=True,
#     handle_parsing_errors=True,
#     max_iterations=5
# )

# # Run the agent
# response = executor.invoke({
#     "input": "Give three ways to travel from Pune to Goa."
# })

# print(response["output"])



from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_community.tools import DuckDuckGoSearchRun
from langchain.agents import create_agent

load_dotenv()

llm = ChatGroq(model="openai/gpt-oss-120b")

search_tool = DuckDuckGoSearchRun()
tools = [search_tool]

agent = create_agent(
    model=llm,
    tools=tools
)

response = agent.invoke({
    "messages": [
        {"role": "user", "content": "Three ways to travel from Pune to Goa"}
    ]
})

print(response["messages"][-1].content)
