# decision tree

import pandas as pd
import numpy as np

df=pd.read_csv('job.csv')
# print(df)
y=df['gaji>10jt']
x=df.drop('gaji>10jt',axis='columns')
print(y)
print(x)

# label encoder
from sklearn.preprocessing import LabelEncoder
label=LabelEncoder()
x['kantor']=label.fit_transform(x['kantor'])
print(label.classes_)
x['job']=label.fit_transform(x['job'])
print(label.classes_)
x['titel']=label.fit_transform(x['titel'])
print(label.classes_)
print(x)

# one hot encoding: 3vars => 8vars (tidak dilakukan karena memperbanyak variabel dan kurang efisien)

# splitting: train & test (tidak dilakukan karena dataset kecil)
from sklearn.model_selection import train_test_split
xtrain,xtest,ytrain,ytest=train_test_split(
    x,
    y,
    test_size=.1,
    # random_state=1 # penggunaan random_state seperti ini kurang dianjurkan karena sama dengan memilah data secara manual
)

# ML decision tree
from sklearn import tree
# from sklearn.tree import DecisionTreeClassifier
model=tree.DecisionTreeClassifier(criterion='entropy')
model.fit(xtrain,ytrain)
print(round(model.score(x,y)*100,2),'%')
print(xtrain)

# ['Gojek' 'Tokopedia' 'Traveloka'] = [0 1 2]
# ['Backend' 'Datasc' 'Frontend'] = [0 1 2]
# ['S1' 'S2'] = [0 1]
print(model.predict([[0,0,0]]))
print(model.predict([[0,1,0]]))
print(model.predict([[2,2,0]]))
print(model.predict([[2,0,1]]))

# draw tree (dapat digunakan apabila data cukup bagus untuk dikenakan decision tree)
from sklearn.tree import export_graphviz
export_graphviz(model.fit(xtrain,ytrain),out_file='JobTree.dot',feature_names=['kantor','job','titel'],class_names=['gaji<10','gaji>10'])

# http://dreampuf.github.io/GraphvizOnline