import functions
import PySimpleGUI as gui
import time
import os
#pyinstaller --onefile --windowed --clean gui.py
if not os.path.exists("todos.txt"):
      with open("todos.txt","w") as file:
            pass

clock = gui.Text("",key="Clock")
label = gui.Text("Type in a reminder")
input_box = gui.InputText(tooltip="Enter reminder", key="todo")
add_button = gui.Button("Add")
list_box = gui.Listbox(values=functions.get_todos(), key="todos", 
                       enable_events=True, size=[45,10])
edit_button = gui.Button("Edit")
complete_button = gui.Button("Complete")
exit_button = gui.Button("Exit")
window = gui.Window("Reminder App", 
                    layout=[[clock], [label],[input_box,add_button], 
                            [list_box,edit_button,complete_button],[exit_button]], 
                    font=("Helvetica",20)) 
while True:
    event, values = window.read(timeout=200)
    match event:
        case "Add":
            if not values["todo"]:
                gui.popup("Please type something first",font=("helvetica",20))
                continue
            todos = functions.get_todos()
            new_todo = values["todo"] +"\n"
            todos.append(new_todo)
            functions.set_todos(todos)
            window["todos"].update(values=todos)
            window["todo"].update(value="")
        case "Edit":
            try:
                todos = functions.get_todos()
                index = todos.index(values["todos"][0])
                todos[index] = values["todo"] +"\n"
                functions.set_todos(todos)
                window["todos"].update(values=todos)
            except IndexError:
                gui.popup("Please select an item first",font=("helvetica",20))
        
        case "todos":
            if values["todos"]:
                window["todo"].update(value=values["todos"][0])

        case "Complete":
            try:
                todo = values["todos"][0]
                todos = functions.get_todos()
                todos.remove(todo)
                functions.set_todos(todos)
                window["todos"].update(values=todos)
                window["todo"].update(value="")
            except IndexError:
                gui.popup("Please select an item first",font=("helvetica",20))

        case "Exit":
            break

        case gui.WIN_CLOSED:
            break
        case gui.WINDOW_CLOSED:
            break
    window["Clock"].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
window.close()