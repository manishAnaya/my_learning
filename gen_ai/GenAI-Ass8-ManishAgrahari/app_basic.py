import streamlit as st

st.title("Welcome to Streamlit!")

st.text_input("Enter your Name")

if st.button("Greet Me"):
    st.write("Hello, !")