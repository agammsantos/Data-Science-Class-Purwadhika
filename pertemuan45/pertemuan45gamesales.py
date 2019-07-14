# kaggle datasets download -d rush4ratio/video-game-sales-with-ratings --unzip
# Recommendation system: single content and multiple content based filtering

import numpy as np
import pandas as pd

dfGame=pd.read_csv(
    'Video_Games_Sales_as_at_22_Dec_2016.csv' # copy relative path: ctrl+k ctrl+shift+c
)
print(dfGame.head(2))
print(dfGame.columns.values)
print(dfGame.isnull().sum())
print(dfGame[dfGame['Genre'].isnull()])

dfGame=dfGame.dropna(subset=['Genre']).reset_index()
print(dfGame.isnull().sum())
dfGame['GenPlat']=dfGame['Genre']+' '+dfGame['Platform']
print(dfGame['GenPlat'])

from sklearn.feature_extraction.text import CountVectorizer
model=CountVectorizer(
    # token_pattern=r'\b[\w-]+\b', # token pattern menentukan kata mana yg akan menjadi token (kunci kategori) dalam bhs regex, dalam kasus ini \w: karakter alphanumeric dan -:simbol strip
    # ngram_range=(1,2), # menentukan jumlah kata token yg masuk, dalam kasus ini akan menjadikan minimal 1 kata dan maksimal 2 kata yg terbaca menjadi satu kategori
    tokenizer=lambda i:i.split(' '), # menentukan pemisah pembaca token
    analyzer='word' # mengkategorikan token per kata, char: per huruf, default: word
    ) 
matrixGenre=model.fit_transform(dfGame['GenPlat'])
genre=model.get_feature_names()
jumlahGenre=len(genre)
eventGenre=matrixGenre.toarray()
# print(matrixGenre)
# print(genre)
# print(jumlahGenre)
# print(eventGenre[16653])
# print(dfGame.iloc[16653])

# cosinus similarity
from sklearn.metrics.pairwise import cosine_similarity
score=cosine_similarity(matrixGenre)
print(score.shape)

# # test model
sayaSuka='Suikoden'
print(dfGame[dfGame['Name']==sayaSuka])
indexSuka=dfGame[dfGame['Name']==sayaSuka].index.values[0]
# print(indexSuka)

# list all games + cos similarity score
allGames=list(enumerate(score[indexSuka]))
# print(allGames)

gameSama=sorted(
    allGames,
    key=lambda i: i[1],
    reverse=True
)

# show 5 first data, sorted by index
print(gameSama[:5])
for i in gameSama[:5]:
    print(dfGame.iloc[i[0]]['Name'],dfGame.iloc[i[0]]['Genre'])

# show 5 data randomly, cos sim score > 50%
gameSama50up=[]
for i in gameSama:
    if i[1]>0.5:
        gameSama50up.append(i)
print(gameSama50up)

# show a part of recommendation randomly every runtime
import random
rekomendasi=random.choices(gameSama50up,k=5)
print(rekomendasi)
for i in rekomendasi:
    print(dfGame.iloc[i[0]]['Name'],dfGame.iloc[i[0]]['Platform'],dfGame.iloc[i[0]]['Genre'])