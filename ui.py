import streamlit as st

def setup_ui():

    st.set_page_config(
        page_title="AI Personal Assistant Chatbot",
        page_icon="🤖",
        layout="centered"
    )

    st.markdown("""
    <style>

    .stApp {
        background: linear-gradient(to bottom right, #f8fafc, #e2e8f0);
    }

    .main .block-container {
        max-width: 900px;
        padding-top: 2rem;
    }

    h1 {
        text-align: center;
        color: #111827;
        font-size: 48px;
        font-weight: bold;
    }

    .subtitle {
        text-align: center;
        color: #6b7280;
        font-size: 18px;
        margin-bottom: 30px;
    }

    </style>
    """, unsafe_allow_html=True)

    st.markdown(
        """
        <h1>🤖 AI Personal Assistant Chatbot</h1>

        <p class="subtitle">
            Smart AI • Live News • AI Assistant ✨
        </p>
        """,
        unsafe_allow_html=True
    )