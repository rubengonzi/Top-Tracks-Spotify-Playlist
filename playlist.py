import os
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyOAuth

load_dotenv()

USERNAME = os.getenv("SPOTIPY_CLIENT_USERNAME")
PLAYLIST_NAME = os.getenv("PLAYLIST_NAME")
PLAYLIST_LENGTH = os.getenv("PLAYLIST_LENGTH")
TIME_RANGE = os.getenv("TIME_RANGE")

scope = "playlist-read-private playlist-modify-private user-top-read"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

def get_playlist():
    for playlist in sp.user_playlists(USERNAME)['items']:
        if playlist['name'] == PLAYLIST_NAME:
            return playlist
    return sp.user_playlist_create(user=USERNAME, name=PLAYLIST_NAME, public=False)

top_tracks = sp.current_user_top_tracks(time_range=TIME_RANGE, limit=PLAYLIST_LENGTH)
track_uris = [track['uri'] for track in top_tracks['items']]
sp.playlist_replace_items(get_playlist()['id'], track_uris)
