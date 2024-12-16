import streamlit as st
import functions
import complete
import time
from datetime import datetime

if "processes" not in st.session_state or not isinstance(st.session_state["processes"], list):
    st.session_state["processes"] = functions.get_processes()

if "endProcess" not in st.session_state or not isinstance(st.session_state["endProcess"], list):
    st.session_state["endProcess"] = complete.get_endProcess()

if "new_processes" not in st.session_state:
    st.session_state["new_processes"] = ""  # Initialize input value

def add_process():
    process = st.session_state["new_processes"] + "\n"
    st.session_state["processes"].append(process)
    functions.write_processes(st.session_state["processes"])
    st.session_state['new_processes'] = ""

def read_file(file_path):
    """Reads the content of a file and returns it as a list of lines."""
    try:
        with open(file_path, "r") as file:
            return file.readlines()
    except FileNotFoundError:
        return ["File not found."]


def write_file(file_path, content):
    """Writes a list of lines to a file."""
    with open(file_path, "w") as file:
        file.writelines(content)


def mark_as_completed(task):
    """Moves a task from processes.txt to endProcess.txt."""
    # Remove task from processes
    if task in st.session_state["processes"]:
        st.session_state["processes"].remove(task)
        write_file("processes.txt", [t + "\n" for t in st.session_state["processes"]])

    # Add task to endProcess
    if task not in st.session_state["endProcess"]:
        st.session_state["endProcess"].append(task)
        write_file("endProcess.txt", [t + "\n" for t in st.session_state["endProcess"]])


# Get current date and time
currentTime = time.strftime("%I:%M %p")
currentDate = datetime.today().strftime("%m-%d-%Y")

# Streamlit app title
st.title("Task Manager")
st.subheader(f"The current date is: {currentDate}")
st.subheader(f"The current time is: {currentTime}")



# Input for adding new processes
st.text_input(label="", placeholder="Open new process...", key="new_processes",
    on_change=lambda: (
        st.session_state["processes"].append(st.session_state["new_processes"]),
        st.session_state.update({"new_processes": ""})))  # Clear the input field


# Radio button for user selection
columns = st.radio("Select Output Value:", ['Current Processes', 'Processes Completed'], key="selection")

# Dynamically display file contents
if columns == "Current Processes":
    for i, task in enumerate(st.session_state["processes"]):
        col1, col2, col3 = st.columns([3, 1, 1])
        with col1:
            # Display the task with a unique key
            new_value = st.text_input(f"Process {i+1}:", value=task, key=f"task_input_{i}")
        with col2:
            # Update button directly fetches the corresponding textbox value
            if st.button("Update Process", key=f"update_btn_{i}"):
                st.session_state["processes"][i] = new_value
                functions.write_processes(st.session_state["processes"])  # Save updates to the file
        with col3:
            # Complete Process button moves the task
            if st.button("Complete Process", key=f"complete_btn_{i}"):
                st.session_state["endProcess"].append(st.session_state["processes"].pop(i))
                functions.write_processes(st.session_state["processes"])  # Save updated processes
                functions.write_processes(st.session_state["endProcess"])  # Save completed processes

elif columns == "Processes Completed":
    for i, task in enumerate(st.session_state["endProcess"]):
        col1, col2 = st.columns([3, 1])
        with col1:
            # Display the task and allow editing
            new_value = st.text_input(f"Completed Process{i+1}:", task, key=f"edit_completed_{i}_{task}")
        with col2:
            # Save button to update the task
            if st.button("Update Process", key=f"save_completed_{i}_{task}"):
                st.session_state["endProcess"][i] = new_value

# "Exit" button to reset the app
if st.button("Exit"):
    with st.container():
        st.warning("Are you sure you want to exit?")
        if st.button("Yes, exit"):
            st.stop()
        if st.button("No, stay"):
            st.empty()  # Clear the warning message