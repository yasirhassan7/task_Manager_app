#Task Manager Application
This is a web app to showcase my Task Manager app and how it operates. 

Overview

##This Streamlit-based Task Manager Application helps users manage and track tasks in an interactive and user-friendly interface. It allows users to:
	•	Add new tasks (processes).
	•	Mark tasks as completed.
	•	View and update tasks in progress.
	•	View and update completed tasks.
	•	Save task data to files for persistence.

##The application dynamically reflects changes to tasks and uses st.session_state for maintaining state across user interactions.

##Features
	1.	Add Tasks
	•	Input a new task through a text box.
	•	The task is appended to the “Current Processes” list.
	2.	Update Tasks
	•	Edit and update tasks in the “Current Processes” list.
	3.	Complete Tasks
	•	Mark tasks in progress as completed and move them to the “Processes Completed” list.
	4.	Edit Completed Tasks
	•	View and modify tasks in the “Processes Completed” list.
	5.	Persistent Data
	•	Task data is stored in two text files:
	•	processes.txt (for tasks in progress)
	•	endProcess.txt (for completed tasks)
	6.	Dynamic Time and Date
	•	Displays the current date and time at the top of the app.
	7.	Exit Option
	•	A simple exit confirmation prompt.

 ##Prerequisites
	•	Python 3.8 or later
	•	Streamlit library

 ##Installation
	1.	Clone the Repository:
 			git clone <repository_url>
			cd <repository_folder>

   
**	2.	Install Streamlit:
 			pip install streamlit

   **	3.	Prepare Required Files:
		•	Ensure the following files exist in the project directory:
		•	processes.txt (initially empty or pre-filled with tasks)
		•	endProcess.txt (initially empty or pre-filled with completed tasks)
	4.	Run the Application:
				streamlit run web.py


##How to Use
	1.	Add a Task:
	•	Use the text input box at the top to add a new task.
	•	Press Enter, and the task will appear under “Current Processes.”
	2.	View and Update Tasks:
	•	Under the “Current Processes” section, edit tasks using the provided text boxes.
	•	Click Update Process to save changes.
	3.	Complete a Task:
	•	Click Complete Process next to a task to move it to the “Processes Completed” list.
	4.	View and Edit Completed Tasks:
	•	Use the radio button to switch to the “Processes Completed” section.
	•	Update completed tasks using the text boxes.
	5.	Exit the Application:
	•	Click the Exit button and confirm the exit prompt.


##Notes
	•	Ensure the processes.txt and endProcess.txt files are writable.
	•	State Management:
	•	The app uses st.session_state to maintain state across user interactions.
	•	Dynamic Updates:
	•	Changes to tasks are reflected in real-time.


 
##Example Command

###To run the app locally:
		streamlit run web.py

  Replace <repository_url> and <repository_folder> with the appropriate GitHub repository URL and folder name.
 
 **
