# Spotify Music Recommender
Welcome to the Spotify Music Recommender project! This project leverages machine learning techniques, particularly the calculation of cosine similarity, to recommend songs to users based on their preferences.
# Introduction
The Spotify Music Recommender is a machine learning-based project designed to recommend songs to users. By analyzing the musical attributes of songs and calculating their cosine similarity, the system suggests tracks that are similar to those the user already likes.
# Features
Song Recommendations: Suggests songs based on cosine similarity to the user's preferred tracks.
Spotify API Integration: Fetches detailed song data directly from Spotify's API.
User-Friendly Input: Simple interface for users to input their favorite songs.
Customizable Recommendations: Users can adjust the number of recommendations they receive.

# Data understanding and Visualisation 

!<img width="607" alt="Screenshot 2024-06-06 at 11 34 45" src="https://github.com/Jonathanferreira999/Spotify-song-recomender/assets/166486887/8689d048-0f99-4dab-9797-8bab3773fb34">

The plot above represent the correlations between feautures and popularity of a song. 

![newplot (11)](https://github.com/Jonathanferreira999/Spotify-song-recomender/assets/166486887/6eb256c9-b452-4a0f-b624-f7ec48752ebf)

The Plot above represents the distribution of the features during the last 100 years.

![newplot (12)](https://github.com/Jonathanferreira999/Spotify-song-recomender/assets/166486887/81638198-e006-4879-b2d1-648244141873)



Above we have the top10 genrs from the Spotifydataset2020 and the features that they have to find similarities.

![newplot (13)](https://github.com/Jonathanferreira999/Spotify-song-recomender/assets/166486887/fff64be2-7ed2-4367-8abe-7c18e761dc46)

K-mean Clustering of genrs and their distribution .

# Usage
 Run the recommender script  : "python src/app.py" 

Input your preferred songs    : The script will prompt you to enter the names or Spotify IDs of songs you like. You can input multiple songs to get more accurate recommendations.

Get recommendations: The system will output a list of songs with high cosine similarity to your input, providing details such as song name, artist, and similarity score.
# Data 
The project uses Spotify's API to fetch song data, including a wide range of musical features such as:

Danceability: How suitable a track is for dancing.

Energy: The intensity and activity level of a track.

Tempo: The speed or pace of a given track.

Valence: The musical positiveness conveyed by a track.

Acousticness, Instrumentalness, Liveness, Loudness, Speechiness: Other detailed attributes that describe the audio characteristics of a track.

These features are used to create a multidimensional space where each song is represented as a vector.

# Methodology 

Data Collection:

Fetch song data from Spotify's API.
Extract relevant musical features for each song.
Data Preprocessing:

Normalize the features to ensure consistent scaling.
Create song vectors based on the extracted features.
Cosine Similarity Calculation:

Calculate the cosine similarity between the input song vectors and all other song vectors in the dataset.

Cosine similarity measures the cosine of the angle between two vectors, providing a metric for similarity between songs.


Recommendation Generation:

Sort the songs based on their cosine similarity scores.
Select the top N songs as recommendations for the user.

# Model 

The core of the recommender system is based on the concept of cosine similarity. Cosine similarity measures the cosine of the angle between two vectors in a multidimensional space, which in this case are vectors representing songs. The similarity score ranges from -1 to 1, where 1 indicates identical vectors (songs), 0 indicates orthogonal vectors (no similarity), and -1 indicates completely opposite vectors.

# Results 

Results
The recommender system has shown promising results in suggesting songs that align well with user preferences. Some key outcomes include:

High Precision: The recommended songs often match the user's taste based on input songs.

Diverse Recommendations: Users receive a varied list of songs, including both popular tracks and hidden gems.

Scalability: The system performs efficiently even with a large dataset of songs.



