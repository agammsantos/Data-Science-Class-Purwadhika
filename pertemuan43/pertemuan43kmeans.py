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
# print(df.head())

# k-means: mengelompokkan data melalui rerata jarak terdekat dari titik pusat massa/sentroid yang jumlahnya ditentukan (clustering)
from sklearn.cluster import KMeans
model1=KMeans(n_clusters=len(data['target_names']),random_state=1)
model2=KMeans(n_clusters=len(data['target_names']),random_state=1)

model1.fit(df[['SL','SW']],df['target'])
model2.fit(df[['PL','PW']],df['target'])

# prediksi
# print(model2.predict(df[['PL','PW']]))
df['prediksiS']=model1.predict(df[['SL','SW']])
df['prediksiP']=model2.predict(df[['PL','PW']])

df1=df[data['target']==0]
df2=df[data['target']==1]
df3=df[data['target']==2]

dfS1=df[df['prediksiS']==0]
dfS2=df[df['prediksiS']==1]
dfS3=df[df['prediksiS']==2]

dfP1=df[df['prediksiP']==0]
dfP2=df[df['prediksiP']==1]
dfP3=df[df['prediksiP']==2]

# print(model1.cluster_centers_)
# print(model2.cluster_centers_)
centroidS=model1.cluster_centers_ # titik pusat massa cluster sepal
centroidP=model2.cluster_centers_ # titik pusat massa cluster petal

# plotting data dan sentroid
import matplotlib.pyplot as plt
fig=plt.figure('Data Iris',figsize=(10,10))
plt.subplot(221)
plt.plot(df1['SL'],df1['SW'],'r.')
plt.plot(df2['SL'],df2['SW'],'g.')
plt.plot(df3['SL'],df3['SW'],'b.')
plt.scatter(
    centroidS[:,0],
    centroidS[:,1],
    marker='*',
    color='y',
    s=200
)
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Sepal Width (cm)')
plt.legend(['Setosa','Versicolor','Virginica','Sentroid'])
plt.title('Data Asli')

plt.subplot(222)
plt.plot(df1['PL'],df1['PW'],'r.')
plt.plot(df2['PL'],df2['PW'],'g.')
plt.plot(df3['PL'],df3['PW'],'b.')
plt.scatter(
    centroidP[:,0],
    centroidP[:,1],
    marker='*',
    color='y',
    s=200
)
plt.xlabel('Petal Length (cm)')
plt.ylabel('Petal Width (cm)')
plt.legend(['Setosa','Versicolor','Virginica','Sentroid'])
plt.title('Data Asli')

plt.subplot(223)
plt.plot(dfS1['SL'],dfS1['SW'],'r.')
plt.plot(dfS2['SL'],dfS2['SW'],'b.')
plt.plot(dfS3['SL'],dfS3['SW'],'g.')
plt.scatter(
    centroidS[:,0],
    centroidS[:,1],
    marker='*',
    color='y',
    s=200
)
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Sepal Width (cm)')
plt.legend(['Setosa','Virginica','Versicolor','Sentroid'])
plt.title('Clustering K-means')

plt.subplot(224)
plt.plot(dfP1['PL'],dfP1['PW'],'r.')
plt.plot(dfP2['PL'],dfP2['PW'],'b.')
plt.plot(dfP3['PL'],dfP3['PW'],'g.')
plt.scatter(
    centroidP[:,0],
    centroidP[:,1],
    marker='*',
    color='y',
    s=200
)
plt.xlabel('Petal Length (cm)')
plt.ylabel('Petal Width (cm)')
plt.legend(['Setosa','Virginica','Versicolor','Sentroid'])
plt.title('Clustering K-means')

plt.show()

