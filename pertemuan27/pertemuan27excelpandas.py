# pip install xlrd

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df1=pd.read_excel('Book1.xlsx','Sheet1')
df1=df1.sort_values(by='id')
df2=pd.read_excel('Book1.xlsx','Sheet2')
df2=df2.sort_values(by='id')
print(df2)

df1['gaji']=df2['gaji'] # secara default akan menggabungkan data kedua berdasarkan index default, maka jika data yg dibaca teracak tidak akan tersortir dan salah
print(df1)

# menggabungkan kedua data apabila data yang ada dalam tabel acak, sorting berdasarkan id
df1=df1.set_index('id')
df1=df1.sort_values(by='id')
df2=df2.set_index('id')
df2=df2.sort_values(by='id')
df1['gaji']=df2['gaji']
print(df1)