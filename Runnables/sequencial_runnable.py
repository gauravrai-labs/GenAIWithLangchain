from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableSequence, RunnableBranch, RunnableLambda, RunnableParallel, RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

prompt1 = PromptTemplate(
    template="write 50 word description of {topic}",
    input_variables=["topic"]
)

# llm = HuggingFaceEndpoint(model="openai/gpt-oss-120b",
#                           task="text-generation"
#                           )
# model = ChatHuggingFace(llm=llm)
model = ChatOpenAI()

parser = str = StrOutputParser()

prompt2 = PromptTemplate(
    template = "write 10 words summary of {description}",
    input_variables=["description"]
)

chain = RunnableSequence(prompt1, model, parser, prompt2, model, parser)

result = chain.invoke({"topic": "the benefits of meditation"})

print(result)