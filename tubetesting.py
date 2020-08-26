from pytube import YouTube
print("PyTube loaded")

video = YouTube('https://youtube.com/watch?v=x')


print(f'Title of video is {video.title}')

download_object = video.streams.filter(resolution="1080p", progressive=True).first()

if not download_object:
    print("Cannot find audio+video stream")
