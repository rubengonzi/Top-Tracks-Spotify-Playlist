# Top Tracks Spotify Playlist

This script automatically creates or updates a playlist based on your top Spotify songs.

## Installation

Visit [python.org](https://www.python.org/downloads/) to see the latest python version.

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the following dependencies:

```bash
pip install python-dotenv
pip install spotipy
```

After creating a file named `.env` in this repository's directory, you must define the following variables:

```
SPOTIFY_USERNAME=Your Spotify username.
PLAYLIST_NAME=The name of the playlist where you want to add tracks.
PLAYLIST_LENGTH=The desired length of the playlist.
PLAYLIST_TIME_RANGE=The time range for selecting tracks (short_term, medium_term, long_term).
```

## Usage

### Manually

Upon executing the [playlist.py](https://github.com/rubengonzi/Top-Tracks-Spotify-Playlist/blob/main/playlist.py) script, you will be asked to grant persmission to your Spotify account. After you have done so, a new tab will open in your browser. Copy the URL to your clipboard and paste it into the following prompt:
![image](https://github.com/rubengonzi/Top-Tracks-Spotify-Playlist/assets/125918471/a488b7aa-bd53-404c-9cc7-b90080138e9a)

### Automated

To automatically execute this script using the Task Scheduler by Windows, I suggest following this [tutorial](https://www.youtube.com/watch?v=T9A8TelGsdo).
