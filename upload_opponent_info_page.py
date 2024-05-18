import streamlit as st


class OpponentInfo:
    def __init__(self, name, gender, age, occupation, mbti, hobby, residence, relationship, birthday, liked_food,
                 disliked_food, other_details):
        self.name = name
        self.gender = gender
        self.age = age
        self.occupation = occupation
        self.mbti = mbti
        self.hobby = hobby
        self.residence = residence
        self.relationship = relationship
        self.birthday = birthday
        self.liked_food = liked_food
        self.disliked_food = disliked_food
        self.other_details = other_details


def upload_opponent_info_page():
    st.title("Upload Your Opponent Info")
    st.write("Type in some information about your opponent. It will be considered when analyzing your chats.")

    opponent_info = OpponentInfo(
        st.text_input("Name"),
        st.text_input("Gender"),
        st.text_input("Age"),
        st.text_input("Occupation"),
        st.text_input("MBTI"),
        st.text_input("Hobby"),
        st.text_input("Residence"),
        st.text_input("Relationship"),
        st.text_input("Birthday"),
        st.text_input("Liked Food"),
        st.text_input("Disliked Food"),
        st.text_input("Other Details")
    )

    if st.button("Register"):
        st.session_state.opponent_info = opponent_info
        st.session_state.page = "upload_chat"
        st.rerun()