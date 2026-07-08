from langgraph.graph import StateGraph, START, END
from langgraph.prebuilt import ToolNode, tools_condition
from langgraph.checkpoint.sqlite import SqliteSaver
from langgraph.graph.message import add_messages

from langchain_core.messages import BaseMessage, SystemMessage
from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from langchain_groq import ChatGroq
from langchain_tavily import TavilySearch
from langchain_core.tools import tool
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

from typing import TypedDict, Annotated
import sqlite3
import os

from src.tool import calculator, get_current_weather, get_stock_price
from dotenv import load_dotenv

load_dotenv()


# LLM
llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.7)

LLM = ChatGroq(model="openai/gpt-oss-120b", temperature=0)

# Embedding Model
embeddings = GoogleGenerativeAIEmbeddings(model="gemini-embedding-001")

# Shared path for the FAISS vector store used by both retrieval and ingestion
FAISS_DB_PATH = "faiss_db"


# Retriver
def get_retriever():
    vector_store = FAISS.load_local(
        folder_path=FAISS_DB_PATH,
        embeddings=embeddings,
        allow_dangerous_deserialization=True,
    )

    retriever = vector_store.as_retriever(
        search_type="similarity", search_kwargs={"k": 3}
    )
    return retriever


# RAG Tool
@tool
def rag_tool(query: str) -> str:
    """
    - Retrieve relevant information from the PDF document.

    - Use this tool when the user asks factual or conceptual questions
    - that may be answered using the stored PDF documents.

    - Args:
        query: The question or search query used to retrieve PDF content.
    """
    try:
        retriever = get_retriever()
    except Exception:
        return (
            "No PDF has been uploaded and indexed yet. "
            "Ask the user to upload a PDF before answering document questions."
        )

    documents = retriever.invoke(query)

    if not documents:
        return "no related information found in provided resource..!"

    formatted_docs = []

    for index, document in enumerate(documents, start=1):
        source = document.metadata.get("source", "unknown source")
        page = document.metadata.get("page", "unknown page")

        formatted_docs.append(
            f"Document {index}\n"
            f"Source: {source}\n"
            f"Page: {page}\n"
            f"Content: {document.page_content}"
        )

    return "\n\n".join(formatted_docs)


# PDF Ingestion (RAG Upload)
def ingest_rag_document(pdf_path: str) -> int:
    """
    Ingest a PDF into the FAISS vector store so `rag_tool` can retrieve it.

    Args:
        pdf_path: Local filesystem path to the PDF file to ingest.

    Returns:
        The number of chunks that were embedded and stored.
    """
    loader = PyPDFLoader(pdf_path)
    documents = loader.load()

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=70,
    )
    chunks = splitter.split_documents(documents)
    if not chunks:
        return 0

    if os.path.exists(FAISS_DB_PATH):
        vector_store = FAISS.load_local(
            folder_path=FAISS_DB_PATH,
            embeddings=embeddings,
            allow_dangerous_deserialization=True,
        )
        vector_store.add_documents(chunks)
    else:
        vector_store = FAISS.from_documents(chunks, embeddings)

    vector_store.save_local(FAISS_DB_PATH)
    return len(chunks)


# Search Tool
search_tool = TavilySearch(max_results=5, topic="general", search_depth="advanced")

tools = [search_tool, calculator, get_current_weather, get_stock_price]

LLM_Tools = LLM.bind_tools(tools)


# Define State
class ChatState(TypedDict):
    messages: Annotated[list[BaseMessage], add_messages]


# Define Node
def chat_node(state: ChatState):
    """LLM node that can answer directly or call an appropriate tool."""

    system_message = SystemMessage(
        content=(
            "You are a helpful Agentic Chatbot with access to several tools.\n\n"
            "Tool usage instructions:\n"
            "- Use `rag_tool` for questions about the uploaded PDF or document. "
            "Always retrieve relevant document content before answering PDF-related questions.\n"
            "- Use `search_tool` for current events, recent information, or information "
            "that requires an internet search.\n"
            "- Use `calculator` for mathematical calculations. Do not calculate complex "
            "expressions manually when the calculator is available.\n"
            "- Use `get_stock_price` when the user asks for the current price of a stock.\n"
            "- Use `purchase_stock` when the user wants to purchase a stock.\n"
            "- Use `get_current_weather` when the user asks about current weather for a location.\n\n"
            "Answer general questions directly when no tool is required. "
            "Do not invent information from the uploaded document. "
            "If the user asks about a PDF but no document is available, ask them to upload a PDF. "
            "After receiving a tool result, provide a clear and helpful final answer."
        )
    )
    messages = [system_message, *state["messages"]]
    response = LLM_Tools.invoke(messages)
    return {"messages": [response]}


tool_node = ToolNode(tools)

# Checkpoints
conn = sqlite3.connect(database="bot_data.db", check_same_thread=False)
checkpoint = SqliteSaver(conn)

# Define Graph
graph = StateGraph(ChatState)

# add nodes
graph.add_node("chat_node", chat_node)
graph.add_node("tools", tool_node)

# add edges
graph.add_edge(START, "chat_node")
graph.add_conditional_edges("chat_node", tools_condition)
graph.add_edge("tools", "chat_node")

chatbot = graph.compile(checkpointer=checkpoint)


# Helper functions for Streamlit frontend
def get_all_threads():
    all_threads = set()
    for ckpt in checkpoint.list(None):
        all_threads.add(ckpt.config["configurable"]["thread_id"])
    return list(all_threads)
