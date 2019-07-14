import numpy as np
import pandas as pd

# step-step untuk membentuk dataframe agar variabel2 dapat diolah pada linear regression, digunakan jika terdapat variabel data kategorikal
df=pd.read_csv('hargaRumah.csv')
# print(df.head(3))

dfDummy=pd.get_dummies(df['kota'])
# print(dfDummy)

# hapus kolom kota dari df
df=df.drop(['kota'],axis='columns')
print(df)

# concat dfDummy => df
df=pd.concat([df,dfDummy], axis=1)
print(df)

dfX=df.drop(['harga'],axis=1)
dfY=df['harga']
print(dfX.head(3))
print(dfY.head(3))

# Linear regression
from sklearn.linear_model import LinearRegression

model=LinearRegression()
model.fit(dfX,dfY)

print(model.predict([[10,2,200,1,0,0]]))
# print(model.predict(dfX))

dfNew=pd.DataFrame({
    'harga_asli':dfY,
    'harga_terbaik':model.predict(dfX).astype('int64') # merubah data float dengan banyak koma atau banyak 0 menjadi data integer
})
# print(dfNew.astype('int64')) # alternatif jika seluruh data ingin dirubah ke jenis int (int64 untuk angka-angka yang lebih besar dan presisi)
print(dfNew)
