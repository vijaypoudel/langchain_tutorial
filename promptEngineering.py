import os
from constant import openai_key
from langchain_openai import OpenAI
from langchain_core.prompts import PromptTemplate
import streamlit as st

# Set the OpenAI API key
os.environ["OPENAI_API_KEY"] = openai_key

# Streamlit UI setup
st.title("Celebrity Search Result")

# Input field for user to type the topic
input_text = st.text_input("Search the topic you want")

# Define the prompt template
first_input_prompt = PromptTemplate(
    input_variables=['name'],
    template="Tell me about celebrity {name}"
)

# Initialize the OpenAI LLM with the desired parameters
llm = OpenAI(temperature=0.8)

# Create the runnable sequence with the defined prompt and LLM
chain = first_input_prompt | llm

# Run the chain and display the result if there's an input
if input_text:
    result = chain.invoke({"name": input_text})
    st.write(result)