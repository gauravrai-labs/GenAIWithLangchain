
## StructuredOutputParser is deprecated, but it is still useful to understand how it works and its advantages and disadvantages.

from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv 
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StructuredOutputParser, ResponseSchema

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="openai/gpt-oss-120b",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)

schema = [
    ResponseSchema(name="fact1", description="fact1 about black holes"),
    ResponseSchema(name="fact2", description="fact2 about black holes"),
    ResponseSchema(name="fact3", description="fact3 about black holes"),
]

parse = StructuredOutputParser.from_response_schemas(schema)

template = PromptTemplate(
    template="write 3 facts about the {topic} in the following format {format_instructions}",
    input_variables=['topic'],
    partial_variables={"format_instructions": parse.get_format_instructions()}  
)

chain = template | model | parse
result = chain.invoke({"topic": "Black holes"}) 
print(result)

# Disadvantages of structured output parsing:
# 1. Complexity: Structured output parsing can be more complex to implement and maintain compared to unstructured parsing. It requires defining a clear schema and ensuring that the output from the model adheres to that schema, which can be challenging.
# 2. Data validation is not possible.
