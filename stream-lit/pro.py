import streamlit as st
import pandas as pd

st.set_page_config(
    page_title = "Sales Dashboard",
    page_icon = "📊",
    layout = "wide"
)

st.title("📊 Sales Dashboard - Reliance Digital")

file = st.file_uploader("Upload Sales CSV File", type = ["csv"])

if file:
    df = pd.read_csv(file)

    # Sidebar
    st.sidebar.header("🔍 Filters")

    city = st.sidebar.selectbox("Select City",["All"] + list(df["City"].unique()))
    category = st.sidebar.selectbox("Select Category",["All"] + list(df["Category"].unique()))
    payment = st.sidebar.selectbox("Select Payment",["All"] + list(df["Payment"].unique()))

    # Filtering
    filtered_df = df.copy()

    if city != "All":
        filtered_df = filtered_df[filtered_df["City"] == city]
    if category != "All":
        filtered_df = filtered_df[filtered_df["Category"] == category]
    if payment != "All":
        filtered_df = filtered_df[filtered_df["Payment"] == payment]

    st.divider()
    
    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("🛒 Total Orders", len(filtered_df))
    with col2:
        st.metric("💰 Total Sales", f" Rs.{filtered_df["Price"].sum():.2f}")
    with col3:
        st.metric("⭐ Average Rating", round(filtered_df["Rating"].mean(), 2))

    st.divider()

    st.dataframe(filtered_df)