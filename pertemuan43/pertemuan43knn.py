import numpy as np
import pandas as pd
from sklearn.datasets import load_iris

data=load_iris()

# print(dir(data))
# print(data['data'])
# print(data['target'])

df=pd.DataFrame(data['data'],columns=['SL','SW','PL','PW'])
df['target']=pd.DataFrame(data['target'])
df['species']=df['target'].apply(lambda x:data['target_names'][x]) # menambahkan kolom target name yang sesuai dengan angka pada kolom target
# print(df.isnull().sum()) # cek jumlah data null
# print(df.head())

def nNeighbors():
    x=round(len(data['data'])**.5)
    if x%2==0:
        return x+1
    else:
        return x

# KNN (K-Nearest Neighbour): mengelompokkan data berdasarkan data-data yang ada disekitarnya (clustering)
from sklearn.neighbors import KNeighborsClassifier
model=KNeighborsClassifier(
    n_neighbors=nNeighbors()
)

model.fit(df[['SL','SW','PL','PW']],df['target'])

df['prediksi']=model.predict(df[['SL','SW','PL','PW']])
print(df)