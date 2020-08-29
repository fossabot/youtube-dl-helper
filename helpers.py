from pytube import YouTube
import PySimpleGUI as sg
import requests

import time
from pyffmpeg import FFmpeg
import os

def check_version(local_version, dev_version):
    try:
        response = requests.get("https://raw.githubusercontent.com/wbnk/youtube-dl-helper/master/version_info.json")
        data = response.text
        server_version = data[0] + data[1] + data[2]
        if not dev_version:
            if server_version != local_version:
                sg.Popup("Out of date", """A newer version is available at Github! Update the software
                         to receive the latest feature updates.""")
                return False
            return True
        print("[INFO] Successfully checked for updates")
        return "dev-ver"
    except requests.exceptions.ConnectTimeout as connection_error:
        sg.Popup("Error", "Unable to check current program version. Check your connection.")


def download_video(resolution, file_dir, subtitles, prefformat, output_type, vid_url):
    ff = FFmpeg()
    current_time = int(time.time())
    video = YouTube(vid_url)
    underscore_name = video.title.replace(" ", "_")
    download_object = video.streams.filter(resolution=resolution,
                                           file_extension="mp4", progressive=True).first()
    # video.register_on_progress_callback(on_progress)  # This appears to completely destroy performance.
    if download_object:
        print("[INFO] Progressive stream found. Direct download available")
        download_object.download(filename=video.title)
        sg.Popup("Success", "Video successfully downloaded!")
    else:
        print("[INFO] Progressive stream not found. Searching for adaptive streams.")
        audio_object = video.streams.filter(only_audio=True, mime_type="audio/mp4").first()
        video_object = video.streams.filter(resolution=resolution, file_extension="mp4").first()
        try:
            print("[INFO] Audio Downloading")
            audio_object.download(filename=f'audio-{current_time}')
            print("[INFO] Video Downloading")
            video_object.download(filename=f'video-{current_time}')
        except AttributeError as download_error:  # It technically shouldn't be possible to get here (using res check)
            print("[ERROR] Couldn't find stream at desired resolution.")
            sg.Popup("Download fail", "Couldn't find a stream at your desired resolution. Choose a lower quality")
            return
        if not file_dir:
            ff.options(
                f'-i audio-{current_time}.mp4 -i video-{current_time}.mp4 -acodec copy -vcodec copy {underscore_name}.{prefformat}')
        else:
            ff.options(
                f'-i audio-{current_time}.mp4 -i video-{current_time}.mp4 -acodec copy -vcodec copy {file_dir}/{underscore_name}.{prefformat}')

        print("[INFO] Cleaning up...")
        os.remove(f'audio-{current_time}.mp4')
        os.remove(f'video-{current_time}.mp4')
        sg.Popup("Success!", "Video downloaded!")
        return


def calculate_directory(user_output_directory):
    if not user_output_directory:
        return
    else:
        return user_output_directory


def calculate_available_resolutions(video):
    print("[INFO] Checking what resolutions are available")
    standard_resolutions = ["144p", "240p", "360p", "480p", "720p", "1080p"]
    available_resolutions = []
    for resolution in standard_resolutions:
        try:
            video_object = video.streams.filter(resolution=resolution, file_extension="mp4", adaptive=True).first()
            audio_object = video.streams.filter(only_audio=True, mime_type="audio/mp4").first()
            if video_object and audio_object:
                available_resolutions.append(resolution)
        except:
            print(f'[INFO] Video not available at: {resolution}')
    print(available_resolutions)
    return available_resolutions




    # def on_progress(stream, chunk, bytes_remaining):  # Used a profiler and download speed is destroyed!
    #    total_size = stream.filesize
    #    bytes_downloaded = total_size - bytes_remaining
    #    percentage_of_completion = bytes_downloaded / total_size * 100
    #    progress = sg.one_line_progress_meter(f'Downloading {stream.title}', int(percentage_of_completion), 100,
    #                                          '% downloaded', orientation="h", size=(50, 50))
    #    if not progress:
    #        print("[INFO] Download finished or you clicked the cancel button")
    #