# Test build for cx_freeze

import os
from cx_Freeze import setup, Executable

setup(
    name = "youtube-dl-helper",
    version = "1.1",
    description = "Grabs the youtube link that the user has inputted and saves it as either an mp3 or mkv.",
    author = "WBNK",
    options = {
        "build_exe": {
            "packages": ["youtube-dl", "tkinter", "PySimpleGUI"],
            "include_files": ["icon.ico", "icon.png"],  # These need to be added
            'include_msvcr': False  # This needs to be verified with a test build
        }
    },
    
    executables = [target]
)
