FILEPATH = "endProcess.txt"

def get_endProcess(filepath=FILEPATH):
    with open(filepath, 'r') as file_local:
        endProcess_local = file_local.readlines()
    return endProcess_local

def write_endProcess(endProcess_arg, filepath=FILEPATH):
    with open(filepath, 'w') as file:
        file.writelines(endProcess_arg)