from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

load_dotenv()

embedding = OpenAIEmbeddings(model="text-embedding-3-small", dimensions=32)

documents = [
    "Virat Kohli is an Indian cricketer known for his aggressive batting and leadership.",
    "MS Dhoni is a former Indian captain famous for his calm demeanor and finishing skills.",
    "Sachin Tendulkar, also known as the 'God of Cricket', holds many batting records.",
    "Rohit Sharma is known for his elegant batting and record-breaking double centuries.",
    "Jasprit Bumrah is an Indian fast bowler known for his unorthodox action and yorkers."
]

query1 = "Who is the best Indian cricketer?"

# Get embeddings for documents and query
doc_embeddings = embedding.embed_documents(documents)
query1_embedding = embedding.embed_query(query1)  

# Compute cosine similarity between query and each document
similarity1 = cosine_similarity([query1_embedding], doc_embeddings)[0] 

# Get the index of the most similar document
index1, score1 = sorted(list(enumerate(similarity1)), key=lambda x: x[1])[-1]

print(f"Query: '{query1}'")
print(f"Most similar document: '{documents[index1]}'")
print(f"Similarity score: {score1:.4f}")

query2 = "Who is the God of Cricket?"
query2_embedding = embedding.embed_query(query2)
similarity2 = cosine_similarity([query2_embedding], doc_embeddings)[0]  
index2, score2 = sorted(list(enumerate(similarity2)), key=lambda x: x[1])[-1]
print(f"\nQuery: '{query2}'")
print(f"Most similar document: '{documents[index2]}'")
print(f"Similarity score: {score2:.4f}")

query3 = "Who hit the double century?"
query3_embedding = embedding.embed_query(query3)
similarity3 = cosine_similarity([query3_embedding], doc_embeddings)[0]
index3, score3 = sorted(list(enumerate(similarity3)), key=lambda x: x[1])[-1]
print(f"\nQuery: '{query3}'")
print(f"Most similar document: '{documents[index3]}'")
print(f"Similarity score: {score3:.4f}")


#output:
# Query: 'Who is the best Indian cricketer?'
# Most similar document: 'Jasprit Bumrah is an Indian fast bowler known for his unorthodox action and yorkers.'
# Similarity score: 0.6025

# Query: 'Who is the God of Cricket?'
# Most similar document: 'Sachin Tendulkar, also known as the 'God of Cricket', holds many batting records.'
# Similarity score: 0.5794

# Query: 'Who hit the double century?'
# Most similar document: 'Rohit Sharma is known for his elegant batting and record-breaking double centuries.'
# Similarity score: 0.6622