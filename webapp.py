import streamlit as st
import functions

todos = functions.get_todos()
st.title("my todo app")
st.subheader("this is my todo app")
st.write("This app helps productivity")

for todo in todos:
    st.checkbox(todo)

st.text_input(label="Enter a todo:",placeholder="New todo...") 
