import spotipy
from spotipy.oauth2 import SpotifyOAuth
import yt_dlp
import os


SPOTIPY_CLIENT_ID = "ef3e82c987064d3a95f06f9882fc5605"
SPOTIPY_CLIENT_SECRET = "af76c7c34b9647caac9192011407e7c4"
SPOTIPY_REDIRECT_URI = "http://localhost:5000/callback"
SCOPE = "user-library-read"
error = []

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id=SPOTIPY_CLIENT_ID,
        client_secret=SPOTIPY_CLIENT_SECRET,
        redirect_uri=SPOTIPY_REDIRECT_URI,
        scope=SCOPE,
    )
)


def get_liked_songs():
    liked_songs = []
    results = sp.current_user_saved_tracks(limit=50)  # Adjust limit as needed
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


output_path = "C:\\Users\\vicke\\Downloads\\SpotiMusic\\"


def download_song(search_query):
    os.makedirs(output_path, exist_ok=True)

    ydl_opts = {
        "format": "bestaudio/best",
        "extractaudio": True,  # Download only audio
        "audioformat": "mp3",  # Save as mp3
        "outtmpl": os.path.join(
            output_path, f"{search_query.replace(' Audio','')}.%(ext)s"
        ),
        "quiet": False,  # Set to True to suppress output
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([f"ytsearch:{search_query}"])


liked_songs = get_liked_songs()

for song in liked_songs:
    print("**************************************************")
    print(song)
    download_song(song)
    print("**************************************************\n")
