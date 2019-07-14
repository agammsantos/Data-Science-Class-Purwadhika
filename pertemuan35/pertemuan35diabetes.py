import numpy as np
import pandas as pd
from sklearn.datasets import load_diabetes

dataDiabet=load_diabetes()

print(dir(dataDiabet))
print(dataDiabet['data_filename'])
print(dataDiabet['target_filename'])
print(dataDiabet['feature_names'])

print(dataDiabet['target']) # data y atau data dependent utama bagi seluruh data dalam dataBoston.data, dalam dataset ini target berupa quantitative measure of disease progression one year after baseline
print(len(dataDiabet['target']))

print(dataDiabet['data'])
print(dataDiabet['data'].shape)


# create dataframe
dfDiabet=pd.DataFrame(
    dataDiabet['data'],
    columns=dataDiabet['feature_names']
)
dfDiabet['y']=dataDiabet['target']
print(dfDiabet.head(5)) # value data yang ada didalam dataframe seluruhnya telah dinormalisasi sehingga berbentuk suatu nilai skala