import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Sales Dashboard",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Sales Dashboard - Reliance Digital")

uploaded_file = st.file_uploader(
    "Upload Sales CSV File",
    type=["csv"]
)

if uploaded_file:

    # Read CSV
    df = pd.read_csv(uploaded_file)

    # Convert Date
    df["Order Date"] = pd.to_datetime(df["Order Date"])

    st.sidebar.header("🔍 Filters")

    # -------------------------------
    # Sidebar Filters
    # -------------------------------

    city = st.sidebar.selectbox(
        "Select City",
        ["All"] + list(df["City"].unique())
    )

    category = st.sidebar.selectbox(
        "Select Category",
        ["All"] + list(df["Category"].unique())
    )

    payment = st.sidebar.selectbox(
        "Select Payment",
        ["All"] + list(df["Payment"].unique())
    )

    # -------------------------------
    # Filtering
    # -------------------------------

    filtered_df = df.copy()

    if city != "All":
        filtered_df = filtered_df[
            filtered_df["City"] == city
        ]

    if category != "All":
        filtered_df = filtered_df[
            filtered_df["Category"] == category
        ]

    if payment != "All":
        filtered_df = filtered_df[
            filtered_df["Payment"] == payment
        ]

    # -------------------------------
    # Metrics
    # -------------------------------

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "🛒 Total Orders",
            len(filtered_df)
        )

    with col2:
        st.metric(
            "💰 Total Sales",
            f"₹ {filtered_df['Price'].sum():,.0f}"
        )

    with col3:
        st.metric(
            "⭐ Average Rating",
            round(filtered_df["Rating"].mean(), 2)
        )

    st.divider()

    # -------------------------------
    # Filtered Data
    # -------------------------------

    st.subheader("📄 Sales Report")

    st.dataframe(
        filtered_df,
        use_container_width=True
    )

    # -------------------------------
    # Charts
    # -------------------------------

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("🏙 Sales by City")

        city_sales = (
            filtered_df.groupby("City")["Price"]
            .sum()
        )

        st.bar_chart(city_sales)

    with col2:

        st.subheader("💳 Payment Method")

        payment_data = (
            filtered_df["Payment"]
            .value_counts()
        )

        st.write(payment_data)

    st.subheader("📈 Daily Sales Trend")

    daily_sales = (
        filtered_df.groupby("Order Date")["Price"]
        .sum()
    )

    st.line_chart(daily_sales)

    # -------------------------------
    # Download CSV
    # -------------------------------

    csv = filtered_df.to_csv(index=False)

    st.download_button(
        label="⬇ Download Filtered Data",
        data=csv,
        file_name="filtered_sales.csv",
        mime="text/csv"
    )

else:
    st.info("👆 Please upload a CSV file to view the dashboard.")