from pytube import YouTube
import PySimpleGUI as sg
import requests


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
    video = YouTube(vid_url)
    if resolution != "1080p":  # Code for potential progressive streams
        download_object = video.streams.filter(resolution=resolution,
                                               file_extension="mp4", progressive="True").first()
        if download_object:
            print("Successfully found progressive stream! No processing required")
            download_object.download()
            print("Successfully grabbed video + audio")
            sg.Popup("Success", "Video successfully downloaded!")
        else:
            print("Couldn't find a progressive stream! Processing WILL be required.")
            video_object = video.streams.filter(resolution=resolution,
                                                   file_extension="mp4", adaptive="True").first()
            video_object.download()
            print("Successfully grabbed video")




def calculate_directory(user_output_directory):
    if not user_output_directory:
        user_output_directory = "%(title)s.%(ext)s"
    else:
        user_output_directory = user_output_directory + "/%(title)s.%(ext)s"
    return user_output_directory
