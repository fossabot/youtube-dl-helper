from __future__ import unicode_literals
import PySimpleGUI as sg
import youtube_dl
import threading

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


def download_video(resolution, file_dir, subtitles, prefformat, output_type, vid_url):
    vid_dl_opts = {
        'format': 'bestvideo[height<={}]+bestaudio'.format(resolution),
        'outtmpl': file_dir,
        'writesubtitles': subtitles,
        'postprocessors': [{
            'key': 'FFmpegVideoConvertor',
            'preferedformat': prefformat  # avi flv mkv mp4 ogg webm
        }]
    }
    audio_dl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': file_dir,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }]
    }
    output_vid_type = vid_dl_opts if output_type == "Video and audio" else audio_dl_opts
    try:
        with youtube_dl.YoutubeDL(output_vid_type) as ydl:
            ydl.download([vid_url])
        sg.Popup("Done!", "Video successfully downloaded.")
    except youtube_dl.utils.DownloadError as download_error:
        sg.Popup("Error whilst downloading", f'{download_error}')


while True:

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
            download_video(values['-RESCOMBO-'], file_output_directory, values['-SUBS-'], values['-PREFFORMAT-'],
                           values['-OUTPUTTYPE-'], video_link)

window.close()
