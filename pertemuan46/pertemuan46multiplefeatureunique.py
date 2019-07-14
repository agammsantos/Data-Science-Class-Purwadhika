# kaggle datasets download -d rush4ratio/video-game-sales-with-ratings --unzip
# Recommendation system: multiple content based filtering

import numpy as np
import pandas as pd

dfGame=pd.read_csv(
    'Video_Games_Sales_as_at_22_Dec_2016.csv' # copy relative path: ctrl+k ctrl+shift+c
)
print(dfGame.head(2))
print(dfGame.columns.values)
print(dfGame.isnull().sum())
print(dfGame[dfGame['Genre'].isnull()])

dfGame=dfGame.dropna(subset=['Genre','Platform']).reset_index()
print(dfGame.isnull().sum())
dfGame=dfGame[['Name','Platform','Genre']]
print(dfGame.head(10))

# add a new col: 'Platform' + 'Genre'
# def mergeCol(i):
#     return i['Platform']+' '+i['Genre']
# dfGame['Features']=mergeCol(dfGame)
# print(dfGame.head())

# alternative
def mergeCol(i):
    return str(i['Platform'])+' '+str(i['Genre'])
dfGame['Features']=dfGame.apply(mergeCol,axis='columns')
print(dfGame.head())

print(len(dfGame['Platform'].unique()))
print(len(dfGame['Genre'].unique()))
print(len(dfGame['Features'].unique()))

# count vectorizer
from sklearn.feature_extraction.text import CountVectorizer
model=CountVectorizer(tokenizer=lambda x:x.split(' '))
matrixFeature=model.fit_transform(dfGame['Features'])

features=model.get_feature_names()
jmlFeatures=len(features)
print(features)
print(jmlFeatures)
print(matrixFeature[0])
print(matrixFeature.toarray()[0])

# cosine similarity
from sklearn.metrics.pairwise import cosine_similarity
score=cosine_similarity(matrixFeature)
print(score)
print(list(enumerate(score[0])))

# testing
sukaGame='Tetris'
indexSuka=dfGame[dfGame['Name']==sukaGame].index[0] # index[0] karena game tetris ada 2, mengambil index yang paling awal
print(indexSuka)

daftarScore=list(enumerate(score[indexSuka]))
print(daftarScore)

sortDaftarScore=sorted(
    daftarScore,
    key=lambda j:j[1],
    reverse=True
)
# print(sortDaftarScore[:5])
# print(sortDaftarScore[:5][0])
# print(dfGame[dfGame['Name']==sukaGame].index.values[0])

# recommending top 5 highest cosine similarity score games
similarGames=[]
for i in sortDaftarScore:
    if i[1]>.8:
        similarGames.append(i)

for i in range(0,5):
    if similarGames[i][0]!=dfGame[dfGame['Name']==sukaGame].index.values[0]:
        print(dfGame['Name'].iloc[similarGames[i][0]])
    else:
        i+=5
        print(dfGame['Name'].iloc[similarGames[i][0]])

# recommending unique similar games
import random

choices=[]
for i in range(0,5):
    while True: # loop forever
        rekomendasi=random.choices(similarGames)
        data=dfGame.iloc[rekomendasi[0][0]].values
        if data[0] not in choices and data[0]!=sukaGame:
            choices.append(data[0])
            print(data[0],data[1],data[2])
            break
        