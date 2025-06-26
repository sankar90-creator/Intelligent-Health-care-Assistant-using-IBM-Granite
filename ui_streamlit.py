import streamlit as st
import requests

st.title("HealthAI - Intelligent Healthcare Assistant")

user_input = st.text_input("Describe your symptoms:")

if st.button("Ask AI"):
    response = requests.post("http://localhost:5000/ask", json={"question": user_input})
    st.write("AI Response:", response.json()["response"])
