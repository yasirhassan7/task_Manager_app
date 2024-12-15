FILEPATH = "processes.txt"

def get_processes(filepath=FILEPATH):
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local

def write_processes(todos_arg, filepath=FILEPATH, processes_arg=None):
    with open(filepath, 'w') as file:
        file.writelines(processes_arg)