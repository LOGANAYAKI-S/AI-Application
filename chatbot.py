import streamlit as st
from groq import Groq

client = Groq(
    api_key=st.secrets["GROQ_API_KEY"]
)

def get_ai_response(messages):

    response = client.chat.completions.create(
        messages=messages,
        model="llama-3.1-8b-instant"
    )

    return response.choices[0].message.content