Task Manager Application

Overview

This Streamlit-based Task Manager Application helps users manage and track tasks in an interactive and user-friendly interface. It allows users to:
	•	Add new tasks (processes).
	•	Mark tasks as completed.
	•	View and update tasks in progress.
	•	View and update completed tasks.
	•	Save task data to files for persistence.

The application dynamically reflects changes to tasks and uses st.session_state for maintaining state across user interactions.

Features
	1.	Add Tasks
	•	Input a new task through a text box.
	•	The task is appended to the Current Processes list.
	2.	Update Tasks
	•	Each task in the “Current Processes” list can be edited and updated.
	3.	Complete Tasks
	•	Tasks in progress can be marked as completed and moved to the Processes Completed list.
	4.	Edit Completed Tasks
	•	Completed tasks can be viewed and modified.
	5.	Persistent Data
	•	Task data is stored in two text files: processes.txt and endProcess.txt.
	6.	Dynamic Time and Date
	•	The current date and time are displayed at the top of the app.
	7.	Exit Option
	•	A simple exit confirmation prompt.

How to Run the App

Prerequisites
	•	Python 3.8 or later
	•	Streamlit library

Installation
	1.	Clone the repository or save the code to a Python file (e.g., task_manager.py)
  2. 	Install Streamlit if it is not already installed
  3. Ensure you have the following two files in the same directory:
    	•	processes.txt (initially empty or with existing processes)
    	•	endProcess.txt (initially empty or with completed processes)
  4. Run the application

  How to Use
	1.	Add a Task:
	•	Use the text input at the top to add a new task.
	•	Press Enter, and the task will appear under “Current Processes.”
	2.	View and Update Tasks:
	•	Under Current Processes, edit tasks using the text boxes.
	•	Click Update Process to save the changes.
	3.	Complete a Task:
	•	Click Complete Process to move a task to the “Processes Completed” list.
	4.	View and Edit Completed Tasks:
	•	Switch to Processes Completed via the radio button.
	•	Update completed tasks using the available text boxes.
	5.	Exit the Application:
	•	Click the Exit button and confirm the exit.

Notes
	•	Make sure the processes.txt and endProcess.txt files are writable.
	•	State management is handled using st.session_state for better interactivity.
