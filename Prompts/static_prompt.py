from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

st.header("Static Prompt Example")
model = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.7)
st.text_input("Enter a prompt:", key="prompt")
if st.button("Submit"):
    result = model.invoke(st.session_state.prompt)
    st.write("Response:")
    st.write(result.content)

