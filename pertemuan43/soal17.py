import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

df=pd.read_csv('pulsar_stars.csv')
print(df.head())
dfnew=pd.DataFrame()
dfnew['Mean IP']=df[df.columns.values[0]]
dfnew['SD IP']=df[df.columns.values[1]]
dfnew['Mean curve']=df[df.columns.values[4]]
dfnew['SD curve']=df[df.columns.values[5]]
dftarget=df['target_class']
print(dfnew.head())

# mengubah data asli menjadi data skala
# from sklearn.preprocessing import MinMaxScaler
# scaler = MinMaxScaler(feature_range=(0,1))
# features_scaled = scaler.fit_transform(dfnew)
# print(features_scaled)

from sklearn.model_selection import train_test_split
xtr,xts,ytr,yts=train_test_split(dfnew,dftarget,test_size=.2,random_state=42)

def nNeighbors():
    x=round(len(df['target_class'])**.5)
    if x%2==0:
        return x+1
    else:
        return x

from sklearn.neighbors import KNeighborsClassifier
model=KNeighborsClassifier(
    n_neighbors=nNeighbors()
) 
model.fit(xtr,ytr)
dfnew['prediksi']=model.predict(np.matrix(dfnew))
dfnametarget=['Negative','Positive']
dfnew['hasilPrediksi']=dfnew['prediksi'].apply(lambda x: dfnametarget[x])
print(dfnew)
print(model.score(xts,yts))

from sklearn.metrics import classification_report
print(classification_report(dftarget,dfnew['prediksi']))
# print(dftarget)