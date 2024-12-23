import os
import time
import FreeSimpleGUI as sg
import functions

if not os.path.exists("processes.txt"):
    with open("processes.txt", "w") as file:
        pass

if not os.path.exists("endProcess.txt"):
    with open("endProcess.txt", "w") as file:
        pass

sg.theme("DarkPurple4")
clock = sg.Text("", key="clock", size=(20, 1))

label = sg.Text("Open a new process")
input_box = sg.InputText(tooltip="Open new process", key="process")
add_button = sg.Button("Open New Process")
list_box = sg.Listbox(
    values=functions.get_processes(), key="processes", enable_events=True, size=[45, 10]
)
edit_button = sg.Button("Update")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")


window = sg.Window(
    "Task Manager",
    layout=[
        [clock],
        [label],
        [input_box, add_button],
        [list_box, edit_button, complete_button],
        [exit_button],
    ],
    font=("Helvetica", 20),
)

while True:
    event, values = window.read(timeout=200)  # Displays window
    print(f"Event triggered: {event}")  # Debugging: log event
    window["clock"].update(value=time.strftime("%b %d, %Y %I:%M %p"))

    match event:
        case "Open New Process":
            processes = functions.get_processes()
            new_processes = values["process"] + "\n"
            processes.append(new_processes)
            functions.write_processes(processes)
            window["processes"].update(values=processes)

        case "Update":
            try:
                process_edit = values["processes"][0]
                new_process = values["process"] + "\n"

                processes = functions.get_processes()
                index = processes.index(process_edit)
                processes[index] = new_process
                functions.write_processes(processes)
                window["processes"].update(values=processes)
            except IndexError:
                sg.popup(
                    "Please select a process first to update.", font=("Helvetica", 20)
                )

        case "Complete":
            try:
                process_complete = values["processes"][0]
                processes = functions.get_processes()
                processes.remove(process_complete)
                functions.write_processes(processes)
                window["processes"].update(values=processes)
                window["process"].update(value="")
            except IndexError:
                sg.popup(
                    "Please select a process first to complete it.",
                    font=("Helvetica", 20),
                )

        case "Exit":
            break

        case "processes":
            window["process"].update(value=values["processes"][0])

        case sg.WIN_CLOSED:  # Closes the program when the red close button is pushed
            break

        case _:
            print(f"Unhandled event: {event}")

window.close()
