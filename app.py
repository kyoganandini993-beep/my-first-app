
import streamlit as st

st.title("My First App 🌟")

st.write("Welcome to my app!")

name = st.text_input("Enter your name")

if name:
    st.success(f"Hello, {name}!")

st.balloons()
