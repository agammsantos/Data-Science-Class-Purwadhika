import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df_main=pd.read_csv('data.csv')

df=df_main.copy()

print(df['Overall'].max())
print(df['Overall'].min())
print(df['Overall'].mean())

print(df[df['Overall']==df['Overall'].max()])
print(df[df['Overall']==df['Overall'].max()]['Name'])
print(df[df['Overall']==df['Overall'].max()][['Name','Club']]) # konsep multi-filter

print(df[df['Overall']>=90][['Name','Position','Club']])
print(df[['Name','Position','Club']][df['Overall']>=90])

print(
    df[['Name','Position','Club']]
    [df['Overall']>=90]
    [df['Club']=='Real Madrid']
)

df=df[['Name','Position','Club','Overall']][df['Overall']>=90]
df=df[df['Club']=='Real Madrid']
print(df)
print(df['Overall'])
print(df.T) # transpose dataframe
dftranspose=df.T
print(dftranspose)
print(dftranspose.index)