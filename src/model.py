import spotipy # Spotify's Python library
from spotipy.oauth2 import SpotifyClientCredentials # Spotify's OAuth credentials
from collections import defaultdict # Python's defaultdict class
import os  # OS operations
import numpy as np  # Numeric operations
import pandas as pd  # Data manipulation

import seaborn as sns  # Statistical visualization
import plotly.express as px  # Interactive plots
import matplotlib.pyplot as plt  # Plotting library
# Display plots inline
#%matplotlib inline  

from sklearn.cluster import KMeans  # KMeans clustering
from sklearn.preprocessing import StandardScaler  # Data standardization
from sklearn.pipeline import Pipeline  # Sequential transformations
from sklearn.manifold import TSNE  # High-dim data visualization
from sklearn.decomposition import PCA  # Principal Component Analysis
from sklearn.metrics import euclidean_distances  # Euclidean distances
from scipy.spatial.distance import cdist  # Pairwise distances

import warnings  # Warning control
warnings.filterwarnings("ignore")  # Ignore warnings
#IRONHCK
CLIENT_ID = "4109b2d9f5014671863bb2df1d1fbdd3"
CLIENT_SECRET = "5cb719fae80c4191a9c0b288f51bfe50"

df_data = pd.read_csv("/Users/jonathansantos/Desktop/IronHack/Projectofinalop/data/raw/data.csv")
f_genre = pd.read_csv("/Users/jonathansantos/Desktop/IronHack/Projectofinalop/data/raw/data_by_genres.csv")
df_year = pd.read_csv("/Users/jonathansantos/Desktop/IronHack/Projectofinalop/data/raw/data_by_year.csv")


song_cluster_pipeline = Pipeline([('scaler', StandardScaler()), 
                                  ('kmeans', KMeans(n_clusters=20, 
                                   verbose=False))
                                 ], verbose=False)

X = df_data.select_dtypes(np.number)
number_cols = list(X.columns)
song_cluster_pipeline.fit(X)
song_cluster_labels = song_cluster_pipeline.predict(X)
df_data['cluster_label'] = song_cluster_labels


sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET))



def find_song(name, year):
    song_data = defaultdict()
    results = sp.search(q= 'track: {} year: {}'.format(name,year), limit=1)
    if results['tracks']['items'] == []:
        return None

    results = results['tracks']['items'][0]
    track_id = results['id']
    audio_features = sp.audio_features(track_id)[0]

    song_data['name'] = name
    song_data['year'] = year
    song_data['explicit'] = int(results['explicit'])
    song_data['duration_ms'] = results['duration_ms']
    song_data['popularity'] = results['popularity']

    for key, value in audio_features.items():
        song_data[key] = value

    return pd.Series(song_data)




from collections import defaultdict
from sklearn.metrics import euclidean_distances
from scipy.spatial.distance import cdist
import difflib

number_cols = ['valence', 'year', 'acousticness', 'danceability', 'duration_ms', 'energy', 'explicit',
 'instrumentalness', 'key', 'liveness', 'loudness', 'mode', 'popularity', 'speechiness', 'tempo']


def get_song_data(song, spotify_data):
    
    try:
        song_data = spotify_data[(spotify_data['name'] == song['name']) 
                                & (spotify_data['year'] == song['year'])].iloc[0]
        return song_data
    
    except IndexError:
        return find_song(song['name'], song['year'])
        

def get_mean_vector(song_list, spotify_data):
    
    song_vectors = []
    
    for song in song_list:
        song_data = get_song_data(song, spotify_data)
        if song_data is None:
            print('Warning: {} does not exist in Spotify or in database'.format(song['name']))
            continue
        song_vector = song_data[number_cols].values
        song_vectors.append(song_vector)  
    
    song_matrix = np.array(list(song_vectors))
    return np.mean(song_matrix, axis=0)


def flatten_dict_list(dict_list):
    
    flattened_dict = defaultdict()
    for key in dict_list[0].keys():
        flattened_dict[key] = []
    
    for dictionary in dict_list:
        for key, value in dictionary.items():
            flattened_dict[key].append(value)
            
    return flattened_dict


def recommend_songs( song_list, spotify_data, n_songs=10):
    
    metadata_cols = ['name', 'year', 'artists']
    song_dict = flatten_dict_list(song_list)
    
    song_center = get_mean_vector(song_list, spotify_data)
    scaler = song_cluster_pipeline.steps[0][1]
    scaled_data = scaler.transform(spotify_data[number_cols])
    scaled_song_center = scaler.transform(song_center.reshape(1, -1))
    distances = cdist(scaled_song_center, scaled_data, 'cosine')
    index = list(np.argsort(distances)[:, :n_songs][0])
    
    rec_songs = spotify_data.iloc[index]
    rec_songs = rec_songs[~rec_songs['name'].isin(song_dict['name'])]
    
    a = rec_songs[metadata_cols].to_dict(orient='records')
    
    print(a)    
    return a