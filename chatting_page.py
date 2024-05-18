import streamlit as st

from agent_selection_page import AGENT_DESCRIPTIONS


def chatting_page():
    st.title("Chat with Your Agents")

    agents = st.session_state.selected_agents
    chat_data = st.session_state.chat_data

    # Display agent introductions
    st.subheader("Agent Introductions")
    for agent in agents:
        st.write(f"**{agent}**: {AGENT_DESCRIPTIONS[agent]}")

    user_input = st.text_input("Ask your question about the relationship:")

    if user_input:
        # Placeholder for agent responses
        responses = {agent: f"{agent} response to '{user_input}'" for agent in agents}

        st.subheader("Agent Responses")
        for agent, response in responses.items():
            st.write(f"**{agent}**: {response}")

        # Placeholder for consensus options
        st.subheader("Consensus Options")
        consensus_options = ["Option 1", "Option 2", "Option 3"]
        for option in consensus_options:
            st.write(f"- {option}")
