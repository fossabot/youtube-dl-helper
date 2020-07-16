from __future__ import unicode_literals
import PySimpleGUI as sg
import helpers

sg.ChangeLookAndFeel('LightBrown3')  # Experimental feature. Might change.

essential_options = [

    [

        sg.Text("Download Directory:"),

        sg.In(size=(25, 1), enable_events=True, readonly=True, key="-FOLDER-"),

        sg.FolderBrowse(),

    ],

    [
        sg.Text("YouTube URL:"),
        sg.In(size=(25, 1), enable_events=True, key="-DLURL-"),
        sg.Button("Download")

    ],

    [
        sg.Text("USING THE NIGHTLY FFMPEG BUILD IS HIGHLY RECOMMENDED")
    ]

]

optional_options = [

    [sg.Checkbox('Subtitles (en)?', default=False, key='-SUBS-')],
    [sg.Text("Video Resolution:"),
     sg.Combo(['144', '240', '360', '480', '720', '1080'], enable_events=True,
              readonly=True, default_value='1080', key='-RESCOMBO-')],
    [sg.Text("File Type:"),
     sg.Combo(['Video and audio', 'Audio only'], enable_events=True,
              readonly=True, default_value='Video and audio', key='-OUTPUTTYPE-')],
    [sg.Text("Vid format:"),
     sg.Combo(['mp4', 'mkv', 'flv', 'avi', 'ogg', 'webm'], enable_events=True,
              readonly=True, default_value='mp4', key='-PREFFORMAT-')]

]

layout = [

    [

        sg.Column(essential_options),

        sg.VSeperator(),

        sg.Column(optional_options)

    ]

]
window = sg.Window("youtube-dl-helper", layout)

while True:
    download_thread = None
    event, values = window.read()
    if event == "Exit" or event == sg.WIN_CLOSED:
        break

    if event == "-OUTPUTTYPE-":
        if values['-OUTPUTTYPE-'] == 'Audio only':
            window.FindElement('-PREFFORMAT-').Update(disabled=True)
        else:
            window.FindElement('-PREFFORMAT-').Update(disabled=False)

    if event == "Download":
        video_link = values["-DLURL-"]
        file_output_directory = values["-FOLDER-"]
        if not file_output_directory:
            file_output_directory = "%(title)s.%(ext)s"
        else:
            file_output_directory = file_output_directory + "/%(title)s.%(ext)s"
        if not video_link:
            sg.Popup('No link', 'No valid link entered.')
        else:
            helpers.download_video(values['-RESCOMBO-'], file_output_directory, values['-SUBS-'],
                                   values['-PREFFORMAT-'],
                                   values['-OUTPUTTYPE-'], video_link)

window.close()
