import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression,LogisticRegression
from sklearn.datasets import fetch_california_housing

data=fetch_california_housing()
# print(dir(data))
# print(len(data['data']))
# print(len(data['data'][0]))
print(len(data['target']))
print(data['target'][0])

df=pd.DataFrame(
    data['data'],
    columns=data['feature_names']
)
df['harga']=data['target']
print(df.head())

# split
from sklearn.model_selection import train_test_split
xtrain,xtest,ytrain,ytest=train_test_split(
    df[df.columns.values[0:8]],
    df['harga'],
    test_size=0.1
)
print(len(xtrain))
print(len(ytrain))
print(len(xtest))
print(len(ytest))

# linear regression
model=LinearRegression()
model.fit(xtrain,ytrain)

print(model.predict(xtest)[0])
print(ytest.iloc[0])

df['hPred']=model.predict(df[df.drop('harga',axis=1).columns.values])
print(df.head())

# plotting
plt.subplot(221)
plt.scatter(
    df['HouseAge'],
    df['harga']
)
plt.subplot(222)
plt.scatter(
    df['HouseAge'],
    df['hPred']
)
plt.subplot(2,2,(3,4))
sns.heatmap(df.corr(),annot=True)
# plt.tight_layout()
plt.show()