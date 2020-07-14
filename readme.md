# youtube-dl-helper
[![CodeFactor](https://www.codefactor.io/repository/github/wbnk/youtube-dl-helper/badge)](https://www.codefactor.io/repository/github/wbnk/youtube-dl-helper)


Grabs the youtube link that the user has inputted and saves it as either an mp3 or mkv. Very early release software so probably doesn't work well




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
*screenshot from version 1.0, new ui looks very different.*
![Image of project](https://i.imgur.com/6ZizI7t.png)

*this is the ui used by the uitest.py file. doesn't look great at the moment but should scale well on different screen types. also much easier to add new features*
![Image of new UI](https://i.imgur.com/lzdkQuY.png)

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
