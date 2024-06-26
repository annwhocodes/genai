import streamlit as st


st.set_page_config(page_title="Configuration: ")


col1, col2 = st.columns(2)

with st.form("customiser"):
    with col1:
        language_option = st.selectbox(
            "Select language: ",
            ("English", "Hindi", "French", "Spanish")
        )

    with col2:
        gender_option = st.selectbox(
            "Select Gender: ",
            ("Male", "Female", "Others")
        )

    adjectives = st.multiselect("Behaviour",
     ["adorable",
        "charming",
        "witty",
        "elegant",
        "energetic",
        "introverted",
        "shy",
        "dominant",
        "romantic",
        "comforting"
    ])
    
    submit_preferences = st.form_submit_button("Submit")

if 'language' not in st.session_state or 'behaviour' not in st.session_state:
    st.session_state.language = "English"
    st.session_state.behaviour = ()

if submit_preferences:
    st.session_state.language = language_option
    st.session_state.behaviour = adjectives

st.write(st.session_state.language)
st.write(st.session_state.behaviour)



