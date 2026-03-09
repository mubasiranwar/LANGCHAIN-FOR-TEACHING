from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from dotenv import load_dotenv
load_dotenv()


llm=ChatOpenAI(model="gpt-3.5-turbo", temperature=0.9)

# Store conversation history
messages = [SystemMessage(content="You are a helpful AI assistant.")]

while True:
    user_input = input("User: ")
    if user_input.lower() == "exit":
        print("Exiting the chatbot. Goodbye!👏")
        break
    
    # Add user message to history
    messages.append(HumanMessage(content=user_input))
    
    # Get response with full conversation history
    response = llm.invoke(messages)
    
    # Add assistant response to history
    messages.append(AIMessage(content=response.content))
    
    print("Bot:", response.content)
    
    
