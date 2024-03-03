from tinytag import TinyTag
import lrclib_fetch
import pyperclip as pc
import tkinter as tk
from tkinter import filedialog
import subprocess
from pathlib import Path
import os

root = tk.Tk()
root.withdraw()


def ffmpeg_embed(OGFileName, lyrics):
    file_ext = Path(OGFileName).suffix
    new_file_name = f"{OGFileName}_syncedLyrics.{file_ext}"
    lyrics_command = f'lyrics={lyrics}'
    print(f"filename: {OGFileName}")
    ffmpeg_command = ["ffmpeg", "-i", OGFileName, "-metadata", lyrics_command, new_file_name]
    # Delete the Original File
    result = subprocess.run(ffmpeg_command)
    if result.returncode == 0:
        print("Lyrics Embedded Successfully")
        os.remove(OGFileName)
        os.rename(new_file_name, OGFileName)
    else:
        pc.copy(lyrics)
        print("Something went wrong with ffmpeg")
        print("synced lyrics have been copied to your clipboard!")


def get_lyrics(song):
    metadata = TinyTag.get(song)
    lyrics = lrclib_fetch.fetch_lyrics(metadata.title, metadata.artist, metadata.album, metadata.duration)
    if lyrics is None:
        print(f"No lyrics found for {metadata.title}")
        return None
    else:
        ffmpeg_embed(song, lyrics)



# Specify the file types to match music files
filetypes = (
    ('All music files', '*.mp3;*.m4a;*.flac'),
    ('MP3 files', '*.mp3'),
    ('M4A files', '*.m4a'),
    ('FLAC files', '*.flac'),
    ('All files', '*.*')
)

def select_files():
    file_path = filedialog.askopenfilenames(filetypes=filetypes)
    return file_path

files = select_files()

for file in files:
    get_lyrics(file)
