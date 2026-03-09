from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()

llm=ChatOpenAI(model="gpt-3.5-turbo", temperature=0.9)

# prompt=[
    
#     ("system", "You are a helpful assistant that translates English to Urdu."),
#     ("user", "What is your name?")
# ]

prompt=[
    
    {"role": "system", "content": "You are a helpful assistant to help in understanding the python questions in one line."},
    {"role": "user", "content": "what is list?"}
]


response=llm.invoke()
print(response.content)

