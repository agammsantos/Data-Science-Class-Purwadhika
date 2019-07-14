import numpy as np
import pandas as pd

data=[
    {'luas':1000,'harga':1000,'kota':'Bekasi'},
    {'luas':2000,'harga':2000,'kota':'Bekasi'},
    {'luas':3000,'harga':3000,'kota':'Bekasi'},
    {'luas':1000,'harga':2000,'kota':'Depok'},
    {'luas':2000,'harga':3000,'kota':'Depok'},
    {'luas':3000,'harga':4000,'kota':'Depok'},
    {'luas':1000,'harga':5000,'kota':'Jakarta'},
    {'luas':2000,'harga':10000,'kota':'Jakarta'},
    {'luas':3000,'harga':15000,'kota':'Jakarta'},
]

# 1. pandas get dummies
df=pd.DataFrame(data)
dfNew=pd.get_dummies(df['kota']) # menjadikan suatu kolom menjadi dummies variable/kategorikal untuk model machine learning
print(dfNew)
print(df.head(5))
dfComplete=pd.concat([df,dfNew],axis='columns').drop('kota',axis='columns')
print(dfComplete.head())

# # 2. sklearn One Hot Encoding
# df=pd.DataFrame(data)
# # 2a. labelling
# from sklearn.preprocessing import LabelEncoder
# label=LabelEncoder()
# df['kota']=label.fit_transform(df['kota'])
# print(df)

# dfX=df[['kota']].values
# print(dfX)
# dfY=df['harga']
# print(dfY)

# # 2b. one hot encoder
# from sklearn.preprocessing import OneHotEncoder
# from sklearn.compose import ColumnTransformer


# coltrans=ColumnTransformer(
#     [('OHE',OneHotEncoder(categories='auto'),[0])], # merubah kolom pertama pada suatu dataframe dari jenis label menjadi jenis dummies menggunakan one hot encoder
#     remainder='passthrough'
# )
# dfX=np.array(coltrans.fit_transform(dfX)).astype(int)

# # dibawah berikut merupakan cara alternatif, pada one hot encoder apabila semua kolom sudah tergabung tidak perlu dilakukan lagi
# # yang dilakukan disini adalah membuat matriks 0 dengan dimensi yang menyesuaikan, kemudian menggantinya dengan matriks dfX dan kolom luas agar keduanya dapat digunakan sebagai xtrain pada regresi
# dfXfix=np.zeros((len(dfX),4))
# for i in range(len(df['luas'])):
#     dfXfix[i]=np.append(dfX[i],df['luas'][i])
# print(dfXfix.astype(int))

# # linear regression
# from sklearn.linear_model import LinearRegression
# modelLR=LinearRegression()
# modelLR.fit(dfXfix,dfY)
# print(modelLR.predict([[1,0,0,1000]]))