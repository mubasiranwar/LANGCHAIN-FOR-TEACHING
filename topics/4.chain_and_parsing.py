from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser#it use for parsing the output of the llm and make it in string format

from dotenv import load_dotenv
load_dotenv()
pareser=StrOutputParser()

#user define runnable
def upper(text):
    return text.upper()

llm=ChatOpenAI(model="gpt-3.5-turbo", temperature=0.9)

prompt=ChatPromptTemplate.from_messages([
    {"role": "system", "content": "You are a helpful assistant to help in understanding the {language} questions in oneline."},
    {"role": "user", "content": "{question}"}
]
)

chain=prompt | llm | pareser | upper
print(chain.invoke({"language":"python", "question":"what is list?"}))

                                        
                                