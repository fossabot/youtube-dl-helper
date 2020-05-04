# mp3_gui
[![Build Status](https://travis-ci.com/jwbn/mp3_gui.svg?branch=master)](https://travis-ci.com/jwbn/mp3_gui)

Grabs the youtube link that the user has inputted and saves it as either an mp3 or mp4. Uses youtube-dl and wxpython for the gui.

Better options do exist but I wanted to practice python and make something simple but useful for me.


# requirements
running source code yourself:
* wxpython
* youtube_dl
* also requires either the ffmpeg binary in the folder or in your system's PATH

view requirements.txt for specific details

running precompiled exe:

visit release page and download latest build


# screenshots
![Image of project](https://i.imgur.com/5GPHZnz.png)


# packaging using pyinstaller
i've successfully created an .exe which runs fine. used the arguments --name *whatever* --onefile --noconsole

every commit is automatically built by travis-ci as well to test that there aren't any errors

# compatibility

| Windows | Linux   | MacOS   |
|---------|---------|---------|
| Working | Unknown | Unknown |

