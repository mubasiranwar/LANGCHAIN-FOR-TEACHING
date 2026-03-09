from langchain_openai import ChatOpenAI
from langchain.agents import create_agent
from langchain.tools import tool
from dotenv import load_dotenv
import os

load_dotenv()

# Check if API keys are set
if not os.getenv("OPENAI_API_KEY"):
    print("Error: OPENAI_API_KEY not set in environment")
    exit(1)

if not os.getenv("SERPER_API_KEY"):
    print("Error: SERPER_API_KEY not set in environment")
    exit(1)

model = ChatOpenAI(model="gpt-4-0613", temperature=0.7)

from langchain_community.utilities import GoogleSerperAPIWrapper

# Properly wrap the Google search as a tool
search_api = GoogleSerperAPIWrapper()

@tool
def google_search(query: str) -> str:
    """Search the internet for information about the query."""
    return search_api.run(query)

agent = create_agent(
    tools=[google_search],
    model=model,
    system_prompt="You are a helpful assistant that answers questions using Google Search. If you don't know the answer, say you don't know."
)
#adding agent execution loop
if __name__ == "__main__":
    try:
        # Test with a sample query
        test_query = "What is Python programming?"
        print(f"Query: {test_query}")
        result = agent.invoke({"input": test_query})
        print(f"Response: {result['messages'][-1].content}")
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()

