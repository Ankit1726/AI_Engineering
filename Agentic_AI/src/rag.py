import os
from langchain_core.tools import tool
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import FAISS

from dotenv import load_dotenv
load_dotenv()

FAISS_DB_PATH = "faiss_db"

embeddings = GoogleGenerativeAIEmbeddings(
    model="models/embedding-001",
)


# Retriever
def get_retriever():
    """
    Load the FAISS vector store and return an MMR retriever.
    """

    if not os.path.exists(FAISS_DB_PATH):
        raise FileNotFoundError("No vector database found.")

    vector_store = FAISS.load_local(
        folder_path=FAISS_DB_PATH,
        embeddings=embeddings,
        allow_dangerous_deserialization=True,
    )

    return vector_store.as_retriever(
        search_type="mmr",
        search_kwargs={
            "k": 4,
            "fetch_k": 20,
            "lambda_mult": 0.7,
        },
    )


def ingest_rag_document(pdf_path: str) -> int:
    """
    - Ingest a PDF into the FAISS vector store.

    - Args:
        pdf_path: Path to PDF.

    - Returns:
        Number of chunks stored.
    """

    if not os.path.exists(pdf_path):
        raise FileNotFoundError(f"PDF not found: {pdf_path}")

    loader = PyPDFLoader(pdf_path)
    documents = loader.load()

    if not documents:
        raise ValueError("No readable text found in PDF.")

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=150,
    )

    chunks = splitter.split_documents(documents)

    if not chunks:
        raise ValueError("Chunk generation failed.")

    # Add clean metadata
    filename = os.path.basename(pdf_path)

    for chunk in chunks:
        chunk.metadata["source"] = filename
        chunk.metadata["page"] = chunk.metadata.get("page", "Unknown")

    # Load existing DB or create new one
    if os.path.exists(FAISS_DB_PATH):
        vector_store = FAISS.load_local(
            folder_path=FAISS_DB_PATH,
            embeddings=embeddings,
            allow_dangerous_deserialization=True,
        )

        vector_store.add_documents(chunks)

    else:
        vector_store = FAISS.from_documents(
            chunks,
            embeddings,
        )

    vector_store.save_local(FAISS_DB_PATH)
    print(f"Indexed {len(chunks)} chunks from {filename}")
    return len(chunks)


# RAG Tool
@tool
def rag_tool(query: str) -> str:
    """
    Retrieve relevant information from uploaded PDFs.

    Use this tool whenever the user asks questions
    about uploaded PDF documents.
    """

    try:
        retriever = get_retriever()

    except FileNotFoundError:
        return (
            "No PDF has been uploaded and indexed yet.\n" "Please upload a PDF first."
        )

    except Exception as e:
        return f"Retriever Error: {str(e)}"

    try:
        documents = retriever.invoke(query)

    except Exception as e:
        return f"Retrieval Error: {str(e)}"

    if not documents:
        return "No relevant information found in the uploaded PDF."

    formatted_docs = []

    for i, doc in enumerate(documents, start=1):
        source = doc.metadata.get("source", "Unknown")
        page = doc.metadata.get("page", "Unknown")

        formatted_docs.append(
            f"Document {i}\n"
            f"Source : {source}\n"
            f"Page   : {page}\n\n"
            f"{doc.page_content}"
        )

    return "\n\n" + "=" * 80 + "\n\n".join(formatted_docs)
