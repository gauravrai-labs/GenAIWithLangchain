from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel

llm = HuggingFaceEndpoint(
    repo_id="openai/gpt-oss-120b",
    task="text-generation"
)

model1 = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.9)
model2 = ChatHuggingFace(llm=llm)

template1 = PromptTemplate(
    template="Generate short and simple notes from the following text: {text}",
    input_variables=['text']
)

template2 = PromptTemplate(
    template="Generate 5 short question answers from the following text: {text}", 
    input_variables=['text']
)

prompt3 = PromptTemplate(
    template='Merge the provided notes and quiz into a single document \n notes -> {notes} and quiz -> {quiz}',
    input_variables=['notes', 'quiz']
)

parser = StrOutputParser()

parallel_chain = RunnableParallel({
    "notes": template1 | model1 | parser,
    "quiz": template2 | model2 | parser
})

merge_chain = prompt3 | model1 | parser

chain = parallel_chain | merge_chain

llm = HuggingFaceEndpoint(
    repo_id="openai/gpt-oss-120b",
    task="text-generation"
    )

text_model = ChatHuggingFace(llm=llm)
text = text_model.invoke("write a detailed report on topic India")
result = chain.invoke({"text": text})

print(result)
print(chain.get_graph().print_ascii())

# output:
'''
India: A Comprehensive Overview

India is the world's largest democracy and the seventh-largest country by land area. With a population exceeding 1.44 billion, it is the second-most populous nation after China. The country is the fastest-growing major economy, boasting a strategic location and rich cultural heritage.

Geography:
India is located in South Asia and shares borders with countries such as Pakistan, China, Nepal, Bhutan, Bangladesh, Myanmar, and the Indian Ocean. The country has diverse topography, including the Himalayan range, Indo-Gangetic Plains, Deccan Plateau, and coastal zones. The highest point in India is Kangchenjunga, standing at 8,586 meters. The Indo-Gangetic Plains support roughly half of India's population. India has a coastline that measures approximately 7,516 kilometers.

Natural Resources:
India is rich in natural resources, including coal, iron ore, bauxite, manganese, natural gas, diamonds, and extensive agricultural land.

Climate:
The climate in India varies from tropical to arid, with the monsoon season playing a crucial role in the country's weather patterns.

Quiz:
1. What is India's population according to the 2024 estimate?
   Answer: Over 1.44 billion people.

2. What is the highest point in India and its elevation?
   Answer: Kangchenjunga - 8,586 meters.

3. Which geographic region supports roughly half of India's population?
   Answer: The Indo-Gangetic Plains.

4. How long is India's coastline?
   Answer: Approximately 7,516 kilometers.

5. Name three natural resources that India possesses.
   Answer: Coal, iron ore, and bauxite (among others).

This report covers India's geography, history, political system, economy, demographics, social indicators, culture, science & technology, foreign relations, and future challenges. India's significance on the global stage cannot be understated, and its rich tapestry of culture and resources continues to shape its position as a major player in the international community.
            +---------------------------+            
            | Parallel<notes,quiz>Input |            
            +---------------------------+            
                 **               **                 
              ***                   ***              
            **                         **            
+----------------+                +----------------+ 
| PromptTemplate |                | PromptTemplate | 
+----------------+                +----------------+ 
          *                               *          
          *                               *          
          *                               *          
  +------------+                 +-----------------+ 
  | ChatOpenAI |                 | ChatHuggingFace | 
  +------------+                 +-----------------+ 
          *                               *          
          *                               *          
          *                               *          
+-----------------+              +-----------------+ 
| StrOutputParser |              | StrOutputParser | 
+-----------------+              +-----------------+ 
                 **               **                 
                   ***         ***                   
                      **     **                      
           +----------------------------+            
           | Parallel<notes,quiz>Output |            
           +----------------------------+            
                          *                          
                          *                          
                          *                          
                 +----------------+                  
                 | PromptTemplate |                  
                 +----------------+                  
                          *                          
                          *                          
                          *                          
                   +------------+                    
                   | ChatOpenAI |                    
                   +------------+                    
                          *                          
                          *                          
                          *                          
                +-----------------+                  
                | StrOutputParser |                  
                +-----------------+                  
                          *                          
                          *                          
                          *                          
              +-----------------------+              
              | StrOutputParserOutput |              
              +-----------------------+              
None


'''