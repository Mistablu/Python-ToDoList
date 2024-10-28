import streamlit as st
import functions

todos = functions.get_todos()

def add_todo():
    todo = st.session_state["input_box"]+"\n"
    todos.append(todo)
    functions.set_todos(todos)
    


st.title("my todo app")
st.subheader("this is my todo app")
st.write("This app helps productivity")

for index,todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.set_todos(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label="Enter a todo:",placeholder="New todo...", 
              on_change=add_todo, key="input_box") 
