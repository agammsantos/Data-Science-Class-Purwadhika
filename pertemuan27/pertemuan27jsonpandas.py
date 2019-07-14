import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import json
from collections import OrderedDict

df=pd.read_json('tes.json',) # membaca file json dan menjadikannya dataframe dengan mengurutkan kolom sesuai abjad, merupakan fitur asli dari json
# df=df.set_index('id')
# df=df.sort_values(by='id')

data = json.load(open('tes.json'), object_pairs_hook=OrderedDict) # membaca file json jika ingin urutan kolom pada dataframe tetap sesuai dengan filenya
dforder=pd.DataFrame(data)
print(dforder)

cols=df.columns.tolist() # menampilkan kolom yang ada kedalam list
print(cols)

# cols=cols[-1:]+cols[:-1] # membalikkan urutan kolom terakhir menjadi pertama
# df=df[cols]
df=df[['id','nama','kota']] # memilih kolom yang ingin ditampilkan sesuai urutan secara manual
print(df)

df.to_csv('haha.csv',index=False) # mengimport kedalam file csv

# pip install openpyxl
df.to_excel('haha.xlsx',index=False) # mengimport kedalam file excel, apabila dipreview tidak menampilkan kolom utama, tidak masalah

df=df.sort_values(by='id')
df.to_json('haha.json',orient='records') # mengimport kedalam file json, orient = records, values, index, table, columns


print(df)