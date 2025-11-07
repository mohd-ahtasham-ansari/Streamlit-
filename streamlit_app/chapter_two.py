import streamlit as st

st.title("The Chai maker App")

if st.button("Make Chai"):
    st.success("The chai is being brewed")

Add_masala=st.checkbox("Add Masala")
if Add_masala:
    st.write("the masala is added")

chai_base=st.radio("Choose the base of chai",["Milk","Water","Almond milk","Vanilla Milk"])
if chai_base:
    st.write(f" base selected  is : {chai_base}")

Flavour=st.selectbox("Choose flavours :",["Adrak","Long","Tulsi","Elaichi"])
if Flavour:
    st.write(f"Flavour added {Flavour}")

Sugar=st.slider("Add Sugar(Spoon)) ", 0,5,1)
if Sugar:
    st.write(f"sugar spoon {Sugar}")

cups =st.number_input("How many Cups ",min_value=1,max_value=15, step=1)
if cups:
    st.write("Order sucessfull of {cups} cups of tea")

name= st.text_input("Enter your name ")
if name:
    st.write(f"Welcome {name} ! your order is on the way")

DOB= st.date_input("enter your DOB ")
st.write(f"Your DOB is {DOB}")