import streamlit as st
from datetime import date

st.title("🎂 Age Calculator")
st.subheader("Please enter your Date of Birth")

dob = st.date_input(
    "Date of Birth",
    min_value=date(1900, 1, 1),
    max_value=date.today()
)

today = date.today()
age = today.year - dob.year

if (today.month, today.day) < (dob.month, dob.day):
    age -= 1

st.write(f"## 🎉 Your Date of Birth is: {dob.strftime('%d %B %Y')}")
st.write(f"## 🧓 Your Age is: **{age} years**")
