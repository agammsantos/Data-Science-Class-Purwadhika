# pip install kaggle
# pip install --user kaggle
# kaggle --version

# manual create folder kaggle
# \Users\agamm> mkdir ~/.kaggle

# download dataset tergantung jenis filenya kedalam folder lokal
# > kaggle datasets download -d karangdiya/fifa19 --unzip (--force)

# liat list datasets kaggle
# > kaggle datasets list --sort-by 'updated'

import csv
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sn
sn.set(style='darkgrid')

players=[]
with open('data.csv','r',encoding='utf8') as fifa: # membuka file csv dengan library csv
    data=csv.DictReader(fifa)
    # print(data)
    for i in data:
        players.append(dict(i))

# print(players[0])
# print(len(players))
# print(players[0]['Age'])
# print(players[0]['Name'])
# print(players[0]['Overall'])

i=0
usia=[]
overall=[]
usiatuabagus=[]
overalltuabagus=[]
usiatuajelek=[]
overalltuajelek=[]
usiamudabagus=[]
overallmudabagus=[]
usiamudajelek=[]
overallmudajelek=[]
while i<len(players):
    usia.append(int(players[i]['Age']))
    overall.append(int(players[i]['Overall']))
    if usia[i]>=25 and overall[i]>=85:
        usiatuabagus.append(usia[i])
        overalltuabagus.append(overall[i])
    elif usia[i]>=25 and overall[i]<85:
        usiatuajelek.append(usia[i])
        overalltuajelek.append(overall[i])
    elif usia[i]<25 and overall[i]>=85:
        usiamudabagus.append(usia[i])
        overallmudabagus.append(overall[i])
    elif usia[i]<25 and overall[i]<85:
        usiamudajelek.append(usia[i])
        overallmudajelek.append(overall[i])
    i+=1

plt.scatter(usiatuabagus,overalltuabagus,c='blue')
plt.scatter(usiatuajelek,overalltuajelek,c='orange')
plt.scatter(usiamudabagus,overallmudabagus,c='g')
plt.scatter(usiamudajelek,overallmudajelek,c='r')
plt.grid(True)
plt.legend(['Tua+','Tua-','Muda+','Muda-'])
plt.xlabel('Usia')
plt.ylabel('Performa')

plt.show()