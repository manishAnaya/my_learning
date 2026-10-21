# custom_tools are created when we define the logic on our own
# like calling API
# for encapsulating business logic
# for interacting LLm to datbase or Product

# You can create tool using 3 methods
# 1. Using @tool in function
# 2. Using Pydantic -> BaseModel and StructuredTool

from langchain_community.tools import DuckDuckGoSearchRun
from langchain_community.tools import tool

search_tool = DuckDuckGoSearchRun()

# print(search_tool.name)
# print(search_tool.description)
# print(search_tool.args)

@tool
def multiply(a: int, b: int) -> int:
    """This tool helps in multiplying the provided numbers"""
    return a * b

# result = multiply.invoke({'a': 4, 'b': 8})

# print(result)

# print(multiply.name)
# print(multiply.description)
# print(multiply.args)


from langchain_community.tools import StructuredTool
from pydantic import BaseModel, Field

class MultiplyInput(BaseModel):
    a: int = Field(required = True, description='First number')
    b: int = Field(required = True, description='Second number')

def multiply_func(a: int, b: int) -> int:
    return a * b

multiply_tool = StructuredTool.from_function(
    func=multiply_func, 
    name='multiply', 
    description='This tool helps in multiplying two numbers',
    args_schema=MultiplyInput
)

result = multiply_tool.invoke({'a': 4, 'b': 9})

print(result)

print(multiply.name)
print(multiply.description)
print(multiply.args)