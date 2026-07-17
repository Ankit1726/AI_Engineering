from langchain_groq import ChatGroq
from mcp_use import MCPAgent,MCPClient
from pathlib import Path
import os,asyncio

from dotenv import load_dotenv
load_dotenv()

GROQ = os.getenv("GROQ_API_KEY")

async def run_memory_chat():
    """Run a chat using MCPAgent's built-in conversation memory.
    """

    config_file = config_file = Path(__file__).parent / "mcp.json"
    print("Initializing Chat..!")

    # Create MCP Client 
    client = MCPClient.from_config_file(config_file)
    llm = ChatGroq(model="llama-3.1-8b-instant")

    # Create Agent 
    agent = MCPAgent(
        llm=llm,
        client=client,
        max_steps=15,
        memory_enabled=True
    )
    print("\n===== Interactive MCP Chat =====")
    print("Type 'exit' or 'quit' to end the conversation")
    print("Type 'clear' to clear conversation history")
    print("=================================\n")

    try:
        while True:
            user_input = input("\nUser:")

            # Check for exit command
            if user_input.lower() in ["exit", "quit"]:
                print("Ending conversation...")
                break

            # Check for clear history command
            if user_input.lower() == "clear":
                agent.clear_conversation_history()
                print("Conversation history cleared.")
                continue

            # Get response from agent
            print("\nAssistant: ", end="", flush=True)

            try:
                # Run the agent with the user input (memory handling is automatic)
                response = await agent.run(user_input)
                print(response)
            
            except Exception as e:
                print(f"\nError: {e}")
    finally:
        if client and client.sessions:
            await client.close_all_sessions()


if __name__ == "__main__":
    asyncio.run(run_memory_chat())
