# youtube-dl-helper
[![CodeFactor](https://www.codefactor.io/repository/github/wbnk/youtube-dl-helper/badge)](https://www.codefactor.io/repository/github/wbnk/youtube-dl-helper) [![Build Status](https://travis-ci.com/wbnk/youtube-dl-helper.svg?branch=master)](https://travis-ci.com/wbnk/youtube-dl-helper)


Simple project that uses pytube to download YouTube videos. Users can select desired resolution and what format they'd
like the file to be.


# modified pytube package

pytube is pretty broken at the moment. i've merged some of the fixes from pull requests
into https://github.com/wbnk/pytube

install this modified version using ```pip install git+https://github.com/wbnk/pytube```


# Features

* Download a video
* Select desired video format
* Select desired video resolution
* Select where to download
* Automatically checks for updates and informs the user if there is an update available (user must manually update for security reasons)


# Screenshots

No screenshot available currently.


# Download

**pyffmpeg includes a binary. ffmpeg will automatically work so you don't need to download it.**

*Builds currently aren't available. Work needs to be done to allow Pyinstaller to correctly find the ffmpeg.exe*

If you'd like to use this program, you'll need to download the git repo. You'll then need to run **pip install requirements.txt**

Finally, you can run **python main.py**


