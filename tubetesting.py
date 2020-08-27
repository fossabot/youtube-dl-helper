# pytube test kit

import pytube
from pytube import YouTube
from pyffmpeg import FFmpeg
ff = FFmpeg()
video = YouTube("https://www.youtube.com/watch?v=X")
user_dir = "C:/Users/X/Documents/X"
audio_object = video.streams.filter(only_audio=True, mime_type="audio/mp4").first()


video_object = video.streams.filter(resolution="1080p", adaptive=True, file_extension="mp4").first()
print("DLING audio")
audio_object.download(filename="audio")
print("DLING video")
video_object.download(filename="video")

print("Preparing conversion")
ff.options(f'-i audio.mp4 -i video.mp4 -acodec copy -vcodec copy {user_dir}/outputfile.mp4')
print("Done?")
