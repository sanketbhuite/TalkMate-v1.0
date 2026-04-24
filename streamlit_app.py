import streamlit as st
import requests

st.title("TalkMate AI")

msg = st.text_input("Ask something")

if st.button("Send"):
    if msg:
        res = requests.post(
            "http://localhost:5000/process",
            json={"message": msg}
        )
        st.write(res.json())