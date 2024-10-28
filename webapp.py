import streamlit as st
import functions

def add_todo():
    todo = st.session_state["input_box"]+"\n"
    todos.append(todo)
    functions.set_todos(todos)

todos = functions.get_todos()
st.title("my todo app")
st.subheader("this is my todo app")
st.write("This app helps productivity")

for todo in todos:
    st.checkbox(todo)

st.text_input(label="Enter a todo:",placeholder="New todo...", 
              on_change=add_todo, key="input_box") 
