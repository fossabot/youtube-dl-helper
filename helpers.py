from pytube import YouTube
import PySimpleGUI as sg
import requests
import time
from pyffmpeg import FFmpeg
import os

def check_version(local_version, dev_version):
    response = requests.get("https://raw.githubusercontent.com/wbnk/youtube-dl-helper/master/release_version.txt")
    data = response.text
    server_version = data[0] + data[1] + data[2]
    if not dev_version:
        if server_version != local_version:
            sg.Popup("Out of date", """A newer version is available at Github! Update the software
                     to receive the latest feature updates.""")
            return False
        return True
    print("dev version! skipping update check.")
    return "dev-ver"


def download_video(resolution, file_dir, subtitles, prefformat, output_type, vid_url):
    ff = FFmpeg()
    current_time = int(time.time())
    video = YouTube(vid_url)
    if not file_dir:
        print("not file dir.")
    else:
        print(file_dir)
    download_object = video.streams.filter(resolution=resolution,
                                           file_extension="mp4", progressive=True).first()
    if download_object:
        print("Successfully found progressive stream! No processing required")
        download_object.download(filename=video.title)
        print("Successfully grabbed video + audio")
        sg.Popup("Success", "Video successfully downloaded!")
    else:
        print("Couldn't find a progressive stream! Processing WILL be required.")
        audio_object = video.streams.filter(only_audio=True, mime_type="audio/mp4").first()
        video_object = video.streams.filter(resolution=resolution, file_extension="mp4").first()
        audio_object.download(filename=f'audio-{current_time}')
        video_object.download(filename=f'video-{current_time}')
        if not file_dir:
            ff.options(f'-i audio-{current_time}.mp4 -i video-{current_time}.mp4 -acodec copy -vcodec copy output-{current_time}.mkv')
            os.remove(f'audio-{current_time}.mp4')
            os.remove(f'video-{current_time}.mp4')
            sg.Popup("Success!", "Video saved to same directory as program")
        else:
            ff.options(f'-i audio-{current_time}.mp4 -i video-{current_time}.mp4 -acodec copy -vcodec copy {file_dir}/download-{current_time}.mkv')
            os.remove(f'audio-{current_time}.mp4')
            os.remove(f'video-{current_time}.mp4')
            sg.Popup("Success!", "Video saved to same selected directory")

def calculate_directory(user_output_directory):
    if not user_output_directory:
        return
    else:
        return user_output_directory
