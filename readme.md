# youtube-dl-helper
[![Build Status](https://travis-ci.com/jwbn/youtube-dl-helper.svg?branch=master)](https://travis-ci.com/jwbn/youtube-dl-helper)

Grabs the youtube link that the user has inputted and saves it as either an mp3 or mp4. Uses youtube-dl and wxpython is used for the gui.

Better options do exist but I wanted to practice python and make something simple but useful for me. I don't need too many features just something to quickly download youtube videos with no hassle.


# features
* download video with audio as mkv
* download mp3 (converted by ffmpeg)
* status text
* basic error handling for incorrect link / no link

# planned features
* different output support

probably more stuff as i think of it



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

| OS | Supported          |
| ------- | ------------------ |
| Windows   | :white_check_mark: |
| Linux  | Probably                |
| MacOS   | ? |


