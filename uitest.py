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

        sg.In('URL', size=(25, 1), enable_events=True, key="-DLURL-"),
        sg.Button("Download")

    ],

]



optional_options = [

    [sg.Text("Not functioning currently")],





]


# ----- Full layout -----

layout = [

    [

        sg.Column(essential_options),

        sg.VSeperator(),

        sg.Column(optional_options),

    ]

]


window = sg.Window("ytdl-helper", layout)



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
            'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/mp4',
            'outtmpl': file_output_directory
        }
        if not video_link:
            sg.Popup('No link', 'No valid link entered.')
        else:
            try:
                with youtube_dl.YoutubeDL(dl_opts) as ydl:
                    ydl.download([video_link])
                sg.Popup("Done!", "Video successfully downloaded.")
            except youtube_dl.utils.DownloadError as download_error:
                sg.Popup("Error whilst downloading", "Something went wrong! Check your link and try again.")




window.close()