# chatbot with memory example, without message types, just simple dicts, 
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()
model = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.7)
chat_history = []
while True:
    user_input = input("You: ")
    chat_history.append({"user": user_input})
    if user_input.lower() in ["exit", "quit"]:
        print("Chatbot: Goodbye!")
        break
    response = model.invoke(chat_history)
    chat_history.append({"assistant": response.content})
    print(f"Chatbot: {response.content}")
