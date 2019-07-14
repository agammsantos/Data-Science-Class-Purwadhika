import numpy as np
import pandas as pd
import joblib as jb

# step-step untuk membentuk dataframe agar variabel2 dapat diolah pada linear regression, digunakan jika terdapat variabel data kategorikal
df=pd.read_csv('hargaRumah.csv')
# print(df.head(3))

dfDummy=pd.get_dummies(df['kota'])
# print(dfDummy)

# hapus kolom kota dari df
df=df.drop(['kota'],axis='columns')

# concat dfDummy => df
df=pd.concat([df,dfDummy], axis=1)

dfX=df.drop(['harga'],axis=1)
dfY=df['harga']

# Linear regression
from sklearn.linear_model import LinearRegression

model=LinearRegression()
model.fit(dfX,dfY)

jb.dump(model,'modelJoblib')