# Collaborative Filtering
import numpy as np
import pandas as pd

df = pd.read_csv('ratingUser.csv',delimiter=',',index_col=0,)
df.fillna(0,inplace=True)
print(df)

# Correlation
'''
pearson : standard correlation coefficient
kendall : Kendall Tau correlation coefficient
spearman : Spearman correlation coefficient
'''
dfCorr = df.corr() # default:pearson
# print(df_corr)

# testing
preferensiSaya = [
    ('kartun_a',4),
    ('sinetron_b',1)
]

skor_sama = pd.DataFrame()
for produk, rating in preferensiSaya:
    skor = dfCorr[produk] * (rating-2.5) # standarisasi dengan nilai median 2.5, karena nilai rating netral adalah 2.5
    skor = skor.sort_values(ascending = False) # sorting dataseries yg diambil dari besar ke kecil
    skor_sama = skor_sama.append(skor,ignore_index=False) # tambahkan kedalam satu dataframe
    print(skor_sama)
   
print(skor_sama.sum().sort_values(ascending=False)) # jumlahkan kedua hasil masukkan korelasi kemudian menampilkannya dalam ranking rekomendasi
mixRating=skor_sama.sum().sort_values(ascending=False)
print(mixRating[mixRating.values>0].index.values) # rekomendasi untuk rating korelasi di atas 0
acaraRecommend=mixRating[mixRating.values>0].index.values
for i in range(0,len(preferensiSaya)):
    acaraRecommend=acaraRecommend[acaraRecommend!=preferensiSaya[i][0]] # merekomendasikan acara yang belum ditonton
print('Acara TV yang mungkin anda suka adalah:',', '.join(acaraRecommend))