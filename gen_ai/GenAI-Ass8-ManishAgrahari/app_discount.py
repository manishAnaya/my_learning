import streamlit as st

st.title("Price Calculator")

product_price = st.number_input(
    "Enter Product Price",
    min_value=0.0,
    value=1000.0,
    step=100.0
)

discount = st.slider(
    "Discount (%)",
    min_value=0,
    max_value=50,
    value=10
)

if st.button("Calculate"):

    disc_price = product_price - (product_price * discount / 100)
    st.success(f"Product price after {discount}% discount is Rs.{disc_price:.2f}")

    st.table([
        ["Original Price", f"{product_price}"],
        ["Discount (%)", discount],
        ["Final Price", disc_price]
    ])