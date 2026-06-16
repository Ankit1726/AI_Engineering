from dotenv import load_dotenv
load_dotenv()

import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_groq import ChatGroq
from langchain_mistralai import ChatMistralAI

model_1 = ChatGroq(
    model="qwen/qwen3-32b",
    api_key=os.getenv("GROQ_API_KEY")
)

model_2 = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash-lite",
    api_key=os.getenv("GEMINI_API_KEY")
)

model_3 = ChatMistralAI(
    model = "mistral-small-2506",temperature=0.9,
    api_key=os.getenv("MISTRAL_API_KEY")
)

response_1 = model_1.invoke("Explain Deep Learning..!")
print(f"Response_1 : {response_1.content}")
print("-------------------------------")

response_2 = model_2.invoke("Explain Machine Learning..!")
print(f"Response_2 : {response_2.content}")
print("-------------------------------")

response_3 = model_3.invoke("write a poem on AI")
print(f"Response_3 : {response_3.content}")
