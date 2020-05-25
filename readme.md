# youtube-dl-helper
[![Build Status](https://travis-ci.com/jwbn/youtube-dl-helper.svg?branch=master)](https://travis-ci.com/jwbn/youtube-dl-helper) [![CodeFactor](https://www.codefactor.io/repository/github/jwbn/youtube-dl-helper/badge)](https://www.codefactor.io/repository/github/jwbn/youtube-dl-helper)

Grabs the youtube link that the user has inputted and saves it as either an mp3 or mkv.



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

Either compile yourself using Pyinstaller or grab the latest release from the release section

# screenshots
![Image of project](https://i.imgur.com/6ZizI7t.png)


# packaging using pyinstaller
i've successfully created an .exe which runs fine. used the arguments --name *whatever* --onefile --noconsole

every commit is automatically built by travis-ci as well to test that there aren't any errors

# compatibility

| OS | Supported          |
| ------- | ------------------ |
| Windows   | :white_check_mark: |
| Linux  | Probably                |
| MacOS   | Probably |

Can't see why they wouldn't work since wxpython is cross platform however I don't have access to a Mac to test. Will try on Linux at some point though. Running pyinstaller with same arguments as above should output a valid executable for these operating systems.
