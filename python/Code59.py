import PySimpleGUI
label=PySimpleGUI.Text(" Type in a to-do")
input_box=PySimpleGUI.InputText(tooltip="Enter tod")
add_button= PySimpleGUI.Button("Add")


window=PySimpleGUI.Window('HI This is ASshwin',layout=[[label],[input_box],[add_button]])
window.read()
window.close()

