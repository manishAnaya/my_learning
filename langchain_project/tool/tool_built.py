# from langchain_community.tools import DuckDuckGoSearchRun

# search_tool = DuckDuckGoSearchRun()

# res = search_tool.invoke('what is todays news')

# print(res)

from langchain_community.tools import ShellTool

shell = ShellTool()

res = shell.invoke('whoami')

print(res)

