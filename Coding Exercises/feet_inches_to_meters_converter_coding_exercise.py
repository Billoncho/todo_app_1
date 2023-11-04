import PySimpleGUI as sg
from meters_converter import convert

label1 = sg.Text("Enter feet: ")
input1 = sg.Input(key="feet")

label2 = sg.Text("Enter inches:")
input2 = sg.Input(key="inches")

convert_button = sg.Button("Convert")
convert_label = sg.Text(key="convert")

window = sg.Window("Converter",
                   layout=[[label1, input1],
                           [label2, input2],
                           [convert_button, convert_label]])
while True:
    event, values = window.read()
    feet = float(values["feet"])
    inches = float(values["inches"])
    #total_inches = (feet * 12) + inches
    #meters = round(total_inches / 39.3701, 3)
    result = convert(feet, inches)
    window["convert"].update(f"{result} m", text_color="white")

window.close()
