import streamlit as st


def home_page():
    st.title("Welcome to Cupid Whisper ✨")
    st.write("Analyze your KakaoTalk chats with advice from four unique agents.")

    solar_api_key = st.text_input("Provide your Solar API Key: ")
    st.session_state.solar_api_key = solar_api_key

    if st.button("Get Started"):
        st.session_state.page = "agent_selection"
        st.experimental_rerun()
