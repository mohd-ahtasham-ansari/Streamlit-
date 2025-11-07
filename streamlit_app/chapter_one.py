import streamlit as st

st.title("this is title")
st.subheader('this is subheader')
st.text('this is text')
st.write('this is write')

#make a slectbox for your favorite language

Programming_Language = st.selectbox("Choose your favorite Programing language :", ["Python", "C++","Java", "C", "other"])

st.write(f" You have selected {Programming_Language} , Excellent choice")

st.success("you have been assigned project of your favorite language")