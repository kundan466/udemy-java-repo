import PySimpleGUI as sg 

label1=sg.Text("Select file to compress:-")
input1=sg.Input()
choose_button=sg.FileBrowse("choose")

label2=sg.Text("selet destination folder:-")

input2=sg.Input()
choose_button2=sg.FolderBrowse("choose")
compress_but=sg.Button("compressor")

window=sg.Window("File compressor", layout=[[label1,input1,choose_button],
                                            [label2,input2,choose_button2],
                                            [compress_but]])

window.read()
window.close()

