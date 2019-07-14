import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_excel('regresi data diskrit.xlsx')
print(df.head(3))

from sklearn.linear_model import LogisticRegression
log_model = LogisticRegression(solver='liblinear')

log_model.fit(df[['usia (x)']],df['nikah (y)'])

print(log_model.score(df[['usia (x)']],df['nikah (y)']))
m = log_model.coef_
c = log_model.intercept_
# = 1/(1+EXP(-1*(mx+c)))

x = df['usia (x)'].values
bestfitline = 1/(1+np.exp(-1*((m*x)+c))).ravel()
print(bestfitline)

plt.scatter(df['usia (x)'],df['nikah (y)'])
plt.plot(df['usia (x)'],bestfitline,'r-')
plt.grid(True)
plt.show()