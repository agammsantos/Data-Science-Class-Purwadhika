import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression

df = pd.read_excel('regresiDataDiskrit.xlsx')
print(df.head())

# logistic regression
logr=LogisticRegression(solver='lbfgs') # solver merupakan jenis algoritma yang digunakan, default adalah liblinear, baca documentation utk detail
logr.fit(df[['usia (x)']],df['nikah (y)'])

# slope dan intercept
m=logr.coef_
c=logr.intercept_
print(m)
print(c)

# predict dan skor
print(logr.score(df[['usia (x)']],df['nikah (y)']))
print(logr.predict([[31]]))
print(logr.predict_proba([[31]])) # cek tingkat keakuratan yang diperoleh oleh model untuk tiap kemungkinan nilai y yang ada
print(logr.predict([[30]]))
print(logr.predict_proba([[30]]))