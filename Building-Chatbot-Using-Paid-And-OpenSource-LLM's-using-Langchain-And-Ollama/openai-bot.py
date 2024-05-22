from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser


import streamlit as st
import os 
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Set environment variables for OpenAI and LangChain
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")

# Prompt Template
prompt = ChatPromptTemplate.from_messages([
    ("system", "you are a helpful assistant. Please respond to the user queries"),
    ("user", "Question: {question}")
])

# Streamlit framework
st.title("LangChain Demo With OPENAI API")
input_text = st.text_input("Search the topic you want")

# Initialize OpenAI LLM and output parser
llm = ChatOpenAI(model="gpt-3.5-turbo")
output_parser = StrOutputParser()

# Define the conversation chain
chain = prompt | llm | output_parser

# Process user input and display output
if input_text:
    st.write(chain.invoke({'question': input_text}))
