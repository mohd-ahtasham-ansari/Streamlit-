import streamlit as st
import pandas as pd

st.title("Streamlit Progress Bar Example")

file = st.file_uploader("Upload a CSV file", type=["csv"])

if file:
    df=pd.read_csv(file)
    st.write("Data preview")
    st.dataframe(df)

if file:
    st.subheader("Summary preview")
    st.write(df.describe())
if file:
    math_score=df["math score"].unique()
    selected_score = st.selectbox("filter by math score",math_score)
    filtered_score=df[df["math score"]==selected_score]
    st.dataframe(filtered_score)