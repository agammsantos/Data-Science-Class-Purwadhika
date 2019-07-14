# {'key' : 'value'} dictionary

namaHari={
    'Monday':'Senin',
    'Tuesday':'Selasa',
    'Wednesday':'Rabu'
}

print(type(namaHari))
print(namaHari['Monday'])
print(namaHari.get('Tuesday')) # pengambilan data versi python lama
print(namaHari.get('Tuesday','Maaf data tidak tersedia')) # pengambilan dengan syarat apabila data tidak ada maka teroutput argumen
print(namaHari.get('Friday','Maaf data tidak tersedia'))

print(namaHari.keys())
print(list(namaHari.keys())) # data yang diambil menjadi list

print(namaHari.values())
print(list(namaHari.values()))

print(
    list(namaHari.keys())[list(namaHari.values()).index('Senin')]
)