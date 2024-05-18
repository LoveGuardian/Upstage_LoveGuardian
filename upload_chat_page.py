import streamlit as st
import pandas as pd

def upload_chat_page():
    st.title("Upload Your Chat")
    st.write("Upload your KakaoTalk chat file in .txt or csv format.")
    uploaded_file = st.file_uploader("Choose a file...", type=["txt", "csv"])

    # I need to upload a KakaoTalk chat file in .csv format as well
    if uploaded_file:
        # if uploaded_file.type is txt
        if uploaded_file.type == "txt":
            st.session_state.chat_data = uploaded_file.read().decode("utf-8")
        elif uploaded_file.type == "csv":
            chat_data = pd.read_csv(uploaded_file)
            st.session_state.chat_data = chat_data.to_string(index=False)
        if st.button("Upload"):
            st.session_state.page = "chatting_page"
            st.rerun()