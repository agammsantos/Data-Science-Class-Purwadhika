from bs4 import BeautifulSoup
import requests
import mysql.connector
import csv
import base64

mydb=mysql.connector.connect(
    host='localhost',
    user='agammsantos',
    password=base64.b64decode(b"RGFuY2VyMTE5OQ==").decode('utf-8'),
    database='digimon'
)

y=requests.get('https://wikimon.net/Visual_List_of_Digimon')
z=BeautifulSoup(y.content,'html.parser')
i=2
j=2
nama=[]
gambar=[]
table=z.find('div',id="mw-content-text")
data=table.find_all('table')
# print(data)
while i<len(data)-1:
    if str(data[i])!='None':
        if str(data[i].tr)!='None':
            if str(data[i].tr.td)!='None':
                if str(data[i].tr.td.a)!='None':
                    if str(data[i].tr.td.a.img)!='None':
                        nama.append(data[i].tr.td.a.img.get('alt'))
                        gambar.append(data[i].tr.td.a.img.get('src'))
    i+=1
i=0
gambarfix=[]
while i<len(gambar):
    gambarfix.append('https://wikimon.net'+gambar[i])
    i+=1
i=0
datafix=[]
while i<len(gambarfix):
    datafix.append(nama[i]+', '+gambarfix[i])
    i+=1
# print(type(datafix))
# print(len(nama))
# print(len(gambar))
with open('digimondb.csv','w',newline='',encoding='utf-8') as digimondb:
    header=['nama','gambar']
    a=csv.writer(digimondb)
    a.writerow(header)
    a.writerows(zip(nama,gambarfix)) # menyatukan list menjadi satu
digimondb.close()

i=0
x=mydb.cursor()
while i<len(nama):
    x.execute('insert into digimon (nama,gambar) values (%s,%s);',(nama[i],gambarfix[i]))
    mydb.commit()
    # data=x.fetchall()
    i+=1
