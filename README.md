# LRCLIB EMBED

A Simple python script to fetch **synced** lyrics from [lrclib](https://lrclib.net/) and embed them directy into your song file's metadata using ffmpeg

if you don't have ffmpeg on your device or it fails to embed for some reason, the script will just copy the lyrics in your clipboard. Some music players such as MusicBee allow you to just paste lyrics on a song.

**The script will only (try to) fetch synced lyrics**

As mentioned in [lrclib's docs](https://lrclib.net/docs) this script will break too if they make any changes to how their apis function.
> please be aware that there may be breaking changes in future updates. Since this document is still in its early stages, it may lack information or contain inaccuracies in certain sections. 

# Usage:
```
pip install -r src/requirements.txt
python3 main.py [song file(s)]
```
