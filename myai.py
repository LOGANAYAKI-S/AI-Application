import streamlit as st

from modules.code_explainer import explain_code
from modules.document import read_document
from modules.document import summarize_document
from modules.chatbot import get_ai_response
from modules.news import get_news
from modules.ui import setup_ui
from modules.resume import generate_resume
from modules.notes_generator import generate_notes

# ---------------- UI ---------------- #

setup_ui()

st.markdown(
    """
    # 

    Welcome to your smart AI application.
    Generate notes, resumes, summarize PDFs, search news, and more.
    """
)

st.divider()

# ---------------- MEMORY ---------------- #

if "messages" not in st.session_state:

    st.session_state.messages = []

if "chat_titles" not in st.session_state:

    st.session_state.chat_titles = []

messages = st.session_state.messages

# ---------------- SIDEBAR ---------------- #

st.sidebar.title("Chats")

from datetime import datetime

current_time = datetime.now().strftime("%d-%m-%Y %H:%M")

st.sidebar.caption(f"Last Active: {current_time}")

st.sidebar.markdown("### Features")

st.sidebar.write("🤖 AI Chatbot")
st.sidebar.write("📄 PDF Reader")
st.sidebar.write("📝 Notes Generator")
st.sidebar.write("📰 News Search")
st.sidebar.write("💼 Resume Generator")
st.sidebar.write("💻 Code Explainer")

st.sidebar.divider()

# ---------------- NEW CHAT ---------------- #

if st.sidebar.button("🆕 New Chat"):

    st.session_state.messages = []

    st.rerun()

# ---------------- CHAT HISTORY ---------------- #

st.sidebar.markdown("### Chat History")

for title in st.session_state.chat_titles:

    st.sidebar.write("💬 " + title[:30])

# ---------------- DOCUMENT UPLOAD ---------------- #

uploaded_file = st.sidebar.file_uploader(
    "Upload PDF or TXT",
    type=["pdf", "txt"]
)

# ---------------- SHOW CHAT ---------------- #

for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.markdown(message["content"])

# ---------------- USER INPUT ---------------- #

prompt = st.chat_input(
    "Ask anything..."
)

# ---------------- PROCESS ---------------- #

if prompt:

    # SAVE CHAT TITLE ONLY FIRST MESSAGE
    if len(st.session_state.messages) == 0:

        st.session_state.chat_titles.append(prompt)

    # SAVE USER MESSAGE
    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )

    # SHOW USER MESSAGE
    with st.chat_message("user"):

        st.markdown(prompt)

    # ---------------- ASSISTANT RESPONSE ---------------- #

    with st.chat_message("assistant"):

        with st.spinner("Thinking..."):

            # ---------------- PDF READER ---------------- #

            if uploaded_file:

                document_text = read_document(uploaded_file)

                reply = summarize_document(document_text)

            # ---------------- RESUME GENERATOR ---------------- #

            elif "resume" in prompt.lower():

                reply = generate_resume(prompt)

            # ---------------- NOTES GENERATOR ---------------- #

            elif "notes" in prompt.lower():

                reply = generate_notes(prompt)

            # ---------------- NEWS SEARCH ---------------- #

            elif "news" in prompt.lower():

                topic = prompt.lower()

                topic = topic.replace("news", "")
                topic = topic.replace("latest", "")
                topic = topic.strip()

                if topic == "":

                    topic = "world"

                reply = get_news(topic)

            # ---------------- CODE EXPLAINER ---------------- #

            elif "code" in prompt.lower() or "program" in prompt.lower():

                reply = explain_code(prompt)

            # ---------------- NORMAL AI CHATBOT ---------------- #

            else:

                reply = get_ai_response(st.session_state.messages)

            # ---------------- SHOW RESPONSE ---------------- #

            st.markdown(reply)

            st.success("Response Generated Successfully")

    # ---------------- SAVE AI RESPONSE ---------------- #

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": reply
        }
    )

    st.rerun()