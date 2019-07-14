# 1. Popularity Based
import numpy as np
import pandas as pd

produk=[
    {'nama':'Tamiya','rating':5},
    {'nama':'Drone','rating':4},
    {'nama':'RC Car','rating':5},
    {'nama':'Action Figure','rating':3},
    {'nama':'Bantal','rating':2},
    {'nama':'Guling','rating':5},
]

dfProduk=pd.DataFrame(produk)
print(dfProduk)

rekomendasiProduk=dfProduk[dfProduk['rating']==dfProduk['rating'].max()]
print(rekomendasiProduk)
print('Item yang mungkin anda suka adalah '+', '.join(rekomendasiProduk['nama'].head(3).tolist())) # join: mengubah list menjadi gabungan urutan string dengan pemisah tertentu


# 2. Content Based Filtering: cosinus similarity

data=[
    'Buku Komik Sejarah',
    'Buku Komik Politik',
    'Buku Hobi Kuliner',
    'Buku Kuliner Hobi',
    'Sejarah Komik Buku',
]

from sklearn.feature_extraction.text import CountVectorizer
model=CountVectorizer() 
hitung=model.fit_transform(data) # menjadikan data kedalam matriks vektor tallus
print(model.get_feature_names())
print(hitung.toarray()) 

from sklearn.metrics.pairwise import cosine_similarity
similarityScore=cosine_similarity(hitung) # memasangkan tiap elemen dengan elemen lainnya kedalam suatu matrix dan membandingkannya berdasarkan cosine similarity atau properti-properti kategori yang sama
print(similarityScore)

sayaSuka=2
print(similarityScore[sayaSuka])
print(list(enumerate(similarityScore[sayaSuka])))
print(sorted(
    list(enumerate(similarityScore[sayaSuka])), # merubah skor similaritas/korelasi menjadi list dengan index untuk masing-masing nilai
    key=lambda x: x[1], # mengambil elemen skor, x[0] merupakan elemen index
    reverse=True # membalik urutan sort
))
listRecommend=sorted(
    list(enumerate(similarityScore[sayaSuka])), # merubah skor similaritas/korelasi menjadi list dengan index untuk masing-masing nilai
    key=lambda x: x[1], # mengambil elemen skor, x[0] merupakan elemen index
    reverse=True # membalik urutan sort
)
print('Barang yang mungkin anda suka adalah barang dengan kategori:')
for i in range(0,3):
    if listRecommend[i][0]!=sayaSuka:
        print(data[listRecommend[i][0]])