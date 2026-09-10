import streamlit as st
st.sidebar.title("Product Form")

name = st.sidebar.text_input("Enter Product Name")

category = st.sidebar.selectbox("Select Category", ["Dairy", "Electronics", "Grocery", "Clothing"])

price = st.sidebar.number_input("Enter Product Price", min_value=1)

if st.sidebar.button("Add Product"):
    st.success("Product Added Successfully!")
    st.subheader("Product Details")
    st.write(f"**Product Name:** {name}")
    st.write(f"**Category:** {category}")
    st.write(f"**Price:** Rs.{price}")