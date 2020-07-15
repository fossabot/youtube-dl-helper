"""
This version is no longer actively developed. If you are building the project, please use main;py as that'll receive future patches and 
feature enhancements.
"""


from __future__ import unicode_literals
import PySimpleGUI as sg
import youtube_dl

sg.ChangeLookAndFeel('LightGrey2')  # Set theme (https://i.imgur.com/h1SuuOM.png)

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

    ]

]

optional_options = [

    [sg.Checkbox('Subtitles (en)?', default=False, key='-SUBS-')],
    [sg.Text("Video Resolution:"),
     sg.Combo(['144', '240', '360', '480', '720', '1080'], enable_events=True,
              readonly=True, default_value='1080', key='-RESCOMBO-')],
    [sg.Combo(['Video and audio', 'Audio only'], enable_events=True,
              readonly=True, default_value='Video and audio', key='-OUTPUTTYPE-')]

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

    event, values = window.read()

    if event == "Exit" or event == sg.WIN_CLOSED:
        break
    if event == "Download":
        output_type = None
        video_link = values["-DLURL-"]
        print(video_link)
        file_output_directory = values["-FOLDER-"]
        if not file_output_directory:
            file_output_directory = "%(title)s.%(ext)s"
        else:
            file_output_directory = file_output_directory + "/%(title)s.%(ext)s"
        vid_dl_opts = {
            'format': 'bestvideo[height<={}]+bestaudio'.format(values["-RESCOMBO-"]),
            'outtmpl': file_output_directory,
            'writesubtitles': values["-SUBS-"]
        }
        audio_dl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': file_output_directory,
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }]
        }

        output_type = vid_dl_opts if values['-OUTPUTTYPE-'] == "Video and audio" else audio_dl_opts

        if not video_link:
            sg.Popup('No link', 'No valid link entered.')
        else:
            try:
                with youtube_dl.YoutubeDL(output_type) as ydl:
                    ydl.download([video_link])
                sg.Popup("Done!", "Video successfully downloaded.")
            except youtube_dl.utils.DownloadError as download_error:
                sg.Popup("Error whilst downloading", f'{download_error}')

window.close()
