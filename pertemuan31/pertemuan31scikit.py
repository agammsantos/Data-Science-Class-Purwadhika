# pip install scikit-learn
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sklearn

print(sklearn.__version__)

# data penjualan luas tanah dan harganya
x=np.array([5000,20000,25000,13000,8439])
y=np.array([11.5,50,55,32.5,27])*1000000000

df=pd.DataFrame({
    'x':x,
    'y':y
}).sort_values(by='x')
print(df)

# linear regression skLearn
from sklearn import linear_model
model=linear_model.LinearRegression()

# training .fit(data independent[2D], data dependent[1D])
model.fit(df[['x']],df['y']) # best fit line

print('Slope =', model.coef_)
print('Intercept =', model.intercept_)
print(model.predict([[10000]])) # prediksi dari regresi linear untuk nilai y jika x=200
df['yBest']=model.predict(df[['x']])
print(df)

# plotting
plt.plot(
    df['x'],df['y'],'g-',
    df['x'],df['yBest'],'r-'
)
plt.grid(True)
plt.show()