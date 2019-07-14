# pip install pandas

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ini adalah list, pada dasarnya tabel dengan 1 baris
# nama=['Andi','Budi','Caca']
# print(nama)

# nama=np.array(['Andi','Budi','Caca'])

# # pandas series, pada dasarnya tabel dengan 1 kolom, dapat dibuat dari list dan tuple
# nama=pd.Series(nama, name='Students', index=['a','b','c'])
# print(nama)
# print(nama[2])
# print(nama['b'])
# print(nama[0:2])
# print(nama[0:3:2])
# print(nama['a':'c'])
# print(nama['a':'c':2])

# nama=np.array([1,2,3,4,5])
# nama=pd.Series(nama, name='Students', index=['a','b','c','d','e'])
# print(nama)
# print(nama[2])
# print(nama['b'])
# print(nama[0:2])

# nama='agam'
# nama=pd.Series(nama, name='Students', index=['a','b','c'])
# print(nama)
# print(nama[2])

# nama=np.arange(10)
# nama=pd.Series(nama, name='Students')
# print(nama)
# print(nama[2])
# plt.plot(nama,nama)
# plt.show()


# Dataframe
nilai=[2,3,4,6,2,4,7,9,1]
nama=['Andi','Budi','Caca','Deni','Euis','Fafa','Gani','Hani','Inne']
dfNilai=pd.DataFrame()
dfNilai['Nama']=nama
dfNilai['Nilai']=nilai
print(dfNilai)

dfNilai=pd.DataFrame([nama,nilai])
print(dfNilai)

# Dataframe list of list
data=[
    ['Andi',90],
    ['Budi',80],
    ['Caca',95],
    ['Dedi',65],
    ['Enni',70]
]

dfData=pd.DataFrame(data,columns=['name','score'])
print(dfData)
print(dfData.shape) # jumlah baris,kolom


# Dataframe numpy array
data=np.arange(10)

dfData=pd.DataFrame(data,columns=['score'])
print(dfData)
print(dfData.shape) # jumlah baris,kolom


# Datafram dictionary, yang paling umum digunakan
data={
    'nama':['Andi','Budi','Caca'],
    'score':[87,78,90]
}
dfData=pd.DataFrame(data)
print(dfData)
print(dfData.shape)

data=[
    {'nama':'Andi', 'score':87},
    {'nama':'Budi', 'score':78},
    {'nama':'Caca', 'score':90},
    {'nama':'Deni', 'score':90},
    {'nama':'Euis', 'score':90},
    {'nama':'Fafa', 'score':60}
]
dfData=pd.DataFrame(data,index=list('abcdef'))
print(dfData)
print(dfData.shape)
print(dfData.head()) # mengambil 5 baris data pertama
print(dfData.head(3)) # mengambil 3 baris data pertama
print(dfData.tail()) # mengambil 5 baris data terakhir
print(dfData.tail(2)) # mengambil 2 baris data terakhir

print(dfData.columns) # menampilkan nama-nama kolom yg ada
print(dfData.index) # menampilkan index dari data yang ada

print(dfData.values) # menampilkan nilai-nilai yang ada dalam dataframe kedalam bentuk numpy array
print(dfData.describe()) # mendeskripsikan data yang ada dengan detail-detail statistik yg dapat dipanggil
print(dfData.sort_index(ascending=False)) # mengurutkan data berdasarkan index
print(dfData.sort_values(by='score')) # mengurutkan data berdasarkan nilai tertentu
print(dfData.sort_values(
    by=['score','nama'], # mengurutkan data dari kolom nilai kemudian data dari kolom nama
    ascending=[False,False] # mengurutkan kedua data secara descending
))

print(dfData['nama']) # menampilkan kolom nama dari dataframe dfData kedalam bentuk panda series
print(dfData['score'])
print(dfData[0:1]) # memanggil nilai dengan index slicing tertentu
print(dfData.loc['a']) # memanggil nilai berdasarkan nama index tertentu
print(dfData.loc['a':'d',['score']]) # memanggil nilai dalam range index tertentu yg ada pada kolom score
print(dfData.iloc[0]) # memanggil nilai dalam index default tertentu kedalam bentuk panda series apabila hanya 1 baris
print(dfData.iloc[0:5:2,0:2]) # memanggil nilai yang ada pada index default 0 sampai 4 dengan step 2, dan pada kolom pertama hingga kedua 
print(dfData.at['a','nama']) # memanggil nilai pada index 'a' di kolom 'nama'
print(dfData.iat[0,1]) # memanggil nilai pada index default 0 di kolom 1

print(dfData.iloc[0:6:2,0:2].sort_values(by=['score','nama'],ascending=[True,False])[['score','nama']]) # konsep multi-filter

# plotting dataframe
plt.plot(dfData['nama'],dfData['score'])
plt.show()