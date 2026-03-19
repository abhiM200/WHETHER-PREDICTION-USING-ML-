import streamlit as st
import pandas as pd

st.title("Weather Prediction App")

temp = st.number_input("Temperature")
humidity = st.number_input("Humidity")

if st.button("Predict"):
    result = "Rainy"  # replace with your ML model
    st.success(f"Prediction: {result}")
