import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from collections import OrderedDict as odi

df=pd.read_csv(
    'tlkm.csv',
    index_col=False,
    parse_dates=['Tanggal']
)

print(df.head()[['Tanggal','Open','Close']])
print(type(df['Tanggal'][0]))

df=df.head()
df=df[['Tanggal','Open','Close']]
# print(df.set_index('Tanggal'))

print(df.pivot( # meringkas data-data yang memiliki variabel kategori yang sama
    index='Open',
    columns='Tanggal'
)['Close'])

dfbaru=[
    odi({'id':1,'kota':'Jakarta','jumlah':45,'nilai':90}),
    odi({'id':1,'kota':'Bandung','jumlah':66,'nilai':92}),
    odi({'id':2,'kota':'Jakarta','jumlah':34,'nilai':67}),
    odi({'id':2,'kota':'Bandung','jumlah':76,'nilai':78}),
    odi({'id':3,'kota':'Jakarta','jumlah':99,'nilai':88}),
    odi({'id':3,'kota':'Bandung','jumlah':12,'nilai':98})
]
dfbaru=pd.DataFrame(dfbaru)
print(dfbaru)
# print(dfbaru.pivot(index='id',columns='kota')['jumlah'])

df1=dfbaru.pivot(index='id',columns='kota')['jumlah']
print(df1)
df2=pd.melt(dfbaru,id_vars=['id']) # meringkas data dengan menyebutkan seluruh/sebagian nilai dari variabel kolom-kolom yang ada
print(df2)

dfkota=[
    {'id':1,'Jakarta':45,'Bandung':90},
    {'id':2,'Jakarta':66,'Bandung':92},
    {'id':3,'Jakarta':34,'Bandung':67},
    {'id':4,'Jakarta':76,'Bandung':78},
    {'id':5,'Jakarta':99,'Bandung':88},
    {'id':6,'Jakarta':12,'Bandung':98}
]
dfkota=pd.DataFrame(dfkota)
dfkota=pd.melt(
    dfkota,
    id_vars=['id'],
    var_name='city',
    value_name='Polusi udara (ppm)'
)
print(dfkota)
print(dfkota[dfkota['city']=='Jakarta'])

# ada pula fungsi pd.crosstab yakni fungsi simple cross-tabulation dari 2 atau lebih variabel/kolom, biasa digunakan untuk tabel frekuensi