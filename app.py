import streamlit as st

st.title("Medical Query Classification Chatbot")

query = st.text_input("Enter your medical query")

if query:
    st.write("Predicted Category: Diagnostic")
