import streamlit as st

st.title("Power Calculator")
st.write("Enter the number whose square, cube, and fifth power you want to calculate.")

n = st.number_input("Enter a integer", value=1, step=1)

square = n ** 2
cube = n ** 3
fifth_power = n ** 5


st.write(f"The square of {n} is : {square}")
st.write(f"The cube of {n} is : {cube}")
st.write(f"The fifth power of {n} is : {fifth_power}")