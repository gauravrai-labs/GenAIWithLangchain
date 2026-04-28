from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import TypedDict, Annotated

load_dotenv()

class review(TypedDict):
    summarize: Annotated[str, "A brief summary of the review"]
    sentiment: Annotated[str, "The sentiment of the review"]

model = ChatOpenAI()

structured_model = model.with_structured_output(review)
response = structured_model.invoke("The movie was fantastic! I loved the storyline and the acting was superb. Highly recommend it.")
print(response)
#output:
'''
{'summarize': 'The movie was fantastic with a great storyline and superb acting.', 'sentiment': 'Positive'}
'''
