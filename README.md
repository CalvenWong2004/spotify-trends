# spotify-trends
Hi, I am doing a mini project based on Spotify stream trends using my own playlist

# about
I am a Data Science student studying my final year so I decided to do some data science related work to add something to my CV, I am learning so I make mistakes, cheers.

I enjoy listening to musics so I decided to do a project based on something i like 

# object of this project
In this project, I will be doing EDA (Exploratory Data Analysis) on two datasets - a basic dataset imported from Kaggle, and my own Spotify playlist

# about the datasets
The basic dataset exported from Kaggle contains basic informations like Artist, Track Name, Daily Streams, and Total Streams
The dataset exported directly from my playlist contains much attributes like loudness, acousticness, danceability, and so on.

# plans
I will be doing standard data cleaning on the first dataset like splitting and renaming the columns, as well as filling out missing value.
As for my own dataset, i will be doing much detailed data cleaning and visualizations.

# note
I will be updating my work progress here 
<-- 20/6/2026 -->
----------------------------------------------------------------------------------------------------------------------------------------

# work progress (20/6/2026)
1. the data-filtering.ipynb is the file for cleaning and gaining insights into the basic dataset. 
2. I have normalised the data - splitting the first column (orginally Artists and Track Name) into two separate columns, Artists, and Track. 
3. Also, I have filled out the missing values to normalize the data. 
4. Then, I have converted the data type of Daily Streams and Streams from string to int64 for mathematical operations.
5. A summary of each artists and their streams have been shown, ranking from highest to lowest.
6. A bar plot has been visualized using the Seaborn library to show the graphical presentation of the artists and their streams.
7. A heatmap has also been implemented to show the relationships between the columns.
8. Feature engineered the dataset by adding a new column - Stream Percentage that shows the percentage of daily streams out of total streams.

# work progress 2 (20/6/2026 - 21/6/2026)
1. exported a new dataset from my own spotify playlist using Exportify
2. Cleaned and normalized the dataset
3. Feature engineered by grouping the sub genres and appending new genres
4. Created a frontend UI using streamlit that shows the statistics of the cleaned dataset. 

# to-do 
1. Create a new dashboard using other frameworks/languages (Spotipy/Standard HTML CSS and JS)




