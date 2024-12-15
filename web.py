import streamlit as st
import functions



if "todos" not in st.session_state:
    st.session_state["todos"] = functions.get_todos()

def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    st.session_state["todos"].append(todo)
    functions.write_todos(st.session_state["todos"])
    st.session_state["new_todo"] = ""  # Clear input field

st.title("My Todo App")
st.subheader("This is my todo app.")
st.write("This app is to increase your productivity."+"\n")
st.text_input(label="", placeholder="Add new todo...",
              on_change=add_todo, key='new_todo')

for index, todo in enumerate(st.session_state["todos"]):
    if st.checkbox(todo, key=f"todo_{index}"):
        st.session_state["todos"].pop(index)
        functions.write_todos(st.session_state["todos"])
        break  # Exit the loop to avoid issues with modifying the list


