import pandas as pd
import spotipy
from spotipy.oauth2 import SpotifyOAuth

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from datetime import datetime
from sklearn.metrics.pairwise import cosine_similarity

data = music_df

# Spotify Developer credentials
CLIENT_ID = '9e912b0d73424539b41d7c1c8a918645'
CLIENT_SECRET = '7b6ceab2e6ca41bc8903c5d69ac74810'
REDIRECT_URI = 'http://127.0.0.1:8888/callback'

# Define scope to access playlist and track information
SCOPE = 'playlist-read-private'

# Authenticate using SpotifyOAuth
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    redirect_uri=REDIRECT_URI,
    scope=SCOPE
))

def get_trending_playlist_data(playlist_id):
    # Get playlist tracks
    playlist_tracks = sp.playlist_tracks(playlist_id, fields='items(track(id, name, artists, album(id, name)))')

    music_data = []
    for track_info in playlist_tracks['items']:
        track = track_info['track']
        if not track:
            continue

        track_id = track['id']
        track_name = track['name']
        artists = ', '.join([artist['name'] for artist in track['artists']])
        album_name = track['album']['name']
        album_id = track['album']['id']

        # Get audio features
        try:
            audio_features = sp.audio_features([track_id])[0]
        except:
            audio_features = None

        # Get album release date
        try:
            album_info = sp.album(album_id)
            release_date = album_info['release_date']
        except:
            release_date = None

        # Get track popularity and other details
        try:
            full_track = sp.track(track_id)
            popularity = full_track['popularity']
            explicit = full_track['explicit']
            external_url = full_track['external_urls']['spotify']
        except:
            popularity = None
            explicit = None
            external_url = None

        # Build track data dictionary
        track_data = {
            'Track Name': track_name,
            'Artists': artists,
            'Album Name': album_name,
            'Album ID': album_id,
            'Track ID': track_id,
            'Popularity': popularity,
            'Release Date': release_date,
            'Duration (ms)': audio_features['duration_ms'] if audio_features else None,
            'Explicit': explicit,
            'External URL': external_url,
            'Danceability': audio_features['danceability'] if audio_features else None,
            'Energy': audio_features['energy'] if audio_features else None,
            'Key': audio_features['key'] if audio_features else None,
            'Loudness': audio_features['loudness'] if audio_features else None,
            'Mode': audio_features['mode'] if audio_features else None,
            'Speechiness': audio_features['speechiness'] if audio_features else None,
            'Acousticness': audio_features['acousticness'] if audio_features else None,
            'Instrumentalness': audio_features['instrumentalness'] if audio_features else None,
            'Liveness': audio_features['liveness'] if audio_features else None,
            'Valence': audio_features['valence'] if audio_features else None,
            'Tempo': audio_features['tempo'] if audio_features else None
        }

        music_data.append(track_data)

    # Convert to DataFrame
    df = pd.DataFrame(music_data)
    return df



playlist_id = '48hFHkpzOju8oOmSaGvR3V'

# Fetch and print DataFrame
music_df = get_trending_playlist_data(playlist_id)
print(music_df)
