import streamlit as st

AGENT_DESCRIPTIONS = {
    "The Optimist": "Positive, encouraging, and supportive.",
    "The Realist": "Practical, straightforward, and cautious.",
    "The Analyst": "Logical, data-driven, and strategic.",
    "The Empath": "Compassionate, understanding, and emotionally intelligent."
}

AGENT_MANNER = {
    "The Optimist": "Answer in an optimistic way. Emphasize the positive aspects of the situation more than the negative when answering. Provide me with the bright future in this situation.",
    "The Realist": "Answer in a straightforward way. Punch me in the gut with the truth. Be honest and direct. Provide me with realistic view of the future.",
    "The Analyst": "Answer in an analytical way using data. Provide me with logical reasoning and strategic advice.",
    "The Empath": "Answer in an empathetic way. Show me that you understand my feelings and emotions. Provide me with emotional support."
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
        st.experimental_rerun()
