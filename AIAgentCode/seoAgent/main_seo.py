import os
from constant import openai_key
from constant import rapid_api_key
from openai import OpenAI
from actions import get_seo_page_report
from prompts import react_system_prompt
from json_helpers import extract_json

import streamlit as st
os.environ["OPENAI_API_KEY"]= openai_key
os.environ["RAPID_API_KEY"]= rapid_api_key


openai_client = OpenAI(api_key=openai_key)

def generate_text_with_conversation(
        messages,
        model="gpt-3.5-turbo"
):
    response = openai_client.chat.completions.create(
        model = model,
        messages = messages
    )
    return response.choices[0].message.content

#Available actions are:

available_actions = {
    "get_seo_page_report": get_seo_page_report
}

user_prompt = "what is the response time of https://learnwithhasan.com"

messages = [
    {"role" : "system", "content": react_system_prompt},
    {"role" : "user" , "content" : user_prompt}
]

think_loop = 0
while think_loop <= 5:
    think_loop += 1
    response = generate_text_with_conversation(messages,"gpt-4")
    print("printing response" , response)
    json_function  = extract_json(response)
    print("hello")
    if json_function:
        function_name = json_function[0]['function_name']
        function_parms = json_function[0]['function_parms']
        if function_name not in available_actions:
            raise Exception(f"Unknown action: {function_name}: {function_parms}")
        print(f" -- running {function_name} {function_parms}")
        action_function = available_actions[function_name]
        # call the function
        result = action_function(**function_parms)
        function_result_message = f"Action_Response: {result}"
        messages.append({"role": "user", "content": function_result_message})
        print(function_result_message)
        print("end of loop")
    else:
         break
