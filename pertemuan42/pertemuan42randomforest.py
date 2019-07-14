# random forest (metode klasifikasi berupa kumpulan dari beberapa decision tree)
import numpy as np
import pandas as pd
from sklearn.datasets import load_digits

digit=load_digits()
print(dir(digit))
print(digit['target_names'])
print(len(digit['target']))
print(digit['data'][0])
print(digit['images'][0])

df=pd.DataFrame(digit['data'])
df['target']=digit['target']
print(df.head(3))

# split: 10% test & 90% train
from sklearn.model_selection import train_test_split
a,b,c,d=train_test_split(
    df.drop(['target'],axis='columns'),
    df['target'],
    test_size=.1
)
# print(len(a))
# print(len(b))
print(a[0])
print(c.iloc[0])


# random forest (mencari feature-feature yang paling optimal untuk prediksi)
from sklearn.ensemble import RandomForestClassifier
model=RandomForestClassifier(n_estimators=50) # n_estimators=50 : pembagian sub-sample untuk decision tree=50
model.fit(a,c)

# extreme random forest (feature-feature yang diambil benar-benar random)
from sklearn.ensemble import ExtraTreesClassifier
modelExtra=ExtraTreesClassifier(n_estimators=50)
modelExtra.fit(a,c)

# predict random forest
d_pred=model.predict(b)[0]
score=model.score(b,d)
print(d.iloc[0])
print(d_pred)
print(round(score*100),'%')

# predict extra random forest
d_predExtra=modelExtra.predict(b)[0]
scoreExtra=modelExtra.score(b,d)

# plot
import matplotlib.pyplot as plt
plt.imshow(b.iloc[0].values.reshape(8,8))
plt.title('Dataset: {} || PRF: {} || SRF: {} || PERF: {} || SERF: {}'.format(d.iloc[0],d_pred,str(round(score*100))+'%',d_predExtra,str(round(scoreExtra*100))+'%'))
plt.show()