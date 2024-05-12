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
PLAYLIST_NAME=The name of the playlist where you want to add the tracks.
PLAYLIST_LENGTH=The desired length of the playlist (Minimum: 1. Maximum: 50).
PLAYLIST_TIME_RANGE=Time frame of your top tracks. Valid values: long_term (calculated from ~1 year of data), medium_term (approximately last 6 months), short_term (approximately last 4 weeks).
```

## Usage

### Manually

After executing this script all you need to do, is grant the application access to your Spotify account and your playlist should be good to go.

### Automated

To automatically update your playlist on a ficed schedule, you can use the Windows Task Scheduler. I suggest watching this [tutorial](https://www.youtube.com/watch?v=T9A8TelGsdo) to guide you through the setup.
