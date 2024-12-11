import spotipy
from spotipy.oauth2 import SpotifyOAuth


client_id = "ef3e82c987064d3a95f06f9882fc5605"
client_secret = "af76c7c34b9647caac9192011407e7c4"
redirect_uri = "http://localhost:5000/callback"
scope = "user-library-read user-library-modify"

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(client_id, client_secret, redirect_uri, scope=scope)
)


def unlike_all_saved_tracks():
    # Get the total number of saved tracks
    results = sp.current_user_saved_tracks(limit=1)
    total_tracks = results["total"]
    print(f"Total saved tracks: {total_tracks}")

    # Remove tracks in batches (max 50 at a time)
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


# Execute the function
unlike_all_saved_tracks()
