from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import json

load_dotenv()

with open("StructuredOutput/review_json_schema.json", "r") as f:
    review_schema = json.load(f)

model = ChatOpenAI()
structed_model = model.with_structured_output(review_schema)
response = structed_model.invoke("""I recently upgraded to the Samsung Galaxy S24 Ultra, and I must say, it's an absolute powerhouse! The Snapdragon 8 Gen 3 processor makes everything lightning fast—whether I'm gaming, multitasking, or editing photos. The 5000mAh battery easily lasts a full day even with heavy use, and the 45W fast charging is a lifesaver.

The S-Pen integration is a great touch for note-taking and quick sketches, though I don't use it often. What really blew me away is the 200MP camera—the night mode is stunning, capturing crisp, vibrant images even in low light. Zooming up to 100x actually works well for distant objects, but anything beyond 30x loses quality.

However, the weight and size make it a bit uncomfortable for one-handed use. Also, Samsung’s One UI still comes with bloatware—why do I need five different Samsung apps for things Google already provides? The $1,300 price tag is also a hard pill to swallow.

Pros:
Insanely powerful processor (great for gaming and productivity)
Stunning 200MP camera with incredible zoom capabilities
Long battery life with fast charging
S-Pen support is unique and useful
                                 
Review by Gaurav rai on 2024-06-15""")

print(response)

#output:
'''
{'key_themes': ['powerful processor', 'long battery life', 'fast charging', 'S-Pen integration', '200MP camera', 'weight and size', 'bloatware', 'price'], 'summary': "Gaurav rai praises the Samsung Galaxy S24 Ultra as a powerhouse device with a lightning-fast Snapdragon 8 Gen 3 processor, long-lasting battery, impressive 200MP camera, and useful S-Pen integration. However, he criticizes its weight and size for one-handed use, the bloatware in Samsung's One UI, and the high $1,300 price tag.", 'sentiment': 'pos', 'pros': ['Insanely powerful processor (great for gaming and productivity)', 'Stunning 200MP camera with incredible zoom capabilities', 'Long battery life with fast charging', 'S-Pen support is unique and useful'], 'cons': ['Weight and size make one-handed use uncomfortable', "Bloatware in Samsung's One UI", 'High $1,300 price tag'], 'name': 'Gaurav rai'}
'''