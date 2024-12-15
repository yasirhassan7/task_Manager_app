FILEPATH = "processes.txt"

def get_processes(filepath=FILEPATH):
    with open(filepath, 'r') as file_local:
        processes_local = file_local.readlines()
    return processes_local

def write_processes(processes_arg, filepath=FILEPATH):
    with open(filepath, 'w') as file:
        file.writelines(processes_arg)





