import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df1=pd.read_csv('tes.csv',skiprows=2,skipfooter=1) # membaca csv dengan menghapus 2 baris pertama dan 1 baris terakhir, kemudian menjadi dataframe

print(df1)
print(df1['nama'])


df2=pd.read_csv('tes2.csv',header=None,names=['No KTP','Nama Lengkap','Score']) # membaca csv dengan mengeset header custom dari coding

print(df2)


data=pd.read_csv('data.csv')
tua1=data[data['Age']>=25][data['Overall']>=85]
tua2=data[data['Age']>=25][data['Overall']<85]
muda1=data[data['Age']<25][data['Overall']>=85]
muda2=data[data['Age']<25][data['Overall']<85]

plt.scatter(tua1['Age'],tua1['Overall'],c='blue')
plt.scatter(tua2['Age'],tua2['Overall'],c='orange')
plt.scatter(muda1['Age'],muda1['Overall'],c='g')
plt.scatter(muda2['Age'],muda2['Overall'],c='r')
plt.grid(True)
plt.legend(['Tua+','Tua-','Muda+','Muda-'])
plt.xlabel('Usia')
plt.ylabel('Performa')

plt.show()