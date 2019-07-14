# Regresi untuk data yang non-linear dan memiliki tren pada titik-titik tertentu:
# Ridge Regression dan Lasso Regression
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# data dummy
x=10*np.random.RandomState(1).rand(50)
x=np.sort(x)
# x=np.linspace(0,10,100)
print(x)
y=2*x-5+np.random.RandomState(1).randn(50) # data random dengan distribusi normal
# y=np.sin(x)
print(y)

# plot dummy data
# plt.scatter(x,y)
# plt.show()


from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline
# linear regression, polynomial, make_pipeline
from sklearn.linear_model import LinearRegression # tidak berbeda dengan ridge apabila menggunakan pipeline dan polynomial
modelLinear=make_pipeline(
    PolynomialFeatures(7),
    LinearRegression()
)
modelLinear.fit(x.reshape(-1,1),y)


# lasso regression, polynomial, make_pipeline
from sklearn.linear_model import Lasso
modelLasso=make_pipeline(
    PolynomialFeatures(7),
    Lasso(alpha=1e-15,max_iter=100000)
)
modelLasso.fit(x.reshape(-1,1),y)


# ridge regression, polynomial, make_pipeline
from sklearn.linear_model import Ridge
modelRidge=make_pipeline(
    PolynomialFeatures(7),
    Ridge(alpha=1e-15)
)
modelRidge.fit(x.reshape(-1,1),y)


# plot best fit line
fig=plt.figure('Regression',figsize=(15,6))

plt.subplot(131)
plt.scatter(x,y)
plt.plot(x,modelLinear.predict(x.reshape(-1,1)))
plt.title('Linear Regression')

plt.subplot(132)
plt.scatter(x,y)
plt.plot(x,modelLasso.predict(x.reshape(-1,1)))
plt.title('Lasso Regression')

plt.subplot(133)
plt.scatter(x,y)
plt.plot(x,modelRidge.predict(x.reshape(-1,1)))
plt.title('Ridge Regression')

plt.show()
