# youtube-dl-helper
[![CodeFactor](https://www.codefactor.io/repository/github/wbnk/youtube-dl-helper/badge)](https://www.codefactor.io/repository/github/wbnk/youtube-dl-helper) [![Build Status](https://travis-ci.com/wbnk/youtube-dl-helper.svg?branch=master)](https://travis-ci.com/wbnk/youtube-dl-helper)

**Current version**: 2.1.1

Simple project that uses pytube to download YouTube videos. Users can select desired resolution and what format they'd
like the file to be.


# modified pytube package

pytube is pretty broken at the moment. i've merged some of the fixes from pull requests
into https://github.com/wbnk/pytube. There's a very good chance that videos won't load if you aren't using the modified version.

install this modified version using ```pip install git+https://github.com/wbnk/pytube```


# Features

* Download a video
* Select desired video output format (if downloading at 1080p, otherwise it downloads as an mp4)
* Select desired video resolution
* Select where to download (directory)
* Automatically combines video + audio files from downloads into a single file. Also cleans up the source files used for conversion
* Automatically checks for updates and informs the user if there is an update available (user must manually update for security reasons)
* Playlist downloading support (experimental feature, downloads at max res for each video)

**Upcoming features**

* Subtitle support
* Video FPS support (60 etc.)
* Download audio only

# Screenshots

2.0 UI (console opens with program to allow users to debug easily and to provide important information)

![2.0 UI](https://i.imgur.com/Szmmnua.png)


# Download

*You can download the latest build from the [releases](https://github.com/wbnk/youtube-dl-helper/releases) page. Alternatively, you can create your own exe by following the instructions below...*

# Build instructions

* Download the latest source
* You'll then need to install the requirements by running ```pip install -r requirements.txt``` (This will install a fixed pytube version)
* Run ```python main.py``` to verify that everything works.
* Create the exe using ```pyinstaller --onefile --name ytdl-helper```. Make sure not to use ```--noconsole```, the conversion output is written to the console and will fail if it's disabled. The console also provides information for debugging.



