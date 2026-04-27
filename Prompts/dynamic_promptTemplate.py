from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import streamlit as st
from langchain_core.prompts import PromptTemplate, load_prompt

load_dotenv()

st.header("Dynamic Prompt Example")
st.subheader("Research Assistant")
model = ChatOpenAI(model="gpt-3.5-turbo", temperature=1.0)
paper_input = st.text_input("Enter a research paper title or topic:", key="paper")
style_input = st.selectbox("Select a writing style:", ["Formal", "Informal", "Technical", "Conversational"], key="style")   
length_input = st.slider("Select summary length (in words):", min_value=50, max_value=500, value=150, step=50, key="length")

template = PromptTemplate(
    template="""
        Please summarize the research paper titled "{paper_input}" with the following specifications:
        Explanation Style: {style_input}  
        Explanation Length: {length_input}  
        1. Mathematical Details:  
        - Include relevant mathematical equations if present in the paper.  
        - Explain the mathematical concepts using simple, intuitive code snippets where applicable.  
        2. Analogies:  
        - Use relatable analogies to simplify complex ideas.  
        If certain information is not available in the paper, respond with: "Insufficient information available" instead of guessing.  
        Ensure the summary is clear, accurate, and aligned with the provided style and length.
        """,
    input_variables=['paper_input', 'style_input','length_input'],
    validate_template=True
    )   

# Instead of above formatting the prompt here, we can also save the template and load it when needed. This allows for better organization and reusability of prompts.
# template = load_prompt("Prompt\\template.json") 

if st.button("Generate Summary"):
    prompt = template.format(paper_input=paper_input, style_input=style_input, length_input=length_input)
    result = model.invoke(prompt)
    st.write("Summary:")
    st.write(result.content)
