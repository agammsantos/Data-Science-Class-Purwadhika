import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from collections import OrderedDict

# cara list
df=pd.read_csv(
    'tes.csv',
    na_values=['-','n.a','not available'] # mengganti value yang terlist sebagai NaN
)

# cara dict
df=pd.read_csv(
    'tes.csv',
    na_values={
        'usia':['-','not available',-1], # mengganti value yang terlist perkolom sebagai NaN
        'job':['-','not available']
    }
)

# df=df.fillna(0) # mengganti data NaN dengan data tertentu
# df=df.fillna({
#     'usia':23,
#     'job':'Staff'
# })

# df=df.fillna(method='ffill',axis=1) # forward filling, mengganti data NaN dengan data di kolom sebelah kiri dari tabelnya (sb x)
# df=df.fillna(method='ffill',axis=0) # mengganti data NaN dengan data di baris atas dari tabelnya (sb y)

# df=df.fillna(method='bfill',axis=1) # backward filling, mengganti data NaN dengan data di kolom sebelah kanan dari tabelnya (sb x) 
# df=df.fillna(method='bfill',axis=0) # mengganti data NaN dengan data di baris bawah dari tabelnya (sb y)

# df=df.interpolate() # mengisi data yang kosong (int) dengan data interpolasi atau data yang berada pada range batas-batasnya secara berurut (baris paling atas dan paling bawah)
df=df.interpolate().fillna({
    'nama':'Anonim',
    'usia':20,
    'job':'Jobless'
})

# df=df.dropna() # menghapus seluruh baris data yang memuat setidaknya satu data NaN
# df=df.dropna(how='all') # menghapus seluruh baris data yang seluruhnya memuat data NaN
# df=df.dropna(thresh=2) # menghapus seluruh baris data yang tidak memuat seminimalnya 2 kolom terisi
# df=df.dropna(subset=['job','nama']) # menghapus seluruh baris data dari data yang kolom 'job' dan 'nama'nya terdapat NaN

# df=df.replace(['-','-1','not available'], 0) # mengganti data-data tertentu dengan data yang diinginkan
# df=df.replace({ # mengganti data-data tertentu dengan beberapa data yang diinginkan
#     '-':'+',
#     '-1':'+1',
#     'not available':'available'
# })
# df=df.replace({ # mengganti data-data spesifik di kolom tertentu dengan data-data yang bersesuaian
#     'nama':['-','+']
# },{
#     'nama':['Andini','Bambang']
# })
# df=df.replace( # mengganti data tertentu dengan method backward filling
#     to_replace='-',
#     method='bfill'
# )
# df['usia']=df['usia'].replace( # cara lain mengganti data tertentu di kolom yang diinginkan
#     to_replace=['-1','-'],
#     method='bfill'
# )
# df=df.replace(['-','-1','not available'], np.NaN)
# df=df.fillna('haha')

print(df[df['kota']=='Jakarta']) # mengambil data dengan isi kolom 'kota' tertentu

dfkota=df.groupby('kota') # mengelompokkan data berdasarkan kategori pada kolom kota sebagai kolom kategori
print(dfkota.get_group('Jakarta')) # memanggil data dengan kategori group jakarta
# print(dfkota[dfkota['usia']==dfkota['usia'].max(numeric_only='int')])
print(dfkota.min(numeric_only='int')) # memanggil data minimal dalam kolom yang berisi integer untuk setiap kategori kota dan menampilkannya sebagai series
print(dfkota.min(level='usia')) # memanggil data minimal untuk seluruh kolom (secara alfabetikal dan numerikal) untuk setiap kategori kota

df2=[
    {'nama':'Mr. X','usia':22, 'berat':77}, # data baru
    {'nama':'Mr. Z','usia':24, 'berat':87}, # data baru
    {'nama':'Andi','berat':68}, # data pelengkap
    {'nama':'Deni','berat':70} # data pelengkap
]
df2=pd.DataFrame(df2,index=[5,6,0,3]) # index untuk mengenali data yang sama pada dataframe lainnya, tidak digunakan apabila data digabung menggunakan merge

dfAll=pd.concat(  # concatinate, menggabungkan dua dataframe yang berbeda dan menyesuaikan kolom beserta indexnya di tabel yang baru
    [df,df2], 
    # ignore_index=True, # ignore index dari dataframe asal sebelum digabungkan
    # keys=['DF1','DF2'], # mengelompokkan dataframe2 yang telah digabungkan, tidak bisa digunakan bersamaan dengan ignore_index
    sort=False, # sortir kolom setelah digabung ditiadakan, atau dapat gunakan ordereddict
    axis=1 # memasukkan dataframe baru kedalam kolom disebelah kanan dari dataframe sebelumnya jika axis=1, kedalam baris dibawah jika axis=0, sesuai denggan indexnya, tidak tepat untuk digunakan apabila index dari data yang sama tidak diketahui karena perlu proses lebih lanjut
    )

# dfAllMerge=pd.merge(df,df2,on='nama',how='left') # menggabungkan kedua data yang berbeda berdasarkan properti tertentu dengan metode left join, penting bahwa data kedua harus memiliki jumlah kolom yg seragam dan suatu variabel properti yang sama dengan variabel properti data pertama

print(df)
print(dfAll)
# print(dfAll.loc['DF1'])
# print(dfAllMerge)