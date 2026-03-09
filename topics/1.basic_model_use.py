from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()


llm=ChatOpenAI(model="gpt-3.5-turbo", temperature=0.9)

response=llm.invoke("What is the capital of Pakistan?")
print(response.content)