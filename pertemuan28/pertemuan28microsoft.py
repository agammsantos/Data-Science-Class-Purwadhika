import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df1=pd.read_csv(
    'MSFT.csv',
    parse_dates=['Date'], # merubah data string pada kolom tanggal menjadi data timestamp
    index_col='Date'
    )
print(df1)
print(df1['Close'].resample('M').mean()) # menampilkan rata-rata dari sampling bulanan data close 
print(df1['Close'].resample('W').mean()) # menampilkan rata-rata dari sampling mingguan data close
print(df1['Close'].resample('Q').mean()) # menampilkan rata-rata dari sampling kuartil tahun data close
print(df1['Close'].resample('Y').mean()) # menampilkan rata-rata dari sampling tahunan data close

df2=pd.read_csv(
    'AAPL.csv',
    parse_dates=['Date'] # merubah data string pada kolom tanggal menjadi data timestamp
    )
print(df2)

plt.plot(
    df1.index,df1['Adj Close'],'r-',
    df2['Date'],df2['Adj Close'],'g-'
)
plt.xlabel('Tanggal')
plt.ylabel('$')
plt.xticks(rotation=65)
plt.grid(True)
plt.legend(['Microsoft','Apple'])
plt.show()