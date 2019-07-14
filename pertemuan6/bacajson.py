import json

# convert dict => json
x={
    'nama':'Andi',
    'usia':23
}
x2=['Andi','Budi']

y=json.dumps(x) # mengoutput data dgn format json ke dalam format string
y2=json.dumps(x2)

z1='aku string biasa'
z2=json.dumps(z1)

print(x)
print(y)
print(x2)
print(y2)
print(type(y2))
print(z2)

tesx='{"nama":"Andi"}'
tesx2='["Andi","Budi","Caca"]'
tesy=json.loads(tesx) # mengambil suatu data sesuai jenisnya dari format string
tesy2=json.loads(tesx2)

print(tesx)
print(tesy)
print(type(tesy))
print(tesy['nama'])
print(tesx2)
print(tesy2)
print(tesy2[1])

with open('data.json') as dataku:
    data=json.load(dataku) # mengambil suatu data sesuai jenisnya dari suatu file

print(data)
print(type(data))
print(data[1]['nama'])
print(data[3][0])

kota={
    'id':2,
    'kota':'Medan'
}
medan=json.dumps(x)

jsonku=open('medan.json','w')
jsonku.write(medan)

