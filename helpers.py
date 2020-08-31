"""
This file handles the actual downloading and a few other things. Functions are explained below.

Functions:
check_version() - reads version number from git repo and checks with local version number.
download_video() - creates 'YouTube' object and downloads it. Searches for progressive (audio+video) streams first.
calculate_available_resolutions() - creates 'YouTube' object and searches for downloads for every resolution.
on_progress() - was used as a callback when downloading video. currently not functional and may be removed

"""

from pytube import YouTube, Playlist
import PySimpleGUI as sg
import requests
import time
from pyffmpeg import FFmpeg
import os


def check_version(local_version, dev_version):
    try:
        response = requests.get("https://raw.githubusercontent.com/wbnk/youtube-dl-helper/master/version_info.json")
        data = response.json()
        server_version = data['stable-version']
        print(server_version)
        if not dev_version:
            if server_version != local_version:
                sg.Popup("Out of date!", """A newer version is available at Github! Update the software
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
    if not file_dir:
        file_dir = os.getcwd()
    download_object = video.streams.filter(resolution=resolution,
                                           file_extension="mp4", progressive=True).first()

    if download_object:
        print("[INFO] Progressive stream found. Direct download available")
        download_object.download(filename=video.title, output_path=file_dir)
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
        try:
            ff.options(
                f'-i audio-{current_time}.mp4 -i video-{current_time}.mp4 -acodec copy -vcodec copy {file_dir}/{underscore_name}.{prefformat}')
        except:  # Horrible hack to fix videos with filenames that break pyffmpeg
            print("[WARN] Error whilst converting. Defaulting back to generic filename")
            ff.options(
                f'-i audio-{current_time}.mp4 -i video-{current_time}.mp4 -acodec copy -vcodec copy {file_dir}/download-{current_time}.{prefformat}')
        print("[INFO] Cleaning up...")
        os.remove(f'audio-{current_time}.mp4')
        os.remove(f'video-{current_time}.mp4')
        sg.Popup("Success!", "Video downloaded!")
        return


def download_playlist_video(url, resolution, file_dir, prefformat):
    ff = FFmpeg()
    if not file_dir:
        file_dir = os.getcwd()
    current_time = int(time.time())
    print(f'[INFO] Attempting to download {url} at max resolution')
    video = YouTube(url)
    underscore_name = video.title.replace(" ", "_")
    max_res = calculate_available_resolutions(video)
    if max_res[-1] == "1080p":
        video_object = video.streams.filter(resolution="1080p", file_extension="mp4").first()
        audio_object = video.streams.filter(only_audio=True, mime_type="audio/mp4").first()
        try:
            video_object.download(filename=f'video-{current_time}')
            audio_object.download(filename=f'audio-{current_time}')
        except:
            sg.Popup("Error", f'Error downloading {video.title}. Sorry!')
            return

        try:
            ff.options(
                f'-i audio-{current_time}.mp4 -i video-{current_time}.mp4 -acodec copy -vcodec copy {file_dir}/{underscore_name}.{prefformat}')
            os.remove(f'audio-{current_time}.mp4')
            os.remove(f'video-{current_time}.mp4')
            print("[INFO] Downloaded and converted 1080p video!")
            return
        except:  # Horrible hack
            print("[WARN] Error whilst converting. Defaulting back to generic filename")
            ff.options(
                f'-i audio-{current_time}.mp4 -i video-{current_time}.mp4 -acodec copy -vcodec copy {file_dir}/download-{current_time}.{prefformat}')
            os.remove(f'audio-{current_time}.mp4')
            os.remove(f'video-{current_time}.mp4')
            print("[INFO] Downloaded and converted 1080p video (generic name)")
            return
    else:
        video_object = video.streams.filter(resolution=max_res[-1], progressive=True, file_extension="mp4").first()
        print("[INFO] Attempting to download video object")
        video_object.download(output_path=file_dir)
        print("[INFO] Video object downloaded")
        return


def get_playlist_links(url):
    vid_links = []
    playlist = Playlist(url)
    for prefix in playlist.video_urls:
        vid_links.append(prefix)
    return vid_links


def download_playlist(resolution, file_dir, subtitles, prefformat, output_type, vid_url):
    video_links = get_playlist_links(vid_url)
    for video in video_links:
        print(f'[INFO] Downloading {video}')
        download_playlist_video(video, resolution, file_dir, prefformat)
    sg.Popup("Done!", "Playlist downloaded")
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
