from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
documents = ["Hello world, I'm Gaurav Rai",
    "I am a software engineer with experience in Python."]
result = embedding.embed_documents(documents)

print(str(result))