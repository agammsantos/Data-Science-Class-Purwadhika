import numpy as np
import pandas as pd

x=np.sort(np.random.RandomState(1).randn(100))
print(x)
y=np.sin(-x)
y[::10]+=0.5*(np.sin(x[::10]))

import matplotlib.pyplot as plt
# plt.scatter(x,y)
# plt.show()

# decision tree regressor
from sklearn.tree import DecisionTreeRegressor
model3=DecisionTreeRegressor(max_depth=3) # max_depth=3 : kedalaman decision tree=3
model3.fit(x.reshape(-1,1),y) # dimensi x dibuat seperti pada regresi linear
model5=DecisionTreeRegressor(max_depth=5)
model5.fit(x.reshape(-1,1),y) 

# predict
y_pred3=model3.predict(x.reshape(-1,1))
y_pred5=model5.predict(x.reshape(-1,1))
# print(y_pred)

# plotting
plt.scatter(x,y)
plt.plot(x,y_pred3,'r-')
plt.plot(x,y_pred5,'g-')
plt.show()