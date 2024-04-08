# flac-various-artists-overwrite

A small Python script that parses a folder of FLAC files and reshuffles their artist and song title tags. Something quick n dirty for personal use, so no fancy CLI with arguments or anything.

Intended to be used with compilation albums where each song's artist tag is "Various Artists" or something and each song's title tag is formatted like "{actual artist} - {actual song title}". This script parses these title tags and overwrites each song's metadata with the correct artist and song title.

# Usage

Download the latest version of Python, clone this repo, start a virtual environment in the cloned repo folder, activate the virtual environment, install packages from `requirements.txt`, modify the variable `MUSIC_FOLDER` in `main.py` to be the path containing your FLAC files, and run `main.py`.
