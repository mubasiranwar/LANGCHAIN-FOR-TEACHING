from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
load_dotenv()


llm=ChatOpenAI(model="gpt-3.5-turbo", temperature=0.9)

prompt=ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant to help in understanding the {language} questions in oneline."),
    ("user", "{question}")
])

#prompt invoke
#print(prompt.format_messages(language="python", question="what is list?"))

#---->we can see that prompt and llm are runnable b/c we use same funation to call it

response=llm.invoke(prompt.format_messages(language="python", question="what is list?"))# As we use the output of the prompt as input to the llm, we can see that both are runnable and we can use them together.
print(response.content)

    