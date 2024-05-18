import streamlit as st
import pandas as pd
from langchain_upstage import ChatUpstage
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate


def upload_chat_page():
    st.title("Upload Your Chat")
    st.write("Upload your KakaoTalk chat file in .txt or csv format.")
    uploaded_file = st.file_uploader("Choose a file...", type=["txt", "csv"])

    # I need to upload a KakaoTalk chat file in .csv format as well
    if uploaded_file:
        chat_text = uploaded_file.read().decode("utf-8")
        analysis = analyze_chat_data(chat_text)

        st.session_state.chat_data = chat_text
        st.session_state.chat_analysis = analysis

        # FIXME: the following if condition doesn't work.
        # if uploaded_file.type == "txt":
        #
        # elif uploaded_file.type == "csv":
        #     chat_data = pd.read_csv(uploaded_file)
        #     st.session_state.chat_data = chat_data.to_string(index=False)
        #     st.session_state.chat_analysis = {}

        if st.button("Upload"):
            st.session_state.page = "chatting_page"
            st.experimental_rerun()


def analyze_chat_data(chat_text):
    analysis = {
        "personality": generate_analysis("상대방 성격", chat_text),
        "relationship_progress": generate_analysis("관계 진전 상황", chat_text),
        "preferences": generate_analysis("취향 파악", chat_text),
        "contact_frequency": generate_analysis("연락 빈도", chat_text)
    }
    return analysis


def generate_analysis(aspect, chat_text):
    llm = ChatUpstage(api_key=st.session_state.solar_api_key)

    if aspect == "personality":
        prompt_template = """
        Analyze the chat data to determine the personality traits of the opponent. 
        Consider the tone, choice of words, and interaction style. 
        Provide the response in fluent Korean in no more than two sentences.
        ---
        Context: {chat_text}
        """
    elif aspect == "relationship progress":
        prompt_template = """
        Analyze the chat data to determine the relationship progress between the user and the opponent. 
        Look for signs of growing intimacy, commitments, and changes in communication patterns over time. 
        Provide the response in fluent Korean in no more than two sentences.
        ---
        Context: {chat_text}
        """
    elif aspect == "preferences":
        prompt_template = """
        Analyze the chat data to identify the preferences of the opponent. 
        Include likes, dislikes, hobbies, and interests. 
        Note any explicit mentions or implicit indications of preferences. 
        Provide the response in fluent Korean in no more than two sentences.
        ---
        Context: {chat_text}
        """
    elif aspect == "contact frequency":
        prompt_template = """
        Analyze the chat data to determine the contact frequency between the user and the opponent. 
        Calculate the number of messages exchanged per day and identify any patterns or changes in frequency. 
        Provide the response in fluent Korean in no more than two sentences.
        ---
        Context: {chat_text}
        """ 
    chat_prompt = PromptTemplate.from_template(
        """
        Analyze the chat data to determine the {aspect}.
        ---
        Context: {chat_text}
        """
    )

    chat_prompt = PromptTemplate.from_template(prompt_template)
    chain = chat_prompt | llm | StrOutputParser()
    response = chain.invoke({"aspect": aspect, "chat_text": chat_text})
    
    return response
