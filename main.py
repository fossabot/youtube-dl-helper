"""
This file handles all of the GUI. When buttons are clicked, events are called. Helpers.py performs the actual downloading
"""
from __future__ import unicode_literals
import PySimpleGUI as sg
import helpers
import pytube
from pytube import YouTube

sg.ChangeLookAndFeel('LightBrown3')  # Experimental feature. Might change.

local_version = "2.0"
dev_version = False  # Set to false to override dev check


essential_options = [
    [
        sg.Text("Download Directory:"),

        sg.In(size=(25, 1), enable_events=True, readonly=True, key="-FOLDER-"),

        sg.FolderBrowse(),

    ],

    [
        sg.Text("YouTube URL:"),
        sg.In(size=(25, 1), enable_events=True, key="-DLURL-"),
        sg.Button("Check")

    ],


    [sg.Text("Video Title: ", key='-VIDEOTITLE-', size=(40, 1))],



    [sg.Button("Download", disabled=True, key='-DLBUTTON-')],

    [sg.Text(f'Version {local_version}')]

]

optional_options = [

    [sg.Checkbox('Subtitles (en)?', default=False, key='-SUBS-')],
    [sg.Text("Video Resolution:"),
     sg.Combo(['144p', '240p', '360p', '480p', '720p', '1080p'], enable_events=True,
              readonly=True, key='-RESCOMBO-')],
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
helpers.check_version(local_version, dev_version)

while True:
    event, values = window.read(timeout=1000)
    if event == "Exit" or event == sg.WIN_CLOSED:
        break

    if event == "-OUTPUTTYPE-":
        if values['-OUTPUTTYPE-'] == 'Audio only':
            window.FindElement('-PREFFORMAT-').Update(disabled=True)
        else:
            window.FindElement('-PREFFORMAT-').Update(disabled=False)

    if event == "Check":
        try:
            video_link = YouTube(values['-DLURL-'])
            window.FindElement("-VIDEOTITLE-").Update(video_link.title)
            window.FindElement("-DLBUTTON-").Update(disabled=False)
            resolutions_available = helpers.calculate_available_resolutions(video_link)
            window.FindElement("-RESCOMBO-").Update(values=resolutions_available)
            if video_link.age_restricted:
                print("[WARN] Video is age restricted. The download MAY fail.")
                age_restricted = True
                sg.popup("Warning", "Video is age restricted. Download MAY fail.")

        except pytube.exceptions.RegexMatchError as invalid_url_error:
            print("[ERROR] Invalid URL")
            sg.Popup("Error", "Invalid URL, check and try again.")

    if event == "-DLBUTTON-":
        video_link = values["-DLURL-"]
        file_output_directory = helpers.calculate_directory(values["-FOLDER-"])
        helpers.download_video(values['-RESCOMBO-'], file_output_directory, values['-SUBS-'],
                               values['-PREFFORMAT-'],
                               values['-OUTPUTTYPE-'], video_link)
        window.FindElement('-DLBUTTON-').Update(disabled=True)


window.close()
