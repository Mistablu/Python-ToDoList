def get_todos(filepath=r"todos.txt"):
    """"""
    with open(filepath,"r") as file:
            lines = file.readlines()
    return lines

def set_todos(lines,filepath=r"todos.txt"):
    """"""
    with open(filepath,"w") as file:
            file.writelines(lines)

