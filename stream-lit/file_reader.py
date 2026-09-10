import streamlit as st
import pandas as pd

st.title("Sales Dashboard of Reliance Digital")
file = st.file_uploader("Please upload .csv file", type=["csv"])

if file:
    df = pd.read_csv(file)
    st.subheader("Sales Report")
    st.dataframe(df)

if file:
    cities = df["City"].unique()
    selected_city = st.selectbox("Filter by city", cities)
    filtered_df = df[df["City"] == selected_city]
    st.dataframe(filtered_df)

if file:
    categories = df["Category"].unique()
    selected_category = st.selectbox("Filter by category", categories)
    filtered_df = df[df["Category"] == selected_category]
    st.dataframe(filtered_df)

if file:
    payment = df["Payment"].unique()
    selected_payment = st.selectbox("Filter by Payment Method", payment)
    selected_df = df[df["Payment"] == selected_payment]
    st.dataframe(selected_df)