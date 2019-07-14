# GET API http://jsonplaceholder.typicode.com/users
# requests = 3rd party library => pip
# Install pip and requests
# win
    # pip --version
    # pip -V
    # py -m pip --version
    # py -m pip install -U pip setuptools
    # python -m pip install -U pip setuptools

# install package via pip
# 1. pip install namaPackage => pip install requests
# 2. py -m pip install namaPackage

import requests
import json

# url='http://jsonplaceholder.typicode.com/users'
# data=requests.get(url)
# print(data)
# print(data.json()[1])
# print(type(data.json()))

# hasilJson=json.dumps(data.json())
# fileJson=open('datauser.json','w')
# fileJson.write(hasilJson)

# namaKlub=input('Masukkan nama klub: ')
# if namaKlub.count(' ')>=1:
#     namaKlub.replace(' ','_')
# url='https://www.thesportsdb.com/api/v1/json/1/searchplayers.php?t='+namaKlub
# players=requests.get(url)
# # print(players.json()['player'])
# for player in players.json()['player']:
#     print(player['strPlayer'],'(',player['strNationality'],')')

nama=input('Ketik nama pemain: ')
if nama.count(' ')>=1:
    nama.replace(' ','_')
url='https://www.thesportsdb.com/api/v1/json/1/searchplayers.php?p='+nama
namaPlayer=requests.get(url)
for player in namaPlayer.json()['player']:
    print(player['strTeam'])

# get api dengan apikey / apiid

# namaKota=input('Masukkan nama kota: ')
# apikey='f55d63d6a8b8c097bec0d502cca59755'
# url='http://api.openweathermap.org/data/2.5/weather?q='+namaKota+'&APPID='+apikey

# dataCuaca=requests.get(url)
# cuaca=dataCuaca.json()['weather'][0]['main']
# suhu=dataCuaca.json()['main']['temp']
# lembab=dataCuaca.json()['main']['humidity']

# # print(dataCuaca.json())
# print('Cuaca=',cuaca)
# print('Suhu=',round(suhu-273,2),'*C')
# print('Kelembaban=',lembab,'%')