import streamlit as st
import pandas as pd 

st.title("live Currency Exchange Rate App")
amount = st.number_input("Enter amount in INR", min_value=1)
target_currency = st.selectbox("Select target currency", ["USD", "EUR", "GBP", "JPY", "AUD"])   

if st.button("Convert"):
    url="https://api.exchangerate-api.com/v4/latest/INR"
    response = requests.get(url)