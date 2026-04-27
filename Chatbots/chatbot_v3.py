from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
from dotenv import load_dotenv
load_dotenv()

model = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.7)

chat_history = [SystemMessage("you are a helpful assistant. Always respond in a concise manner.")]
while True:
    user_input = input("You: ")
    chat_history.append(HumanMessage(user_input))
    if user_input.lower() in ["exit", "quit", "bye"]:
        print("Chatbot: Goodbye!")
        break
    response = model.invoke(chat_history)
    chat_history.append(AIMessage(response.content))
    print(f"Chatbot: {response.content}")
 
print(chat_history)