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
    
    opponent_info = st.session_state.opponent_info
        # self.name = name
        # self.gender = gender
        # self.age = age
        # self.occupation = occupation
        # self.mbti = mbti
        # self.hobby = hobby
        # self.residence = residence
        # self.relationship = relationship
        # self.birthday = birthday
        # self.liked_food = liked_food
        # self.disliked_food = disliked_food
    
    chat_prompt = PromptTemplate.from_template(
        """
        Analyze the chat data to determine the {aspect}.
        ---
        Context: {chat_text}
        ---
        Take this is the information about the person I'm interested in when analyzing the chat data:
        Name is {name}, gender is {gender}
        He/she is {age} years old.
        He/she is a {occupation}.
        His/her MBTI is {mbti}.
        His/her hobby is {hobby}.
        He/she lives in {residence}.
        He/she is currently {relationship}.
        His/her birthday is {birthday}.
        His/her favorite food is {liked_food}.
        He/she doesn't like {disliked_food}.
        """
    )
    
    chain = chat_prompt | llm | StrOutputParser()
    response = chain.invoke({"aspect": aspect, "chat_text": chat_text, 
                             "name": opponent_info.name, "gender": opponent_info.gender, 
                             "age": opponent_info.age, "occupation": opponent_info.occupation, "mbti": opponent_info.mbti, 
                             "hobby": opponent_info.hobby, "residence": opponent_info.residence, "relationship": opponent_info.relationship, 
                             "birthday": opponent_info.birthday, "liked_food": opponent_info.liked_food, "disliked_food": opponent_info.disliked_food})
    
    return response
