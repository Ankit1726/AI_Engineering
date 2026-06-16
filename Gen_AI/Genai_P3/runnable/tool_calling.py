from dotenv import load_dotenv
load_dotenv()
from langchain_mistralai import ChatMistralAI
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from rich import print

# 1. Define tool
@tool
def get_text_length(text: str) -> int:
    """Returns the number of characters in a given text"""
    return len(text)

tools = {
    "get_text_length": get_text_length
}

# 2. Create LLM and bind tools
llm = ChatMistralAI(model="mistral-small-2506")
llm_with_tool = llm.bind_tools(
    [get_text_length],
    tool_choice="any"
)

# 3. Build initial message
messages = []
prompt = input("You: ")
messages.append(HumanMessage(f'What is the character length of this text: "{prompt}"'))

# 4. First LLM call — may or may not call a tool
result = llm_with_tool.invoke(messages)
messages.append(result)
print(result.tool_calls) 
print(result.content)

# 5. If tool was called, run it and get final answer
if result.tool_calls:
    tool_name = result.tool_calls[0]["name"]
    tool_message = tools[tool_name].invoke(result.tool_calls[0])
    print(tool_message)
    messages.append(tool_message)

    # Second call — now model has the tool result
    result = llm_with_tool.invoke(messages)
    print("Final:", result.content) 

print(result.content)

# isko badal kar
if result.content:
    print(result.content)
else:
    print(f"Text length: {tool_message.content} characters")