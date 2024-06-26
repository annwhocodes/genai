from constants import gemini_key
import streamlit as st
import google.generativeai as genai

genai.configure(api_key=gemini_key)


def get_flirting_model(language):
    model = genai.GenerativeModel(
        "gemini-1.5-pro",
        system_instruction=[
            "You are a very flirty person.",
            "you respond as if you want to impress the person in front.",
            "You only respond in" + language,
        ],
        )
    return model


def get_gemini_response(question):
    model = get_flirting_model()
    response = model.generate_content(
        question,
        safety_settings={
            "HARM_CATEGORY_HARASSMENT": "block_none",
            "HARM_CATEGORY_SEXUALLY_EXPLICIT": "block_none",
            "HARM_CATEGORY_HATE_SPEECH": "block_none",
            "HARM_CATEGORY_DANGEROUS_CONTENT": "block_none",
        },
        generation_config=genai.GenerationConfig(
            candidate_count=1,
            temperature=0.9,
            max_output_tokens=500
        )
        )
    response.prompt_feedback
    return response.text

st.set_page_config(page_title="q and a")
st.header("Gemini llm")
input = st.text_input("Input: ", key="input")
submit = st.button("ask")

if submit:
    response = get_gemini_response(input)
    st.subheader("Response: ")
    st.write(response)






