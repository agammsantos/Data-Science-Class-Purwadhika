# multivariable linear regression
# multiple variables
# y = m1x1 + m2x2 + m3x3 + ... + c

import numpy as np
import pandas as pd

df=pd.read_csv('hargaRumah.csv')
print(df)

# linear regression
from sklearn import linear_model as lm
model=lm.LinearRegression()
model.fit(df[['usia','kamar','luas']],df['harga'])

m=model.coef_
c=model.intercept_
print(m)
print(c)

# prediksi
print(model.predict([[5,10,2000]]))
print(model.predict([[50,1,2000]]))

# score
print(round(model.score(
    df[['usia','kamar','luas']],
    df['harga']
)*100,3),'%')

# save model with PICKLE: pip install pickle
# import pickle # merupakan library bawaan python
# with open('modelPickle.pkl','wb') as fileku:
#     pickle.dump(model,fileku) # akan menyimpan file python beserta file-file lain yang dipanggil dari kodingan tersebut kedalam satu file pkl, bisa digunakan untuk file-file biasa

# save model with JOBLIB: pip install joblib
import joblib as jb # dapat dipanggil apabila diinstal karena merupakan library sendiri
# import sklearn.externals.joblib as jb # merupakan library bawaan scikitlearn
jb.dump(model,'modelJoblib')