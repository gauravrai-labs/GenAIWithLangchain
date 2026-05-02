from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableSequence, RunnableBranch, RunnableLambda, RunnableParallel, RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

prompt1 = PromptTemplate(
    template="write 50 word tweet about {topic}",
    input_variables=["topic"]
)

model = ChatOpenAI()

parser = str = StrOutputParser()

prompt2 = PromptTemplate(
    template = "write 50 word post for linkedin about {topic}",
    input_variables=["topic"]
)

parallel_chain = RunnableParallel({
    'tweet': prompt1 | model | parser,
    'LinkedIn': prompt2 | model | parser
})

result = parallel_chain.invoke({"topic": "Future of AI"})

print(result['tweet'])
print(result['LinkedIn'])
