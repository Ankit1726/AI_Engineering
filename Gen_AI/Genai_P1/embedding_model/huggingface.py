from langchain_huggingface import HuggingFaceEmbeddings

embedding = HuggingFaceEmbeddings(
    model_name="all-MiniLM-L6-v2"
)

texts = [
    "Hello this is Akarsh Vyas",
    "Hello your name is YouTube",
    "And you all are very beautiful"
]

vectors = embedding.embed_documents(texts)

print(len(vectors))
print(len(vectors[0]))