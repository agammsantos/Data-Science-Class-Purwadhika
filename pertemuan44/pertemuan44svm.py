# SVM Support Vector Machine: Membuat garis linear/nonlinear pembatas untuk masing-masing cluster, dapat dilihat dengan plot countour

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

#  Note: 
#  target = 12 | prediksi: 11.8  12.1  12.3  11.7  (akurat)
#  target = 12 | prediksi: 10  10  10  10  (presisi)
#  target = 12 | prediksi: 12  12  12  12  (akurat & presisi)

# SVM
from sklearn.svm import SVC
modelP=SVC(gamma='auto')
modelP.fit(df[['PL','PW']],df['target'])
modelS=SVC(gamma='auto')
modelS.fit(df[['SL','SW']],df['target'])
df['prediksiP']=modelP.predict(df[['PL','PW']])
df['prediksiS']=modelS.predict(df[['SL','SW']])
print(df[df['target']==0])
print(df[df['target']==1])
print(df[df['target']==2])

from sklearn.metrics import classification_report, confusion_matrix
print(classification_report(df['target'],df['prediksiP']))
print(confusion_matrix(df['target'],df['prediksiP'])) # jika target ada 3 kategori, maka matriks akan berbentuk 3x3 dgn kolom menyatakan jumlah prediksi masing-masing target dan baris menyatakan kategori target

# data terluar (ditambah 1 dan dikurang 1 agar plotting diluar titik-titik max dan min rapih)
xp_max=df['PL'].max()+1
xp_min=df['PL'].min()-1
yp_max=df['PW'].max()+1
yp_min=df['PW'].min()-1

xs_max=df['SL'].max()+1
xs_min=df['SL'].min()-1
ys_max=df['SW'].max()+1
ys_min=df['SW'].min()-1
# print(x_max,x_min,y_max,y_min)

x=np.linspace(0,1,3)
y=np.linspace(0,1,2)
print(x)
print(y)
a,b=np.meshgrid(x,y) # menghasilkan 2 matriks meshgrid, hasil ukuran matriks meshgrid adalah baris=len(y), kolom=len(x)
print(a)
print(b)

# meshgrid biasa digunakan untuk menghasilkan gabungan matriks berupa titik-titik grid yang merata untuk diplot 
XP,YP=np.meshgrid(
    np.arange(xp_min,xp_max,0.01),
    np.arange(yp_min,yp_max,0.01)
)
XS,YS=np.meshgrid(
    np.arange(xs_min,xs_max,0.01),
    np.arange(ys_min,ys_max,0.01)
)
print(XP)
print(YP)
print(XP.ravel()) # merubah matriks kedalam array 1D, sama seperti reshape
print(YP.ravel())

# x ravel = [x1 x2 x3 x4 x5]
# y ravel = [y1 y2 y3 y4 y5]

ZP=modelP.predict(np.c_[XP.ravel(),YP.ravel()]) # c_: memasangkan kedua elemen-elemen array secara satu persatu dan menjadikannya matriks [[x,y]]
ZS=modelS.predict(np.c_[XS.ravel(),YS.ravel()]) 
ZP=ZP.reshape(XP.shape)
ZS=ZS.reshape(XS.shape)

import matplotlib.pyplot as plt
fig=plt.figure('SVM Data Iris')
gbr=plt.subplot(121)
gbr.contourf(XP,YP,ZP,cmap='seismic',alpha=.1) # plot contour

# import matplotlib.pyplot as plt
plt.plot(
    df[df['target']==0]['PL'],
    df[df['target']==0]['PW'],
    'r.'
)
plt.plot(
    df[df['target']==1]['PL'],
    df[df['target']==1]['PW'],
    'g.'
)
plt.plot(
    df[df['target']==2]['PL'],
    df[df['target']==2]['PW'],
    'b.'
)

gbr=plt.subplot(122)
gbr.contourf(XS,YS,ZS,cmap='seismic',alpha=.1) # plot contour

# import matplotlib.pyplot as plt
plt.plot(
    df[df['target']==0]['SL'],
    df[df['target']==0]['SW'],
    'r.'
)
plt.plot(
    df[df['target']==1]['SL'],
    df[df['target']==1]['SW'],
    'g.'
)
plt.plot(
    df[df['target']==2]['SL'],
    df[df['target']==2]['SW'],
    'b.'
)
plt.show()