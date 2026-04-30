from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
load_dotenv()


model = ChatOpenAI(model="gpt-3.5-turbo")

parser = StrOutputParser()

prompt_template = PromptTemplate(
    template="write 3 facts about the {topic}",
    input_variables=['topic'],
)
chain = prompt_template | model | parser
result = chain.invoke({"topic": "Black holes"}) 
print(result)