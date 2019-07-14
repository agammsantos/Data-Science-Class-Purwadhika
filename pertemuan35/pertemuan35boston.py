import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_boston

dataBoston=load_boston()
print(dataBoston) # data sample
print(dir(dataBoston)) # properti yang menyusun file data
print(len(dataBoston.data)) # total rows data sample 
print(dataBoston.data[0]) # 1st data sample
print(len(dataBoston.data[0])) # total column
print(dataBoston.data.shape)
print(dataBoston['data'].shape)

print(dataBoston['feature_names']) # feature / column names
print(dataBoston['filename']) # sumber file csv dari dataBoston

print(dataBoston['target']) # data y atau data dependent utama bagi seluruh data dalam dataBoston.data, dalam dataset ini berupa harga rumah di boston
print(len(dataBoston['target']))


# create dataframe
dfBoston=pd.DataFrame(
    dataBoston['data'],
    columns=dataBoston['feature_names']
)
dfBoston['MEDV']=dataBoston['target']
print(dfBoston.head(5))


# model linear regression
from sklearn.linear_model import LinearRegression
model=LinearRegression()
model.fit(
    dfBoston[dataBoston['feature_names']], # x 2D, 2D karena dataBoston['feature_names'] sudah berbentuk list juga
    dfBoston['MEDV'] # y 1D
    )
print(model.coef_)
print(model.intercept_)
print(model.score(
    dfBoston[dataBoston['feature_names']],
    dfBoston['MEDV']
    )*100)

# print(model.score( # mengecek score regression apabila kolom x yg digunakan hanya kolom 'CRIM'
#     dfBoston[['CRIM']],
#     dfBoston['MEDV']
#     )*100)