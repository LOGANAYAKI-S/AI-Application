import streamlit as st

def load_memory():

    if "messages" not in st.session_state:

        st.session_state.messages = []

    return st.session_state.messages