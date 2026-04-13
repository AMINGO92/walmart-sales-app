import streamlit as st
import joblib
import pandas as pd

st.title("Walmart Sales Prediction App")

model = joblib.load("sales_model.pkl")

st.header("Enter Details")

store = st.number_input("Store", 1, 50)
dept = st.number_input("Dept", 1, 100)
size = st.number_input("Size", 1000, 200000)
week = st.number_input("Week", 1, 52)
cpi = st.number_input("CPI", 100.0, 300.0)


if st.button("Predict Sales"):
    data = pd.DataFrame({
        'Store': [store],
        'Dept': [dept],
        'Size': [size],
        'Week': [week],
        'CPI': [cpi],
    })

    prediction = model.predict(data)

    st.success(f"Predicted Sales: {prediction[0]:.2f}")