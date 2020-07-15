from __future__ import unicode_literals
import PySimpleGUI as sg
import youtube_dl

essential_options = [

    [

        sg.Text("Download Directory:"),

        sg.In(size=(25, 1), enable_events=True, key="-FOLDER-"),

        sg.FolderBrowse(),

    ],

    [
        sg.Text("YouTube URL:"),
        sg.In(size=(25, 1), enable_events=True, key="-DLURL-"),
        sg.Button("Download")

    ],

]

optional_options = [

    [sg.Checkbox('Subtitles (en)?', default=False, key='-SUBS-')],
    [sg.Text("Video Resolution:"),
    sg.Combo(['144', '240', '360', '480', '720', '1080'], enable_events=True, default_value=1080, key='-RESCOMBO-')]

]

layout = [

    [

        sg.Column(essential_options),

        sg.VSeperator(),

        sg.Column(optional_options),

    ]

]

window = sg.Window("youtube-dl-helper", layout)

while True:

    event, values = window.read()

    if event == "Exit" or event == sg.WIN_CLOSED:
        break
    if event == "Download":

        video_link = values["-DLURL-"]
        print(video_link)
        file_output_directory = values["-FOLDER-"]
        if not file_output_directory:
            file_output_directory = "%(title)s.%(ext)s"
        else:
            file_output_directory = file_output_directory + "/%(title)s.%(ext)s"
        dl_opts = {
            'format': 'bestvideo[height<={}]+bestaudio'.format(values["-RESCOMBO-"]),
            'outtmpl': file_output_directory,
            'writesubtitles': values["-SUBS-"]
        }
        if not video_link:
            sg.Popup('No link', 'No valid link entered.')
        else:
            try:
                with youtube_dl.YoutubeDL(dl_opts) as ydl:
                    ydl.download([video_link])
                sg.Popup("Done!", "Video successfully downloaded.")
            except youtube_dl.utils.DownloadError as download_error:
                sg.Popup("Error whilst downloading", f'{download_error}')

window.close()
