from langchain.agents import create_agent
from langchain_groq import ChatGroq
from langchain_core.tools import tool
from dotenv import load_dotenv

load_dotenv()

llm = ChatGroq(model="openai/gpt-oss-120b")

@tool
def addition(a: int, b: int) -> int:
    """Add two numbers."""
    return a + b


@tool
def multiplication(a: int, b: int) -> int:
    """Multiply two numbers."""
    return a * b


@tool
def company_policy_lookup(query: str) -> str:
    """company policy information."""

    policies = {
        "leave": "Employees receive 20 paid leaves per year.",
        "work from home": "Employees can work from home 2 days per week.",
        "working hours": "Working hours are 9 AM to 6 PM."
    }

    query = query.lower()

    for key, value in policies.items():
        if key in query:
            return value

    return "No matching company policy found."


tools = [
    addition,
    multiplication,
    company_policy_lookup
]

agent = create_agent(
    model=llm,
    tools=tools,
    system_prompt="You are a helpful assistant. Use tools when needed."
)

print("AI Agent Assistant")
print("Type 'exit' to quit.")

while True:
    user_input = input("\nYou: ")

    if user_input.lower() == 'exit':
        print("Goodbye!")
        break

    response = agent.invoke({
        "messages": {"role": "user", "content": user_input}
    })

    print("Assistant:", response["messages"][-1].content)