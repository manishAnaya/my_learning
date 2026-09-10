import streamlit as st

age = st.number_input("Age", 18, 100)
income = st.number_input("Income", 0)

if st.button("Predict"):
    # features = preprocess(age, income)
    # prediction = model.predict(features)
    prediction = "Example result"

    st.success(prediction)