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

chain = prompt1 | model | parser

parallel_chain = RunnableParallel({
    'tweet': RunnablePassthrough(),
    'word_count': RunnableLambda(lambda x: len(x.split()))
}) 

final_chain = chain | parallel_chain
result = final_chain.invoke({"topic": "Future of AI"})

print(f"Tweet: {result['tweet']}")
print(f"Word Count: {result['word_count']}")