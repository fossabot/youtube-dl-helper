# youtube-dl-helper
[![CodeFactor](https://www.codefactor.io/repository/github/wbnk/youtube-dl-helper/badge)](https://www.codefactor.io/repository/github/wbnk/youtube-dl-helper) [![Build Status](https://travis-ci.com/wbnk/youtube-dl-helper.svg?branch=master)](https://travis-ci.com/wbnk/youtube-dl-helper)


Simple project that allows users to download YouTube videos to a specified folder. User can also select desired resolution, whether they want an MP3 or video and what format the video should be.

# Rewrite

The youtube_dl dependency will be changing to PyTube. The current release version is **1.1.3** (this version uses youtube_dl). The rewrite progress is being tracked [here](https://github.com/wbnk/youtube-dl-helper/projects/3)

# Features

* Download a video
* Download the audio only
* Select desired video format
* Select desired video resolution
* Download video subtitles (if available)
* Select where to download
* Automatically checks for updates and informs the user if there is an update available (user must manually update for security reasons)


# Screenshots

*current build 1.1 ui*

![Image of new UI](https://i.imgur.com/NiUybyY.png)


# Download
**You need to have ffmpeg downloaded. You can download it from [here](https://ffmpeg.org/download.html), windows builds are available [here](https://ffmpeg.zeranoe.com/builds/). Please use the latest version available else you might experience bugs (you probably will anyway). Place ffmpeg.exe either in your system's path or in the same folder as the executable.**

You can download the current stable release from [here](https://github.com/wbnk/youtube-dl-helper/releases). The current stable release version is **1.1.3**.

Alternatively, you can clone the repo and run the latest version of the code. The dev_version variable is set to true which will bypass the "update available" message box. Make sure to install the requirements from requirements.txt. 


