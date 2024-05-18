import streamlit as st

from langchain.chains import LLMChain
from langchain.llms import OpenAI


# FIXME: This is just the code suggested by GPT. To be replaced with Solar LLM API
def get_agent_response(agent, user_input, chat_data):
    llm = OpenAI(api_key=st.session_state.solar_api_key)
    chain = LLMChain(llm=llm)

    # Customize prompt for each agent
    prompt = f"{agent} prompt with user input and chat data"
    response = chain.run(prompt)
    return response
