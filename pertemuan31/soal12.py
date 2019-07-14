import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model

df=pd.read_excel('indo_12_1.xls',skipfooter=3,header=3,na_values='-',index_col=0)
# df=df.rename(columns={'Unnamed: 0':'Provinsi'})
df.index.name='Provinsi'
print(df)

sum_ind=[]
for i in df.columns.values:
    sum_ind.append(np.sum(df[i]))
print(sum_ind)
max2010=str(df[df[2010]==df[2010].max()].index.values[0])
min1971=str(df[df[1971]==df[1971].min()].index.values[0])
print(max2010)
print(min1971)
provinsimax2010=df.transpose()[max2010]
provinsimin1971=df.transpose()[min1971]
print(provinsimax2010)
print(provinsimin1971)

plt.plot(
    df.columns.values,sum_ind,'r-o',
    df.columns.values,provinsimax2010,'g-o',
    df.columns.values,provinsimin1971,'b-o',
)
plt.grid(True)

model=linear_model.LinearRegression()
model.fit(np.transpose(np.matrix(df.columns.values)),sum_ind) # digunakan tranpose karena matriks 2D yang dibuat harus dalam bentuk matriks list horizontal
print('Slope =', model.coef_)
print('Intercept =', model.intercept_)
df1=model.predict(np.transpose(np.matrix(df.columns.values)))

model.fit(np.transpose(np.matrix(df.columns.values)),provinsimax2010)
print('Slope =', model.coef_)
print('Intercept =', model.intercept_)
df2=model.predict(np.transpose(np.matrix(df.columns.values)))

model.fit(np.transpose(np.matrix(df.columns.values)),provinsimin1971)
print('Slope =', model.coef_)
print('Intercept =', model.intercept_)
df3=model.predict(np.transpose(np.matrix(df.columns.values)))

# melihat skor dependency kedua variabel / skor relasi R^2 kedua variabel yang akan dicek, apabila nilai 0.85 s/d 1 maka nilai relasi kedua variabel bagus
print(model.score(np.transpose(np.matrix(df.columns.values)),provinsimin1971))

plt.plot(
    df.columns.values,df1,'orange',
    df.columns.values,df2,'orange',
    df.columns.values,df3,'orange',
)
plt.legend(['Pertumbuhan Penduduk Indonesia','Pertumbuhan penduduk '+max2010,'Pertumbuhan penduduk '+min1971,'Best fit'])
plt.grid(True)
plt.show()