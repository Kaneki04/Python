import os

import spotipy
from spotipy.oauth2 import SpotifyOAuth


client_id = os.getenv("SPOTIPY_CLIENT_ID")
client_secret = os.getenv("SPOTIPY_CLIENT_SECRET")
redirect_uri = os.getenv(
    "SPOTIPY_REDIRECT_URI", "http://localhost:5000/callback"
)
scope = "user-library-read user-library-modify"

if not client_id or not client_secret:
    raise RuntimeError(
        "Set SPOTIPY_CLIENT_ID and SPOTIPY_CLIENT_SECRET as environment variables."
    )

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id=client_id,
        client_secret=client_secret,
        redirect_uri=redirect_uri,
        scope=scope,
    )
)


def unlike_all_saved_tracks():
    results = sp.current_user_saved_tracks(limit=1)
    total_tracks = results["total"]
    print(f"Total saved tracks: {total_tracks}")

    for offset in range(0, total_tracks, 50):
        results = sp.current_user_saved_tracks(limit=50, offset=offset)
        track_ids = [
            item["track"]["id"]
            for item in results["items"]
            if item["track"] is not None
        ]

        if track_ids:
            sp.current_user_saved_tracks_delete(track_ids)
            print(f"Unliked tracks: {track_ids}")


unlike_all_saved_tracks()
