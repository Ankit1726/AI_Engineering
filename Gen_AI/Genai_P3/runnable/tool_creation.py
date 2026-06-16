from langchain.tools import tool


@tool
def get_greeting(name: str) -> str:
    """
    Generate a greeting message for a user.
    """
    return f"Hello {name}, Welcome to the AI world"


# Invoke Tool
result = get_greeting.invoke({"name": "Ankit"})
print("Tool Output:")
print(result)

print("\nTool Name:")
print(get_greeting.name)

print("\nTool Description:")
print(get_greeting.description)

print("\nTool Arguments:")
print(get_greeting.args)