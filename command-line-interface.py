from functions import get_todos, write_todos
import time

now = time.strftime("%b-%d-%Y %H:%M:%S %p")
print("It is", now)


while True:
    user_action = input("Type add, show, edit, complete or exit:")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:]

        todos = get_todos()

        todos.append(todo + '\n')

        write_todos(todos)

    elif user_action.startswith("show"):
        todo = user_action[4:]

        todos = get_todos()

        #new_todos = [item.strip('\n') for item in todos] this is list comprehension

        for index, item in enumerate(todos):
            item = item.strip('\n') #same as line 23
            row = f"{index + 1}-{item}"
            print(row)

    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            number = number - 1

            todos = get_todos()

            new_todo = input("Enter new todo:")
            todos[number] = new_todo + '\n'

            write_todos(todos)

        except ValueError:
            print("Your command is not valid.")
            continue #this starts the loop for the beginning

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])

            todos = get_todos()

            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            write_todos(todos)

            message = f"Todo {todo_to_remove} was completed from the list."
            print(message)

        except IndexError:
            print("There is no item with that number.")
            continue

    elif user_action.startswith("exit"):
        break

    else:
        print("Incorrect command was entered")

print("Bye!")
