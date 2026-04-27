from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()

chat_template = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant. Always respond in a concise manner."),
    ("human", "What is the capital of {country}?"),
    MessagesPlaceholder('chat_history')
])
chat_history = []
with open("Prompts/chat_history.txt", "r") as f:
    chat_history.extend(f.readlines())

print(chat_history)
#model = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.7)
#response = model.invoke(chat_template.format_prompt(country="France", chat_history=chat_history).to_messages())

#output:
'''
['HumanMessage(content="I want to request a refund for my order #12345.")\n', 
'AIMessage(content="Your refund request for order #12345 has been initiated. It will be processed in 3-5 business days.")']
'''