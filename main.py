def get_todos(filepath=r"files\todos.txt"):
    with open(filepath,"r") as file:
            lines = file.readlines()
    return lines

def set_todos(lines,filepath=r"files\todos.txt"):
    with open(filepath,"w") as file:
            file.writelines(lines)

while True:
    user_action = input("Type 'add', 'show', 'edit', 'complete', or 'exit': ").strip()

    if user_action.startswith("add"):
        todo = user_action[4:]
        todos = get_todos()
        todos.append(todo+"\n")
        set_todos(todos)
        print("Added")

    elif user_action.startswith("show"):
        todos = get_todos()
        for index, item in enumerate(todos):
            item = item.strip('\n')
            print(f"{index+1}.{item.title()}")

    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            todos = get_todos()
            todos[number-1] = input("Enter new todo: ") + "\n"
            set_todos(todos)
            print("Edit successful")
        except ValueError:
            print("Invalid input")
            continue

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])
            todos = get_todos()
            todos.pop(number-1)
            set_todos(todos)
            print("Removed!")
        except IndexError:
            print("This number does not exist")
            continue
        except ValueError:
            print("Invalid input")
            continue

    elif user_action.startswith("exit"):
        print("Goodbye")
        break

    else:
        print("Invalid command")
