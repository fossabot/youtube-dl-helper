# pytube test kit

import pytube
from pytube import YouTube
from pyffmpeg import FFmpeg
import os
import time


current_time = int(time.time())
ff = FFmpeg()
video = YouTube("x")
user_dir = "x"
audio_object = video.streams.filter(only_audio=True, mime_type="audio/mp4").first()


video_object = video.streams.filter(resolution="1080p", adaptive=True, file_extension="mp4").first()
print("DLING audio")
audio_object.download(filename=f'audio-{current_time}')
print("DLING video")
video_object.download(filename=f'video-{current_time}')

print("Preparing conversion")
ff.options(f'-i audio-{current_time}.mp4 -i video-{current_time}.mp4 -acodec copy -vcodec copy {user_dir}/testfile-{current_time}.mkv')
print("Finished conversion")
time.sleep(1)
os.remove(f'audio-{current_time}.mp4')
os.remove(f'video-{current_time}.mp4')

