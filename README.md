# Top Tracks Spotify Playlist

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the following dependencies:

```bash
pip install python-dotenv
pip install spotipy
```

The environment variables below must be defined in the .env file of this repository.

```
SPOTIPY_CLIENT_ID=The Spotify Client ID provided by Spotify Developer Dashboard.
SPOTIPY_CLIENT_SECRET=The Spotify Client Secret provided by Spotify Developer Dashboard.
SPOTIPY_REDIRECT_URI=The Redirect URI registered in your Spotify Developer Dashboard (e.g. https://example.com/callback).
SPOTIPY_CLIENT_USERNAME=Your Spotify username.
PLAYLIST_NAME=The name of the playlist where you want to add tracks.
PLAYLIST_LENGTH=The desired length of the playlist.
PLAYLIST_TIME_RANGE=The time range for selecting tracks (e.g., short_term, medium_term, long_term).
```

To get your Client ID, Client Secret and set up your Redirect URI please follow the [tutorial](https://developer.spotify.com/documentation/web-api/tutorials/getting-started#create-an-app) by Spotify to create your own app.

## Usage

Upon executing the [playlist.py](https://github.com/rubengonzi/Top-Tracks-Spotify-Playlist/blob/main/playlist.py) script, you will be asked to grant persmission to your Spotify account. After you have done so, you will be redirected to the URI you have specified in your Spotify Developer Dashboard. Copy the URI to your clipboard and paste it into the following prompt:
![image](https://github.com/rubengonzi/Top-Tracks-Spotify-Playlist/assets/125918471/a488b7aa-bd53-404c-9cc7-b90080138e9a)
