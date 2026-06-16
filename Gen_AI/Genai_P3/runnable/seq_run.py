from dotenv import load_dotenv
load_dotenv()

from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# Prompt Template
prompt = ChatPromptTemplate.from_template(
    "Explain {topic} in simple words"
)

# Model
model = ChatMistralAI(model="mistral-small-2506")

# Output Parser 
parser = StrOutputParser()

# using chain method
chain = prompt | model | parser

result = chain.invoke("Expalin Future Scope of AIML Job for fresher")
print(result)