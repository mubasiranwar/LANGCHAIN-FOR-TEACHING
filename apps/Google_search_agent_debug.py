from langchain_openai import ChatOpenAI
from langchain.agents import create_agent
from langchain.tools import tool
from dotenv import load_dotenv
import os
import sys

load_dotenv()

# Check if API keys are set
if not os.getenv("OPENAI_API_KEY"):
    print("Error: OPENAI_API_KEY not set in environment")
    exit(1)

if not os.getenv("SERPER_API_KEY"):
    print("Error: SERPER_API_KEY not set in environment")
    exit(1)

print("Creating model...", file=sys.stderr, flush=True)
model = ChatOpenAI(model="gpt-4-0613", temperature=0.7)

from langchain_community.utilities import GoogleSerperAPIWrapper

print("Creating search API...", file=sys.stderr, flush=True)
search_api = GoogleSerperAPIWrapper()

@tool
def google_search(query: str) -> str:
    """Search the internet for information about the query."""
    print(f"[TOOL] Searching for: {query}", file=sys.stderr, flush=True)
    result = search_api.run(query)
    print(f"[TOOL] Result: {result[:100]}", file=sys.stderr, flush=True)
    return result

print("Creating agent...", file=sys.stderr, flush=True)
agent = create_agent(
    tools=[google_search],
    model=model,
    system_prompt="You are a helpful assistant that answers questions using Google Search. If you don't know the answer, say you don't know."
)

print("Agent created successfully!", file=sys.stderr, flush=True)

if __name__ == "__main__":
    try:
        test_query = "What is Python programming?"
        print(f"Query: {test_query}")
        print(f"[DEBUG] Invoking agent...", file=sys.stderr, flush=True)
        
        result = agent.invoke({"input": test_query})
        
        print(f"[DEBUG] Agent returned", file=sys.stderr, flush=True)
        print(f"Response: {result.get('output', 'No output key')}")
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()
