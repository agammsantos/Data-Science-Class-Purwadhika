import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression,LogisticRegression
from sklearn.datasets import fetch_olivetti_faces

data=fetch_olivetti_faces()
print(dir(data))

print(data['data'][0])
print(len(data['images'][0]))
print(len(data['images'][0][0]))
print(data['images'][0].shape)

# import matplotlib.pyplot as plt
# fig=plt.figure('Wajah',figsize=(10,5))
# for i in range(10):
#     orangke=3
#     plt.subplot(2,5,i+1)
#     plt.imshow(data['images'][i+(10*(orangke-1))],cmap='gray')
# plt.show()

print(data['target'])

# train
from sklearn.model_selection import train_test_split
xtrain,xtest,ytrain,ytest=train_test_split(
    data['data'],
    data['target'],
    test_size=0.1,
    random_state=40
)
model=LogisticRegression(solver='liblinear',multi_class='auto')
model.fit(xtrain,ytrain)
print(model.score(xtrain,ytrain)*100,'%')

# import matplotlib.pyplot as plt
# fig=plt.figure('Wajah',figsize=(10,5))
# for i in range(10):
#     orangke=22
#     plt.subplot(2,5,i+1)
#     plt.imshow(data['images'][i+(10*(orangke))],cmap='gray')
#     plt.title('{},{}'.format(data['target'][i+(10*(orangke))],model.predict(data['data'][i+(10*(orangke))].reshape(1,-1))))
# plt.show()

# evaluasi model (pelajari lebih lanjut)
from sklearn.metrics import classification_report
print(classification_report(ytest,model.predict(xtest)))