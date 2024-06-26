import sys
sys.path.append('../langchen')

from gtts import gTTS
from io import BytesIO
from constants import gemini_key
import streamlit as st
import google.generativeai as genai
import base64


genai.configure(api_key=gemini_key)

def role_to_streamlit(role):
  if role == "model":
    return "assistant"
  else:
    return role
  
sound_file = BytesIO()



st.set_page_config(page_title="hahaha")
st.header("Gemini chat bot")


if 'language' not in st.session_state or 'behaviour' not in st.session_state:
    st.session_state.language = "English"
    st.session_state.behaviour = ()

with st.form("customiser"):
    col1,col2 = st.columns(2)
    with col1:
        st.write("Select Language: ")
        language_option = st.selectbox(
                "Select language: ",
                ("English", "Hindi", "French", "Spanish", "Maithali"),
            )
    with col2:
        st.write("Select Gender: ")
        gender_option = st.selectbox(
                "Select: ",
                ("Male", "Female", "Other"),
            )
    
    submit_button = st.form_submit_button("Submit")



prompt_customised=[
    f"""
    You only respond in {language_option},
    You are a {"male" if gender_option == "Female" else "female"},
    You act as {st.session_state.behaviour}
    
    
    """
]




model = genai.GenerativeModel(
    "gemini-1.5-pro",
    system_instruction=[
        "You are a very flirty person.",
        "you respond as if you want to impress the person in front.",
    ],
    )
chat = model.start_chat(history=[])
if 'chat' not in st.session_state:
    st.session_state.chat = model.start_chat(history=[])


for message in st.session_state.chat.history:
    with st.chat_message(role_to_streamlit(message.role)):
        st.markdown(message.parts[0].text)

if prompt := st.chat_input("I possess a well of knowledge. What would you like to know?"):
    st.chat_message("user").markdown(prompt)
        
    response = st.session_state.chat.send_message([prompt,prompt_customised[0]],
        safety_settings={
            "HARM_CATEGORY_HARASSMENT": "block_none",
            "HARM_CATEGORY_SEXUALLY_EXPLICIT": "block_none",
            "HARM_CATEGORY_HATE_SPEECH": "block_none",
            "HARM_CATEGORY_DANGEROUS_CONTENT": "block_none",
        },
    ) 

    
        
    with st.chat_message("assistant"):
        st.markdown(response.text)
        tts = gTTS(response.text, lang='en', tld="com")
        tts.write_to_fp(sound_file)
        st.audio(sound_file)
    





