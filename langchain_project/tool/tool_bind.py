
from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, ToolMessage
from langchain_core.tools import tool

load_dotenv()

llm = ChatGroq(model="openai/gpt-oss-120b")

@tool
def addition(a: int, b: int) -> int:
    """Adds two given numbers."""
    return a + b

@tool
def multiplication(a: int, b: int) -> int:
    """Multiplies two given numbers."""
    return a * b

tools = [addition, multiplication]
tools_by_name = {t.name: t for t in tools}
print(tools_by_name)
llm_with_tools = llm.bind_tools(
    tools,
    tool_choice="addition"
)

messages = [
    HumanMessage(content="Help me add 4 and 15")
]

# Step 1: Ask the LLM which tool to call
ai_message = llm_with_tools.invoke(messages)
messages.append(ai_message)

# Step 2: Execute the requested tool
for tool_call in ai_message.tool_calls:
    selected_tool = tools_by_name[tool_call["name"]]

    result = selected_tool.invoke(tool_call["args"])

    # Step 3: Return the actual result to the conversation
    tool_message = ToolMessage(
        content=str(result),
        tool_call_id=tool_call["id"]
    )

    messages.append(tool_message)

# Step 4: Ask the LLM to generate the final answer
final_response = llm.invoke(messages)

print(final_response.content)
