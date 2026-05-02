from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableSequence, RunnableBranch, RunnableLambda, RunnableParallel, RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

prompt1 = PromptTemplate(
    template="write about {topic}",
    input_variables=["topic"]
)

model = ChatOpenAI()

parser = str = StrOutputParser()

prompt2 = PromptTemplate(
    template = "write 20 words summary about {description}",
    input_variables=["description"]
)

chain = prompt1 | model | parser

branch_chain = RunnableBranch(
    (lambda x: len(x.split())>20, prompt2 | model | parser),
    RunnablePassthrough()
)

final_chain = chain | branch_chain

result = final_chain.invoke({"topic": "Future of AI"})

print(result)
