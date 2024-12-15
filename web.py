import streamlit as st
import functions
import complete
import time
from datetime import datetime

currentTime = time.strftime("%I:%M %p")
currentDate = datetime.today().strftime("%m-%d-%Y")
# Initialize session state variables
if "processes" not in st.session_state:
    st.session_state["processes"] = functions.get_processes()

if "endProcess" not in st.session_state:
    st.session_state["endProcess"] = complete.get_endProcess()

list_files = {'Current Processes': 'processes.txt', 'Processes Completed': 'endProcess.txt'}

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


# Streamlit app title
st.title("Task Manager")
st.subheader(f"The current date is: {currentDate}")
st.subheader(f"The current time is: {currentTime}")
st.text_input(label="", placeholder="Open new process...",
              on_change=add_process, key="new_processes")
# Radio button for user selection
columns = st.radio("Select Output Value:", ['Current Processes', 'Processes Completed'])

# Dynamically display file contents
if columns == "Current Processes":
    for i, task in enumerate(st.session_state["processes"]):
        if st.checkbox(task, key=f"current_{i}_{task}"):
            mark_as_completed(task)

elif columns == "Processes Completed":
    for task in st.session_state["endProcess"]:
        st.text(task)
