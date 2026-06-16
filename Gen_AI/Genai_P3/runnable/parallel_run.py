from dotenv import load_dotenv
load_dotenv()

from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel,RunnableLambda

# Component 
model = ChatMistralAI(model="mistral-small-2506")
parser = StrOutputParser()

# Different Prompts 
short_prompt = ChatPromptTemplate.from_template(
    "Explain {topic} in 10-20 lines"
)

detailed_prompt = ChatPromptTemplate.from_template(
    "Explain {topic} in detailed version"
)

# Input 
topic = "Explain AIML role in tech jobs and it is worthi to get it job as a fresher candidate todays scenario"

chain = RunnableParallel({
    "short" :RunnableLambda(lambda x :x['short']) |short_prompt | model | parser ,
    "detailed" :RunnableLambda(lambda x: x['detailed']) |detailed_prompt |model |parser
})

result = chain.invoke({
    "short":{"topic":"is it possible to get it job in AIML roles"},
    "detailed":{"topic":"Explain AIML role in tech jobs and it is worthi to get it job as a fresher candidate todays scenario"}
})

print(result["short"])
print(result["detailed"])