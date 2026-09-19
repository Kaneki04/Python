import os

import spotipy
from spotipy.oauth2 import SpotifyOAuth
import yt_dlp


SPOTIPY_CLIENT_ID = os.getenv("SPOTIPY_CLIENT_ID")
SPOTIPY_CLIENT_SECRET = os.getenv("SPOTIPY_CLIENT_SECRET")
SPOTIPY_REDIRECT_URI = os.getenv(
    "SPOTIPY_REDIRECT_URI", "http://localhost:5000/callback"
)
SCOPE = "user-library-read"

if not SPOTIPY_CLIENT_ID or not SPOTIPY_CLIENT_SECRET:
    raise RuntimeError(
        "Set SPOTIPY_CLIENT_ID and SPOTIPY_CLIENT_SECRET as environment variables."
    )

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id=SPOTIPY_CLIENT_ID,
        client_secret=SPOTIPY_CLIENT_SECRET,
        redirect_uri=SPOTIPY_REDIRECT_URI,
        scope=SCOPE,
    )
)

output_path = os.getenv(
    "SPOTIFY_DOWNLOAD_DIR",
    os.path.join(os.path.expanduser("~"), "Downloads", "SpotiMusic"),
)


def get_liked_songs():
    liked_songs = []
    results = sp.current_user_saved_tracks(limit=50)

    while results:
        for item in results["items"]:
            track = item["track"]
            liked_songs.append(
                f"{track['name']} - {', '.join(artist['name'] for artist in track['artists'])} Audio"
            )

        if results["next"]:
            results = sp.next(results)
        else:
            break

    return liked_songs


def download_song(search_query):
    os.makedirs(output_path, exist_ok=True)

    ydl_opts = {
        "format": "bestaudio/best",
        "extractaudio": True,
        "audioformat": "mp3",
        "outtmpl": os.path.join(
            output_path, f"{search_query.replace(' Audio', '')}.%(ext)s"
        ),
        "quiet": False,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([f"ytsearch:{search_query}"])


for song in get_liked_songs():
    print("**************************************************")
    print(song)
    download_song(song)
    print("**************************************************\n")
