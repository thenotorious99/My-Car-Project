import functions
import FreeSimpleGUI as sg
import time

now = time.strftime("%b %d, %Y %H:%M:%S")

sg.theme("BlueMono")

clock = sg.Text("", key="clock")

label = sg.Text("Write kind of car")
input_box = sg.InputText(tooltip="Enter car", key="car")
add_button = sg.Button("Add")
list_box = sg.Listbox(values=functions.get_car(), key="items",
                      enable_events=True, size=[45, 10])

edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")

window = sg.Window("My List Of Cars",
                   layout= [[clock],
                        [label],
                        [input_box, add_button],
                        [list_box], [edit_button, complete_button],
                        [exit_button]],
                   font=("Helvetica", 20))

while True:
    event, values = window.read(timeout=200)
    window["clock"].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
    match event:
        case "Add":
            cars = functions.get_car()
            index = cars.index(cars_to_edit)
            cars[index] = new_cars
            functions.write_cars(cars)
            window['items'].update(values=cars)
