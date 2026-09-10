import streamlit as st

st.title("Simple Sales Dashboard")
st.caption("Select a month to view its sales.")

selected_month = st.selectbox("Select Month", ["January", "February", "March", "April"])

sales = {
    "January": 1200,
    "February": 1500,
    "March": 900,
    "April": 2000
}

month_sale = sales[selected_month]

st.metric("Selected Month Sales", month_sale)

st.subheader("Sales Summary")
st.bar_chart(list(sales.values()))