# youtube-dl-helper
[![CodeFactor](https://www.codefactor.io/repository/github/wbnk/youtube-dl-helper/badge)](https://www.codefactor.io/repository/github/wbnk/youtube-dl-helper) [![Build Status](https://travis-ci.com/wbnk/youtube-dl-helper.svg?branch=master)](https://travis-ci.com/wbnk/youtube-dl-helper)


Simple project that uses pytube to download YouTube videos. Users can select desired resolution and what format they'd
like the file to be.


# modified pytube package

pytube is pretty broken at the moment. i've merged some of the fixes from pull requests
into https://github.com/wbnk/pytube. There's a very good chance that videos won't load if you aren't using the modified version.

install this modified version using ```pip install git+https://github.com/wbnk/pytube```


# Features

* Download a video
* Select desired video format
* Select desired video resolution
* Select where to download (directory)
* Automatically combines video + audio files from downloads into a single file
* Automatically checks for updates and informs the user if there is an update available (user must manually update for security reasons)


# Screenshots

2.0 UI (console opens with program to allow users to debug easily and to provide important information)

![2.0 UI](https://i.imgur.com/Szmmnua.png)


# Download

*I have found a way to include the ffmpeg.exe in the pyinstaller executable, however I'm not sure whether I can bundle the .exe with ffmpeg. You can create your own exe very easily.*

Select a release and download 

You'll then need to install the requirements. Pytube is required, but this project is using a *slightly* modified version. You can install it by using the command ```pip install git+https://github.com/wbnk/pytube```. I'd recommend using Pytube when it is properly fixed.

You can then run ```python main.py```. 

# Creating exe

Using pyinstaller, you can run ```pyinstaller --onefile --name ytdl-helper --add-binary ffmpeg.exe;pyffmpeg/static/bin/win32 main.py``` You'll need ffmpeg.exe in the directory 



