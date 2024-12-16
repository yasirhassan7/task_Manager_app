import streamlit as st
import functions
import complete
import time
from datetime import datetime

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
        write_file("endProcess.txt", [t for t in st.session_state["endProcess"]])

def initialize_state():
    """Initializes session state variables."""
    if "processes" not in st.session_state or not isinstance(st.session_state["processes"], list):
        st.session_state["processes"] = functions.get_processes()

    if "endProcess" not in st.session_state or not isinstance(st.session_state["endProcess"], list):
        st.session_state["endProcess"] = complete.get_endProcess()

    if "new_processes" not in st.session_state:
        st.session_state["new_processes"] = ""  # Initialize input value

    if "reset_flag" not in st.session_state:
        st.session_state["reset_flag"] = False  # Used to track resets

def reset_app():
    """Triggers a reset by toggling the reset flag."""
    st.session_state["reset_flag"] = True  # Mark reset requested

# Run initialization
initialize_state()

# Handle reset logic
if st.session_state["reset_flag"]:
    # Reinitialize state variables
    st.session_state["processes"] = functions.get_processes()
    st.session_state["endProcess"] = complete.get_endProcess()
    st.session_state["new_processes"] = ""  # Clear input field
    st.session_state["reset_flag"] = False  # Reset the flag

# Get current date and time
currentTime = time.strftime("%I:%M %p")
currentDate = datetime.today().strftime("%m-%d-%Y")

# Streamlit app title
st.title("Task Manager")
st.subheader(f"The current date is: {currentDate}")
st.subheader(f"The current time is: {currentTime}")



# Input for adding new processes
st.text_input(
    label="",
    placeholder="Open new process...",
    on_change=lambda: st.session_state["processes"].append(st.session_state["new_processes"]),
    key="new_processes"
)

# Radio button for user selection
columns = st.radio("Select Output Value:", ['Current Processes', 'Processes Completed'], key="selection")

# Dynamically display file contents
if columns == "Current Processes":
    for i, task in enumerate(st.session_state["processes"]):
        col1, col2, col3 = st.columns([3, 1, 1])
        with col1:
            # Display the task and allow editing
            new_value = st.text_input(f"Process {i+1}:", task, key=f"edit_current_{i}_{task}")
        with col2:
            # Save button to update the task
            if st.button("Update Process", key=f"save_current_{i}_{task}"):
                st.session_state["processes"][i] = new_value
        with col3:
            # Complete Process button to move the task
            if st.button("Complete Process", key=f"complete_current_{i}_{task}"):
                st.session_state["endProcess"].append(st.session_state["processes"].pop(i))

elif columns == "Processes Completed":
    for i, task in enumerate(st.session_state["endProcess"]):
        col1, col2 = st.columns([3, 1])
        with col1:
            # Display the task and allow editing
            new_value = st.text_input(f"Task {i+1}:", task, key=f"edit_completed_{i}_{task}")
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