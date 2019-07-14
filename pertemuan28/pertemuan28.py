import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.DataFrame({
    'nomor':[1,2,3,4,5],
    'nama':['Andi','Budi','Caca','Deni','Euis'],
    'gender':pd.Categorical(['L','L','P','L','P']), # list yang anggotanya terbatas untuk beberapa jenis kategori saja
    'kota':'Makassar', # apabila dimasukkan satu buah string akan mengisi seluruh baris pada kolom
    'tanggal':pd.Timestamp('20191228'), # format timestamp (tahun)(bulan)(tanggal)
    'tgl2':pd.date_range('20191228',periods=5) # memasukkan datetime dalam beberapa periode tertentu secara berurutan
})
print(df)

tgl=pd.Timestamp('20201212')
print(tgl)
print(type(tgl))
print(pd.Series(tgl).dtype) # mengecek data type menggunakan pandas

tgl2=pd.date_range('20190928',periods=3)
print(tgl2)
print(type(tgl2))
print(pd.Series(tgl2).dtype)