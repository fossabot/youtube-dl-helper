import PySimpleGUI as sg

print("Successfully loaded library")

window_layout = [[sg.Text('ytdl-helper')], [sg.Button("OK")]]

window = sg.Window('ytdl-helper', window_layout)

while True:
    event, values = window.read()
    if event == "OK" or event == sg.WIN_CLOSED:
        break


window.close()
