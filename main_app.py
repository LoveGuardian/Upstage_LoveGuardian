import streamlit as st

def home_page():
    st.title("Welcome to LoveGuardians")
    st.write("Analyze your KakaoTalk chats with advice from four unique agents.")
    if st.button("Get Started"):
        st.session_state.page = "agent_selection"
