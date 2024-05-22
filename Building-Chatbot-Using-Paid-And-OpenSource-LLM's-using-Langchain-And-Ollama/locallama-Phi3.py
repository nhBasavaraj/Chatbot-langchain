from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama


import streamlit as st
import os
from dotenv import load_dotenv
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
st.title("Microsoft Phi-3 Chatbot with Ollama")
input_text = st.text_input("Search the topic you want")

# Initialize ollama Phi-3 LLM 
llm = Ollama(model="phi3")
output_parser = StrOutputParser()
chain=prompt|llm|output_parser

# Process user input and display output
if input_text:
    st.write(chain.invoke({'question': input_text}))
