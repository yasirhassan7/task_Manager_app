import time
from functions import get_processes, write_processes


now = time.strftime("%b-%d-%Y %H:%M:%S %p")
print("It is", now)


while True:
    user_action = input("Type add, show, edit, complete or exit:")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        process = user_action[4:]

        processes= get_processes()

        processes.append(process + '\n')

        write_processes(processes)

    elif user_action.startswith("show"):
        try:
            process = user_action[4:]

            processes = get_processes()

            #new_processes = [item.strip('\n') for item in processes] #this is list comprehension

            for index, item in enumerate(processes):
                item = item.strip('\n') #same as line 23
                row = f"{index + 1}-{item}"
                print(row)



        except IndexError:
            print("There is nothing currently processing. Please open a new process by adding a new process")
        continue


    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            number = number - 1

            processes = get_processes()

            new_process = input("Update process:")
            processes[number] = new_process + '\n'

            write_processes(processes)

        except ValueError:
            print("Your command is not valid.")
            continue #this starts the loop for the beginning

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])

            processes = get_processes()

            index = number - 1
            process_to_remove = processes[index].strip('\n')
            processes.pop(index)

            write_processes(processes)

            message = f"Process {process_to_remove} was completed from the list."
            print(message)

        except IndexError:
            print("There is no item with that number.")
            continue

    elif user_action.startswith("exit"):
        break

    else:
        print("Incorrect command was entered")

print("Bye!")
