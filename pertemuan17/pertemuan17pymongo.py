# pip install pymongo
# python -m pip install pymongo

from pymongo import MongoClient
from flask import jsonify

# menghubungkan ke server mongodb yg berjalan
x=MongoClient('mongodb://localhost:27017/')
# print(x.list_database_names())

db=x['agamdb']
col=db['produk']

nama=input('Ketik nama produk: ')
harga=input('Ketik harga produk: ')

cari1={'harga':{'$gt':1000000}}
cari2={'nama':'Headset'}
data={'nama':nama,'harga':int(harga)}

# menampilkan data pada collection
# print(list(col.find()))
for x in col.find(cari1):
    print(x)

for x in col.find(cari2):
    print(x)

# menambahkan data kedalam collection
z=col.insert_one(data)
print(z.inserted_id)
for i in col.find({'_id':z.inserted_id}):
    print('Data sukses tersimpan!')
    print(i)