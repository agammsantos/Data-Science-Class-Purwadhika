import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

data=sb.load_dataset('titanic')
print(data.columns.values)

# drop data null yang tidak akan membantu training machine learning
# print(data)
# print(data[data['embarked'].isnull()==True])
# print(data.drop(data[data['embarked'].isnull()==True].index.values))

# 0. Tentukan kolom-kolom yang akan diambil sebagai data train dan data test

# 1. Labelling (apabila menggunakan one hot encoding)
# from sklearn.preprocessing import LabelEncoder
# label=LabelEncoder()
# data['sex']=label.fit_transform(data['sex'])

# 2. Create dummies
print(data.head())
dfSex=pd.get_dummies(data['sex'])
dfWho=pd.get_dummies(data['who'])
from sklearn.preprocessing import LabelEncoder # untuk kolom yang bernilai true dan false tetap menggunakan label
label=LabelEncoder()
data['alone']=label.fit_transform(data['alone'])
data['adult_male']=label.fit_transform(data['adult_male'])
data=pd.concat([data,dfSex,dfWho],axis='columns').drop(['sex','who','embarked','class','deck','embark_town','alive'],axis='columns')
print(data.head())

# 3. Split: feature X & target Y
data=data.dropna(subset=['age']) # menghilangkan data dimana kolom agenya merupakan null
x=data.drop(['survived'],axis='columns')
y=data['survived']
print(x.head())
x=np.array(x)
# print(x[0])

# 4. Split: data training
from sklearn.model_selection import train_test_split
xtrain,xtest,ytrain,ytest=train_test_split(x,y,test_size=.1,random_state=1)

# 5.a Logistic regression
from sklearn.linear_model import LogisticRegression
model=LogisticRegression() # default solver liblinear
model.fit(xtrain,ytrain)
print(round(model.score(xtest,ytest)*100,2),'%') # score apabila machine learning yang dibuat dikenakan pada data test
print(round(model.score(xtrain,ytrain)*100,2),'%') # score apabila machine learning yang dibuat dikenakan pada data training

# 5.b Decision tree
from sklearn import tree
modeltree=tree.DecisionTreeClassifier()
modeltree.fit(xtrain,ytrain)

# 6. Testing model
print(xtest[0])
print(ytest.iloc[0])
print(model.predict(xtest[0].reshape(1,-1))) # prediksi pada data training
print(model.predict([[3,30,1,1,70,1,1,0,1,0,1,0]])) # prediksi pada suatu data baru
print(model.predict([[1,20,0,0,4,1,0,0,1,0,1,0]]))
# urutan kolom prediksi: pclass age sibsp parch fare adult_male alone female male child man woman

predictions=model.predict(xtest)
# *. Mengecek rerata error prediksi, digunakan untuk model regresi linear
# from sklearn.metrics import mean_squared_error
# print(mean_squared_error(ytest,predictions))

# *. Mengecek rerata error prediksi, digunakan untuk model regresi logistik
from sklearn.metrics import classification_report
print(classification_report(ytest,predictions)) # melihat f1-score dan support, f1-score=skor model keseluruhan untuk data test, support=jumlah data yang diprediksi
from sklearn.metrics import confusion_matrix
print(confusion_matrix(ytest,predictions)) # membuat matriks dengan jumlah prediksi benar dan prediksi salah, baris pertama menyatakan prediksi benar-salah utk output 0, baris kedua menyatakan prediksi salah-benar utk output 1

# *. Save model
import joblib as jb
jb.dump(model,'modelTitanic')
jb.dump(modeltree,'treeTitanic')