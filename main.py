import streamlit as st

# Importing page functions
from home_page import home_page
from agent_selection_page import agent_selection_page
from upload_opponent_info_page import upload_opponent_info_page
from upload_chat_page import upload_chat_page
from chatting_page import chatting_page

# Initializing session state
if "page" not in st.session_state:
    st.session_state.page = "home"
if "selected_agents" not in st.session_state:
    st.session_state.selected_agents = []
if "chat_data" not in st.session_state:
    st.session_state.chat_data = ""
if "chat_analysis" not in st.session_state:
    st.session_state.chat_analysis = {}
if "solar_api_key" not in st.session_state:
    st.session_state.solar_api_key = ""
if "conversation_history" not in st.session_state:
    st.session_state.conversation_history = {}

# Navigation
if st.session_state.page == "home":
    home_page()
elif st.session_state.page == "agent_selection":
    agent_selection_page()
elif st.session_state.page == "upload_opponent_info":
    upload_opponent_info_page()
elif st.session_state.page == "upload_chat":
    upload_chat_page()
elif st.session_state.page == "chatting_page":
    chatting_page()
