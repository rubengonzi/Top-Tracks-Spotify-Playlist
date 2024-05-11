"""Module creating or updating a Spotify playlist with the users top songs."""

import os
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyOAuth

load_dotenv()

USERNAME = os.getenv("SPOTIPY_CLIENT_USERNAME")
PLAYLIST_NAME = os.getenv("PLAYLIST_NAME")
PLAYLIST_LENGTH = os.getenv("PLAYLIST_LENGTH")
TIME_RANGE = os.getenv("PLAYLIST_TIME_RANGE")

REPOSITORY_URL = "https://github.com/rubengonzi/Top-Tracks-Spotify-Playlist"

SCOPE = "playlist-read-private playlist-modify-public user-top-read"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=SCOPE))

def get_playlist():
    """Return playlist if present else create a new one."""
    for playlist in sp.user_playlists(USERNAME)['items']:
        if playlist['name'] == PLAYLIST_NAME:
            return playlist
    return sp.user_playlist_create(user=USERNAME, name=PLAYLIST_NAME, description=REPOSITORY_URL)

top_tracks = sp.current_user_top_tracks(time_range=TIME_RANGE, limit=PLAYLIST_LENGTH)
track_uris = [track['uri'] for track in top_tracks['items']]
sp.playlist_replace_items(get_playlist()['id'], track_uris)
