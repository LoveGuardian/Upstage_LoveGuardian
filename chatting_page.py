import streamlit as st

from agent_selection_page import AGENT_DESCRIPTIONS
from langchain_upstage import ChatUpstage
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from get_agent_response import get_agent_response


def chatting_page():
    st.title("Chat with Your Agents")

    agents = st.session_state.selected_agents
    chat_data = st.session_state.chat_data
    chat_analysis = st.session_state.chat_analysis

    st.subheader("Chat Analysis")

    with st.expander("Personality"):
        st.write(f"Personality: {chat_analysis['personality']}")
    
    with st.expander("Relationship Progress"):
        st.write(f"Relationship Progress: {chat_analysis['relationship_progress']}")
    
    with st.expander("Preferences"):
        st.write(f"Preferences: {chat_analysis['preferences']}")
    
    with st.expander("Contact Frequency"):
        st.write(f"Contact Frequency: {chat_analysis['contact_frequency']}")

    st.subheader("Agent Introductions")
    for agent in agents:
        with st.expander(agent):
            st.write(f"**{agent}**: {AGENT_DESCRIPTIONS[agent]}")

    user_input = st.text_input("Ask your question about the relationship:")

    if user_input:
        responses = {agent: get_agent_response(agent, user_input, chat_data) for agent in agents}

        st.subheader("Agent Responses")
        for agent, response in responses.items():
            with st.expander(f"Response from {agent}"):
                st.write(response)

        st.subheader("Consensus Options")
        consensus_options = ["Option 1", "Option 2", "Option 3"]
        for option in consensus_options:
            st.write(f"- {option}")

