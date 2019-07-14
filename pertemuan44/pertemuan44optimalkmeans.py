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
print(df.isnull().sum()) # cek jumlah data null
print(df.head())

# K optimal K-Means (jumlah cluster optimal utk pemakaian k-means 0~10): SSE (sum square error) + elbow method
from sklearn.cluster import KMeans

sse=[]
for x in range(1,15):
    model=KMeans(n_clusters=x)
    model.fit(df[['SL','SW','PL','PW']])
    sse.append(model.inertia_) # nilai SSE
print(sse)

# plot = elbow method
import matplotlib.pyplot as plt
plt.plot(range(1,15),sse,'r-o')
plt.show()

# berdasarkan elbow method, pilih lengkungan paling bawah sebagai titik K optimal, pada kasus ini k=3
model=KMeans(n_clusters=3)
model.fit(df[['SL','SW','PL','PW']])
