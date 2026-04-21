from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

modal = ChatGoogleGenerativeAI(model='gemini-2.0-flash')

print(modal.invoke("what is the capital of India?"))