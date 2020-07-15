# youtube-dl-helper
[![CodeFactor](https://www.codefactor.io/repository/github/wbnk/youtube-dl-helper/badge)](https://www.codefactor.io/repository/github/wbnk/youtube-dl-helper) [![Build Status](https://travis-ci.com/wbnk/youtube-dl-helper.svg?branch=master)](https://travis-ci.com/wbnk/youtube-dl-helper)


Grabs the youtube link that the user has inputted and saves it as either an mp3 or mkv. Very early release software so probably doesn't work well.




# features
* download video
* download mp3
* save to directory
* select video quality
* optionally download subtitles (if available)
* youtube-dl automatically uses ffmpeg to combine audio + video streams


# requirements

*develping:*

view requirements.txt - make sure you have ffmpeg in your systems PATH or in the same folder

*running:*
Every release is automatically built and stored on the releases page. You can download a fresh build from there.

Alternatively, you can download the source code and compile it using PyInstaller.

# screenshots
*screenshot from version 1.0, new ui looks very different.*

![Image of project](https://i.imgur.com/6ZizI7t.png)

*this is the ui used by the uitest.py file (out of date). doesn't look great at the moment but should scale well on different screen types. also much easier to add new features*

![Image of new UI](https://i.imgur.com/UTnx7g6.png)

# packaging using pyinstaller
i've successfully created an .exe which runs fine. used the arguments --name *whatever* --onefile --noconsole

every commit is automatically built by travis-ci as well to test that there aren't any errors

# compatibility

| OS | Supported          |
| ------- | ------------------ |
| Windows   | :white_check_mark: |
| Linux  | Probably                |
| MacOS   | Probably |

Can't see why they wouldn't work since pysimplegui is cross platform however I don't have access to a Mac to test. Will try on Linux at some point though. Running pyinstaller with same arguments as above should output a valid executable for these operating systems.
