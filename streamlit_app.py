import streamlit as st
import requests

st.title("TalkMate AI")

msg = st.text_input("Ask something")

if st.button("Send"):
    if msg:
        res = requests.post(
            "https://opulent-cod-69vjwpwwxv9gc77p-8501.app.github.dev/process",
            json={"message": msg}
        )
        st.write(res.json())