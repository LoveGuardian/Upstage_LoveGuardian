import streamlit as st
import os

from langchain.chains import LLMChain
from langchain.llms import OpenAI

from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_upstage import ChatUpstage
from langchain_community.document_loaders import TextLoader

from agent_selection_page import AGENT_DESCRIPTIONS




def get_agent_response(agent, user_input, chat_data):

    llm = ChatUpstage(api_key = st.session_state.solar_api_key)

    prompt_template = PromptTemplate.from_template(
        """
        Please provide most relevant response based on the following context which is a text of chat between two possible lovers.
        You're {agent_type} with "{agent_personality}" personality.   
        ---
        Question: {question}
        ---
        Context: {Context}
        """
    )
    chain = prompt_template | llm | StrOutputParser()
    # 3. define chain
    agent_type = agent
    agent_personality = AGENT_DESCRIPTIONS[agent]

    # chain.invoke({"agent_type": agent_type, "agent_personality": agent_personality, "question": "What do you think is the personality of the guy?", "Context": docs})

    # chain.invoke({"agent_type": agent_type, "agent_personality": agent_personality, "question": "Describe the current relationship status of these two people", "Context": docs})

    # chain.invoke({"agent_type": agent_type, "agent_personality": agent_personality, "question": "Do you think the guy is interested in me?", "Context": docs})

    response = chain.invoke({"agent_type": agent_type, "agent_personality": agent_personality, "question": user_input, "Context": chat_data})

    return response