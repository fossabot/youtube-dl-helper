# pytube test kit

import pytube
from pytube import YouTube
print("PyTube loaded")


# Progressive (720p and below audio + vid), adaptive (1080p+noaudio)
video_url = input("Enter video url: ")
desired_resolution = input("Enter res: ")
try:
    video = YouTube(video_url)
    print(f"Video found. Title: {video.title}")

except pytube.exceptions.RegexMatchError as invalid_url_error:
    print("You entered an invalid URL!")

#
#download_object = video.streams.filter(resolution="720p", progressive=True).first()
#
#if not download_object:
#    print("Cannot find audio+video stream")
#else:
#    print("Found audio+video stream")
