# mp3_gui
[![Build Status](https://travis-ci.com/jwbn/mp3_gui.svg?branch=master)](https://travis-ci.com/jwbn/mp3_gui)

didn't like running youtube_dl in the command prompt every time. wanted to practice making gui applications so made this.
i am aware of a youtube_dl gui which is much better but wanted to try and make something myself.

# requirements
* wxpython
* youtube_dl

view requirements.txt for specific details

# packaging using pyinstaller
i've successfully created an .exe which runs fine. used the arguments --name *whatever* --onefile --noconsole

will also build using travis-ci so i can see if pyinstaller works properly on other machines.

