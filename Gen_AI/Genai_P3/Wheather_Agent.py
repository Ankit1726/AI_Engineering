from dotenv import load_dotenv
import os
import requests
load_dotenv()

from langchain_mistralai import ChatMistralAI
from langchain.tools import tool
from langchain_core.messages import HumanMessage, ToolMessage
from tavily import TavilyClient
from rich import print

# TOOLS
@tool
def get_weather(city: str) -> str:
    """Get current weather of a city in India"""
    api_key = os.getenv("OPENWEATHER_API_KEY")
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city},IN&appid={api_key}&units=metric"
    
    data = requests.get(url).json()
    
    if str(data.get("cod")) != "200":
        return f"Error: {data.get('message', 'Could not fetch weather')}"
    
    temp = data["main"]["temp"]
    desc = data["weather"][0]["description"]
    return f"Weather in {city}: {desc}, {temp}°C"


@tool
def get_news(city: str) -> str:
    """Get latest news about a city"""
    client = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))
    response = client.search(
        query=f"latest news in {city}",
        search_depth="basic",
        max_results=3
    )
    
    results = response.get("results", [])
    if not results:
        return f"No news found for {city}"
    
    news_list = []
    for r in results:
        title = r.get("title", "No title")
        url   = r.get("url", "")
        snip  = r.get("content", "")[:100]
        news_list.append(f"- {title}\n  {url}\n  {snip}...")
    
    return f"Latest news in {city}:\n\n" + "\n\n".join(news_list)

# TOOL REGISTRY
tools = {
    "get_weather": get_weather,
    "get_news"   : get_news,
}

# LLM SETUP
llm = ChatMistralAI(model="mistral-small-2506")
llm_with_tools = llm.bind_tools(list(tools.values()))



# HUMAN APPROVAL (manual middleware)
def ask_approval(tool_name: str) -> bool:
    confirm = input(f"\n  Agent wants to call '{tool_name}'. Approve? (yes/no): ")
    return confirm.strip().lower() == "yes"

# AGENT LOOP
def run_agent(user_input: str):
    messages = [HumanMessage(user_input)]
    
    while True:
        result = llm_with_tools.invoke(messages)
        messages.append(result)
        
        # No tool call — final answer ready
        if not result.tool_calls:
            return result.content
        
        # Tool calls — handle each one
        for call in result.tool_calls:
            tool_name = call["name"]
            tool_args = call["args"]
            tool_id   = call["id"]
            
            print(f"\n[bold yellow]Tool call:[/bold yellow] {tool_name}({tool_args})")
            
            # Human approval check
            if ask_approval(tool_name):
                tool_result = tools[tool_name].invoke(call)
                print(f"[bold green]Tool result:[/bold green] {tool_result}")
            else:
                tool_result = "Tool call denied by user."
                print("[bold red]Denied.[/bold red]")
            
            # Add tool result to messages
            messages.append(ToolMessage(
                content=str(tool_result),
                tool_call_id=tool_id
            ))



# MAIN
print("[bold]City Agent | type 'exit' to quit[/bold]\n")

while True:
    user_input = input("You: ").strip()
    
    if user_input.lower() == "exit":
        print("Bye!")
        break
    
    if not user_input:
        continue
    
    response = run_agent(user_input)
    print(f"\n[bold cyan]Bot:[/bold cyan] {response}\n")