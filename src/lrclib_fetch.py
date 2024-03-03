import requests
import urllib.parse

def fetch_lyrics(track_name: str, artist_name: str, album_name: str, duration: int | float) -> str:

    # GET /api/get?artist_name=Borislav+Slavov&track_name=I+Want+to+Live&album_name=Baldur%27s+Gate+3+(Original+Game+Soundtrack)&duration=233

    track_name = urllib.parse.quote(track_name)
    artist_name = urllib.parse.quote(artist_name)
    album_name = urllib.parse.quote(album_name)

    url = f"https://lrclib.net/api/get?track_name={track_name}&artist_name={artist_name}&album_name={album_name}&duration={duration}"
    header = {
        'User-Agent': 'LRCLIB_EMBED v0.1.0 (https://github.com/ExclusiveRishi/LRCLIB_EMBED)'
    }
    response = requests.get(url, headers=header)

    print(f"request url: {url}")

    # Check for successful response and potential error handling
    if response.status_code == 200:
        data = response.json()
        # Extract lyrics from the response (assuming appropriate format)
        lyrics = data.get("syncedLyrics")
        return lyrics
    else:
        print(f"Error fetching lyrics: {response.status_code}")
        return None
