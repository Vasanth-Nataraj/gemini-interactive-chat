import os
import streamlit as st
from dotenv import load_dotenv
from google import genai

load_dotenv()
API= os.getenv("GEMINI_API_KEY")

if not API:
    st.error("Error! API Not found")
    st.stop()

rules="Do not use bold texts, and keep all responses very short and consice."

st.set_page_config(page_title="Gemini Chat",page_icon="🤖",layout="centered")
st.title("Gemini Interactive Chat")

if "client" not in st.session_state:
    st.session_state.client = genai.Client(api_key=API)

if "chat" not in st.session_state:
    st.session_state.chat=st.session_state.client.chats.create(model="gemini-3.6-flash",config={"system_instruction":rules})

if "messages" not in st.session_state:
    st.session_state.messages=[]

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt:=st.chat_input("Ask something..."):
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.messages.append({"role":"user","content":prompt})

    with st.chat_message("assistant"):
        message_placeholder=st.empty()
        full_response=""

        response=st.session_state.chat.send_message_stream(prompt)
        for chunk in response:
            full_response+=chunk.text
            message_placeholder.markdown(full_response + "▌")
        message_placeholder.markdown(full_response)
    st.session_state.messages.append({"role":"assistant","content":full_response})