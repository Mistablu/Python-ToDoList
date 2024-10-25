
while True:
    todo = input("Type 'add', 'show', 'edit', 'complete', or 'exit': ")
    match todo.lower().strip():
        case "add":
            todo = input("Enter a todo: ") + "\n"

            file = open(r"files\todos.txt","r")
            todos = file.readlines()
            file.close()

            todos.append(todo)

            file = open(r"files\todos.txt","w")
            file.writelines(todos)
            file.close()

            print("Added")

        case "show":
            file = open(r"files\todos.txt","r")
            todos = file.readlines()
            file.close()

            for index, item in enumerate(todos):
                print(f"{index+1}.{item.title()}")

        case "edit":
            number = int(input("Input number to be edited: "))
            todos[number-1] = input("Enter new todo: ")
            print("Edit successful")

        case "complete":
            number = int(input("Input number completed: "))
            todos.pop(number-1)

        case "exit":
            print("Goodbye")
            break

        case _:
            print("Invalid Input")