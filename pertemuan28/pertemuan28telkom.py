import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

tgl_tlkm=pd.read_csv(
    'tlkm.csv',
    index_col=False, # menghilangkan kolom index pada csv dan diganti dengan kolom index default
    parse_dates=['Tanggal'] # merubah data string pada kolom tanggal menjadi data timestamp
    )
tgl_tlkm=tgl_tlkm.set_index('Tanggal') # mengubah kolom tanggal menjadi index agar bisa diproses lebih mudah oleh pandas

print(tgl_tlkm)
print(tgl_tlkm.head())
# print(type(tgl_tlkm['Tanggal'][0]))
print(tgl_tlkm.sort_index()) # sortir data berdasarkan jenis indexnya

tgl_tlkm=tgl_tlkm.sort_index()
print(tgl_tlkm['2019'])
print(tgl_tlkm['2019-02']) # menampilkan data berdasarkan tahun bulan dan tanggal tertentu jika timestamp dijadikan index
# print(tgl_tlkm['20190227']) # menampilkan data dengan index tanggal tertentu, dapat digunakan apabila data tidak disortir terlebih dahulu
# print(tgl_tlkm['2019-02-27']) # dapat digunakan apabila data tidak disortir terlebih dahulu
# print(tgl_tlkm['27-02-2019']) # dapat digunakan apabila data tidak disortir terlebih dahulu
print(tgl_tlkm.loc['2019-02-27']) # menampilkan data dengan index tertentu kedalam series
print(tgl_tlkm.loc['20190227'])
print(tgl_tlkm.loc['27-02-2019'])
print(tgl_tlkm['27-02-2019':'28-02-2019']) # menampilkan data dalam range tertentu
print(tgl_tlkm['2019-02-27':'2019-02-28'])
print(tgl_tlkm['20190227':'20190228'])

print(tgl_tlkm['2019-03']['Close'].mean())
print(tgl_tlkm['2019-03']['Close'].max())
print(tgl_tlkm['2019-03']['Close'].min())

print(tgl_tlkm[tgl_tlkm['Close']==tgl_tlkm['2019-03']['Close'].max()])

plt.plot(
    tgl_tlkm.index, tgl_tlkm['Open'],'g-',
    tgl_tlkm.index, tgl_tlkm['Close'],'r-'
)
plt.xlabel('Tanggal')
plt.ylabel('Rp')
plt.xticks(rotation=65)
plt.grid(True)
plt.legend(['Open','Close'])
plt.show()