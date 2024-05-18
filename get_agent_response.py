import streamlit as st

from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_upstage import ChatUpstage

from agent_selection_page import AGENT_DESCRIPTIONS


def get_agent_response(agent, user_input, chat_data):
    llm = ChatUpstage(api_key=st.session_state.solar_api_key)

    prompt_template = PromptTemplate.from_template(
        """
        Please provide the most relevant response based on the given context.
        
        First, a text of chat between two possible lovers, is given as "<Chat>".
        Second, the previous questions and the corresponding responses given by you, are given as "<Conversation>".
        Third, the question on which you should provide a response now, is given as "<Question>".
        Each region is separated by "-----------".
        
        Keep in mind that you are "{agent_type}" agent.
        You should respond based on a "{agent_personality}" perspective.
        
        ----------
        <Chat>
        {chat}
        ----------
        <Conversation>
        {conversation}
        ----------
        <Question>
        {question}
        """
    )
    chain = prompt_template | llm | StrOutputParser()

    # 3. define chain
    agent_type = agent
    agent_personality = AGENT_DESCRIPTIONS[agent]

    response = chain.invoke(
        {
            "agent_type": agent_type,
            "agent_personality": agent_personality,
            "chat": chat_data,
            "conversation": st.session_state.conversation_history.get(agent, ""),
            "question": user_input,
        }
    )

    st.session_state.conversation_history[agent] = (
            st.session_state.conversation_history.get(agent, "")
            + f"Q: {user_input}\n"
            + f"A: {response}\n\n"
    )

    return response
