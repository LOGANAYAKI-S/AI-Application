import streamlit as st
from groq import Groq

client = Groq(
   api_key=st.secrets["GROQ_API_KEY"]
)

st.title("Memory AI Chatbot")
if "messages" not in st.session_state:
    st.session_state.messages = []

if st.button("Clear Chat"):
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

prompt = st.chat_input("Ask something...")

if prompt:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    response = client.chat.completions.create(
        messages=st.session_state.messages,
        model="llama-3.1-8b-instant"
    )

    ai_reply = response.choices[0].message.content

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": ai_reply
        }
    )

    with st.chat_message("assistant"):
        st.markdown(ai_reply)
