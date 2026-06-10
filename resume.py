import streamlit as st
from groq import Groq

client = Groq(
    api_key=st.secrets["GROQ_API_KEY"]
)
def generate_resume(prompt):

    response = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": f"""
                Create a professional resume.

                Details:
                {prompt}

                Include:
                - Professional Summary
                - Technical Skills
                - Career Objective
                """
            }
        ],
        model="llama-3.1-8b-instant"
    )

    return response.choices[0].message.content