from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv 
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="openai/gpt-oss-120b",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)

class Person(BaseModel):
    name: str = Field(description="The person's name")
    age: int = Field(gt = 18, description="The person's age")
    city: str = Field(description="The city where the person lives")

parse = PydanticOutputParser(pydantic_object=Person)


template = PromptTemplate(
    template="Generate name, age and city of a frictional {place} person {format_instructions}",
    input_variables=['place'],
    partial_variables={"format_instructions": parse.get_format_instructions()}  
)

chain = template | model | parse
result = chain.invoke({"place": "Dehradun"}) 
print(result)

#output:
# name='Arjun Singh' age=27 city='Dehradun'
