import youtube_dl
import PySimpleGUI as sg


#  Video download function

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
    sg.PopupAnimated(sg.DEFAULT_BASE64_LOADING_GIF, background_color='orange', time_between_frames=100)
    try:
        with youtube_dl.YoutubeDL(output_vid_type) as ydl:
            ydl.download([vid_url])
            sg.PopupAnimated(None)
            sg.Popup("Success", "Video Downloaded!")
    except youtube_dl.utils.DownloadError as download_error:
        sg.PopupAnimated(None)
        sg.Popup("Download error!", f"{download_error}")


def calculate_directory(user_output_directory):
    if not user_output_directory:
        user_output_directory = "%(title)s.%(ext)s"
    else:
        user_output_directory = user_output_directory + "/%(title)s.%(ext)s"
    return user_output_directory
