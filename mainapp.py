import streamlit as st

st.set_page_config(
    page_title="AI Super Assistant",
    page_icon="🤖"
)

st.title("🤖 AI Super Assistant")

module = st.sidebar.selectbox(
    "Choose Module",
    [
        "Home",
        "AI Chatbot",
        "Memory Chatbot",
        "Translator",
        "Live News"
    ]
)

if module == "Home":

    st.header("Welcome")