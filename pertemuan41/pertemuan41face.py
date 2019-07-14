import numpy as np
import pandas as pd
from sklearn.datasets import fetch_olivetti_faces

faces=fetch_olivetti_faces()
print(dir(faces))
print(len(faces.data))
print(len(faces.images[0]))
print(len(faces.images[0][0]))
print(faces['images'][0].shape)
print(faces.target)
print(list(dict.fromkeys(faces.target))) # menjadikan list target menjadi key-key dictionary yang unik kemudian dilist

import matplotlib.pyplot as plt
# plt.imshow(faces.images[0],cmap='gray')
# plt.show()

# splitting
from sklearn.model_selection import train_test_split
xtr,xts,ytr,yts=train_test_split(
    faces.data,
    faces.target,
    test_size=.15
)

# decision tree
from sklearn import tree
model=tree.DecisionTreeClassifier()
model.fit(xtr,ytr)

# logistic regression
from sklearn.linear_model import LogisticRegression
model2=LogisticRegression(
    solver='liblinear',
    multi_class='auto'
)
model2.fit(xtr,ytr)
print(xts[0].reshape(64,64))

# plot
plt.imshow(xts[0].reshape(64,64),cmap='gray')
plt.title(
    'DataAsli: {} / DT: {} / SkorDT: {}% / LR: {} / SkorLR: {}%'
    .format(yts[0],model.predict([xts[0]])[0],round(model.score(xts,yts)*100,2),model2.predict([xts[0]])[0],round(model2.score(xts,yts)*100,2))
)
plt.show()