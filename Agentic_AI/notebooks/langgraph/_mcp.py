import asyncio
from typing import TypedDict, Annotated
from warnings import filterwarnings
from dotenv import load_dotenv

from langchain_core.messages import BaseMessage, HumanMessage
from langchain_mistralai import ChatMistralAI
from langchain_mcp_adapters.client import MultiServerMCPClient

from langgraph.graph import StateGraph, START
from langgraph.graph.message import add_messages
from langgraph.prebuilt import ToolNode, tools_condition

filterwarnings("ignore")
load_dotenv()


# ==========================
# LLM
# ==========================

llm = ChatMistralAI(
    model="mistral-large-latest",
    temperature=0.3,
    streaming=True,
)


# ==========================
# MCP Client
# ==========================

client = MultiServerMCPClient(
    {
        "calculator": {
            "transport": "streamable_http",
            "url": "https://calculator-serverr.fastmcp.app/mcp",
        },
        "expense": {
            "transport": "streamable_http",
            "url": "https://xptracker-server.fastmcp.app/mcp",
        },
    }
)


# ==========================
# State
# ==========================

class ChatState(TypedDict):
    messages: Annotated[list[BaseMessage], add_messages]


# ==========================
# Build Graph
# ==========================

async def build_graph():

    tools = await client.get_tools()

    print("\nLoaded Tools")
    for tool in tools:
        print(tool.name)

    llm_with_tools = llm.bind_tools(tools)

    async def chatbot(state: ChatState):
        response = await llm_with_tools.ainvoke(state["messages"])
        return {"messages": [response]}

    graph = StateGraph(ChatState)

    graph.add_node("chatbot", chatbot)
    graph.add_node("tools", ToolNode(tools))

    graph.add_edge(START, "chatbot")

    graph.add_conditional_edges(
        "chatbot",
        tools_condition,
    )

    graph.add_edge("tools", "chatbot")

    return graph.compile()


# ==========================
# Main
# ==========================

async def main():

    chatbot = await build_graph()

    result = await chatbot.ainvoke(
        {
            "messages": [
                HumanMessage(
                    content="Give detailed weather forecasting report for Noida, Delhi, Gurgaon, Mainpuri and Agra with comparison."
                )
            ]
        }
    )

    print("\nWeather Response\n")
    print(result["messages"][-1].content)

    result = await chatbot.ainvoke(
        {
            "messages": [
                HumanMessage(
                    content="Add my spending of ₹8000 for August and give detailed analysis."
                )
            ]
        }
    )

    print("\nExpense Response\n")
    print(result["messages"][-1].content)


if __name__ == "__main__":
    asyncio.run(main())