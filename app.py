from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

import streamlit as st
import os
from dotenv import dotenv_values

import constant

# Set the OpenAI API key
os.environ["OPENAI_API_KEY"] = constant.openai_key

prompt = ChatPromptTemplate.from_messages(
    [
        ("ai", "you are a helpful assistant who responds in bullet points for any question asked"),
        (f"human", "Question - {question}")
    ]
)

st.title("Langchain demo with LLM")
input_text = st.text_input("Search the topic you want to search")

llm = ChatOpenAI(model="gpt-3.5-turbo")
out_parser = StrOutputParser()

chain = prompt | llm | out_parser

if input_text:
    st.write(chain.invoke({'question' : input_text}))
