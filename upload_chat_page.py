import streamlit as st


def upload_chat_page():
    st.title("Upload Your Chat")
    st.write("Upload your KakaoTalk chat file in .txt format.")

    uploaded_file = st.file_uploader("Choose a file...", type="txt")
    if uploaded_file:
        st.session_state.chat_data = uploaded_file.read().decode("utf-8")
        if st.button("Upload"):
            st.session_state.page = "chatting_page"
