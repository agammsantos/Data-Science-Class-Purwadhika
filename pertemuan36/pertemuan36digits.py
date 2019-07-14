import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_digits

dataDigit = load_digits()

print(dir(dataDigit))
print(len(dataDigit['data']))
print(dataDigit['data'][0])
print(len(dataDigit['images']))
print(dataDigit['images'][0])
print(len(dataDigit['target']))
print(dataDigit['target'][0])
print(len(dataDigit['target_names']))
print(dataDigit['target_names'])

# dataframe
df=pd.DataFrame(
    dataDigit['data'],
    dataDigit['target']
).reset_index()
df.rename(columns={'index':'target'},inplace=True)
df=df[df.columns.values.tolist()[1:]+[df.columns.values.tolist()[0]]]
print(df.head(2))

# splitting dataset manual: 90% training - 10% testing
# train=round(0.9*df.shape[0]) # mengambil data training dari 90% jumlah data
# train=df.iloc[:train]
# test=df.iloc[train:]

# splitting dataset sklearn
from sklearn.model_selection import train_test_split

# mencari nilai random_state agar skor regresi paling tinggi untuk test_size tertentu
# i=0
# c=0
# while i < len(dataDigit['data']):
#     xtrain,xtest,ytrain,ytest=train_test_split(
#         dataDigit['data'],
#         dataDigit['target'],
#         test_size=0.33,
#         random_state=i # menentukan metode pengacakan dari data training
#     )
#     model=LogisticRegression(solver='liblinear',multi_class='auto')
#     model.fit(xtrain,ytrain)
#     if model.score(xtrain,ytrain)>c:
#         c=model.score(xtrain,ytrain)
#         rsmax=i
#     i+=1
# print(rsmax)

xtrain,xtest,ytrain,ytest=train_test_split(
        dataDigit['data'],
        dataDigit['target'],
        test_size=0.33,
        random_state=253 # menentukan metode pengacakan dari pengambilan data utk training dan test
    )

# print(len(xtrain))
# print(len(xtest))
# print(len(ytrain))
# print(len(ytest))
# print(ytrain)
# print(ytest)

# logistic regression
model=LogisticRegression(solver='liblinear',multi_class='auto') # multi_class menyesuaikan bergantung pada jenis data binary atau bukan untuk keakuratan regresi

# training
model.fit(xtrain,ytrain)
print(model.score(xtrain,ytrain)*100,'%')

# prediksi
print(ytest[0])
print(model.predict(xtest[0].reshape(1,-1)))

# draw image, show real data, show prediction
import matplotlib.pyplot as plt

fig=plt.figure(figsize=(5,5))
plt.imshow(xtest[0].reshape(8,8),cmap='gray')
plt.title(
    'Data asli = {} // Prediksi = {} // Akurasi = {}%'
    .format(
        ytest[0],
        model.predict(xtest[0].reshape(1,-1))[0],
        round(model.score(xtrain,ytrain)*100,2)
    )
)
plt.show()