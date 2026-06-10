import PyPDF2

from modules.chatbot import get_ai_response

def read_document(uploaded_file):

    text = ""

    # PDF FILE
    if uploaded_file.name.endswith(".pdf"):

        pdf_reader = PyPDF2.PdfReader(uploaded_file)

        for page in pdf_reader.pages:

            text += page.extract_text()

    # TXT FILE
    elif uploaded_file.name.endswith(".txt"):

        text = uploaded_file.read().decode("utf-8")

    return text


def summarize_document(text):

    messages = [
        {
            "role": "user",
            "content": f"""
            Summarize this document clearly:

            {text}
            """
        }
    ]

    return get_ai_response(messages)