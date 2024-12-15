import streamlit as st
import functions



if "todos" not in st.session_state:
    st.session_state["processes"] = functions.get_processes()

def add_process():
    todo = st.session_state["new_processes"] + "\n"
    st.session_state["processes"].append(process)
    functions.write_processes(st.session_state["processes"])
    st.session_state["new_process"] = ""  # Clear input field

st.title("Task Manager")
st.subheader("Here are my current processes.")
#st.write("This is the list of current processes."+"\n")
st.button(label = "Open new process", on_click = add_process)

#st.text_input(label="", placeholder="Open new process...",
              #on_change=add_todo, key='new_todo')

for index, todo in enumerate(st.session_state["processes"]):
    if st.checkbox(todo, key=f"process_{index}"):
        st.session_state["processes"].pop(index)
        functions.write_processes(st.session_state["processes"])
        break  # Exit the loop to avoid issues with modifying the list


