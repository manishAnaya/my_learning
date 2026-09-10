import streamlit as st
import pandas as pd

st.title("File Analysis Dashboard")

st.caption("Upload your file to demonstarte")

st.set_page_config(
    page_title="Sales Dashboard",
    page_icon="📊",
    layout="wide"
)

file = st.file_uploader("Please Upload here", type = ["csv"])

if file:
    df = pd.read_csv(file)  

    # Filtering Sudebars
    st.sidebar.subheader("Filters")
    city = st.sidebar.selectbox("City",["All"] + list(df["City"].unique()))
    category = st.sidebar.selectbox("Category",["All"] + list(df["Category"].unique()))
    payment = st.sidebar.selectbox("Payment",["All"] + list(df["Payment"].unique()))

    # Filtering 
    filtered_df = df.copy()
    if city != "All":
        filtered_df = filtered_df[filtered_df["City"] == city]

    if category != "All":
        filtered_df = filtered_df[filtered_df["Category"] == category]

    if payment != "All":
        filtered_df = filtered_df[filtered_df["Payment"] == payment]

    # Some Metrics
    
    col1, col2, col3 = st.columns(3)

    with col1:  
        st.metric("Orders", len(filtered_df))

    with col2:
        st.metric("Sales", f"₹ {filtered_df['Price'].sum():,.0f}")

    with col3:
        st.metric("Average Ratings", f"{filtered_df['Rating'].mean():,.2f}")

    col1, col2, col3 = st.columns(3)
        
    with col1:
        st.subheader("🏙 Sales by City")
        st.bar_chart(df.groupby("City")["Price"].sum())

    with col2:
        st.dataframe(filtered_df)
        
    with col3:
        st.subheader("💳 Payment Method")
        st.write(df["Payment"].value_counts())
    
    
else:
    st.info("👆 Please upload a CSV file to view the dashboard.")
    