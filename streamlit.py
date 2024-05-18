from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

import warnings
warnings.filterwarnings("ignore")
from langchain_upstage import ChatUpstage
import os
import streamlit as st
#from langchain.llms import OpenAI
from langchain_community.llms import OpenAI


st.title('🦜🔗 Love Guardian')

#openai_api_key = st.sidebar.text_input('OpenAI API Key')
openai_api_key = os.environ["UPSTAGE_API_KEY"]

def generate_response(input_text):
  llm = OpenAI(temperature=0.7, openai_api_key=openai_api_key)
#   llm =  OpenAI(temperature=0.7,
#     api_key=os.environ["UPSTAGE_API_KEY"], base_url="https://api.upstage.ai/v1/solar"
#     )
  st.info(llm(input_text))

with st.form('my_form'):
  text = st.text_area('Enter text:', 'What are the three key pieces of advice for learning how to code?')
  submitted = st.form_submit_button('Submit')
  if not openai_api_key.startswith('sk-'):
    st.warning('Please enter your OpenAI API key!', icon='⚠')
  if submitted and openai_api_key.startswith('sk-'):
    generate_response(text)