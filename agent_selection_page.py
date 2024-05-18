import streamlit as st

AGENT_DESCRIPTIONS = {
    "The Optimist": "Positive, encouraging, and supportive.",
    "The Realist": "Practical, straightforward, and cautious.",
    "The Analyst": "Logical, data-driven, and strategic.",
    "The Empath": "Compassionate, understanding, and emotionally intelligent."
}


def agent_selection_page():
    st.title("Select Your Agents")
    st.write("Choose up to 2 agents to help analyze your chat.")

    selected_agents = st.multiselect("Select Agents", list(AGENT_DESCRIPTIONS.keys()), max_selections=2)
    for agent in selected_agents:
        st.write(f"**{agent}**: {AGENT_DESCRIPTIONS[agent]}")

    if st.button("Next"):
        st.session_state.selected_agents = selected_agents
        st.session_state.page = "upload_opponent_info"
        st.rerun()
