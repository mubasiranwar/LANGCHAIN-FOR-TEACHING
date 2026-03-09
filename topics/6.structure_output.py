from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()

llm=ChatOpenAI(model="gpt-3.5-turbo", temperature=0.9)

from pydantic import BaseModel, Field
from typing import List

#Example of structured output using pydantic
class Person(BaseModel):
    name: str = Field(..., description="The person's name")
    age: int = Field(..., description="The person's age")
    hobbies: List[str] = Field(..., description="A list of the person's hobbies")
# Define a prompt to generate structured output
prompt = "My name is mubasir anwar and my age is 25 and my hobbies are coding, reading, and traveling. Please provide this information in a structured format."
# Get structured output from the LLM
person_info=llm.with_structured_output(Person)
response=person_info.invoke(prompt)
print(response.name)
print(response.age)
print(response.hobbies) 
print(response.json())