import streamlit as st
import requests

st.set_page_config(
    page_icon = "",
    page_title = "currency converter",
    layout="wide"
)

st.title("Live currency converter")
amount = st.number_input("Enter the amount in INR", min_value=1)

target_currency = st.selectbox("Convert to:", ["USD", "EUR", "GBP", "JPY"])

if st.button("Convert"):
    url = "https://api.exchangerate-api.com/v4/latest/INR"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        rate = data["rates"][target_currency]
        convert_amount = rate * amount
        st.success(f"{amount} INR = {convert_amount:.2f} {target_currency}")
    else:
        st.error("Failed to fetch conversion rate")