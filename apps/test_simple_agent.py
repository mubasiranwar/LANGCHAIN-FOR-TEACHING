from langchain_openai import ChatOpenAI
from langchain.agents import create_agent
from langchain.tools import tool
from dotenv import load_dotenv
import os
import json

load_dotenv()

model = ChatOpenAI(model="gpt-4-0613", temperature=0.7)

@tool
def simple_add(a: int, b: int) -> int:
    """Add two numbers together."""
    return a + b

agent = create_agent(
    tools=[simple_add],
    model=model,
    system_prompt="You are a helpful math assistant."
)

if __name__ == "__main__":
    try:
        print("Testing with simple math query...")
        result = agent.invoke({"input": "What is 5 plus 3?"})
        print("Result type:", type(result))
        print("Result keys:", result.keys() if hasattr(result, 'keys') else "N/A")
        print("Full result:", result)
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()
