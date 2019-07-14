# Soal 1: menghitung jumlah karakter tanpa spasi
nama='Mustaqiim Agam Santoso'
i=0
panjangkarakter=0
banyakkata=len(nama.split(' '))
while i<=banyakkata-1:
    panjangkarakter+=len(nama.split(' ')[i])
    if i==banyakkata:
        break
    i+=1
print(panjangkarakter)
# cara efisien
total = len(nama)
jumlahSpasi = len(nama.split(' ')) - 1
totalTanpaSpasi = total - jumlahSpasi
print('Nama',nama,'mengandung: ',totalTanpaSpasi,'huruf')

# Soal 2: menghitung jumlah a
namaNonKapital = nama.lower()
i=0
banyakhuruf=0
banyakkata=len(namaNonKapital.split('a'))
while i<=banyakkata-1:
    banyakhuruf+=len(namaNonKapital.split('a')[i])
    if i==banyakkata-1:
        break
    i+=1
banyakhurufa=len(nama)-banyakhuruf
print(banyakhurufa)
# cara efisien
cari = 'a'
namaTanpaCari = namaNonKapital.replace(cari, '')
print('Jumlah Huruf',cari,'dalam',nama,'adalah',len(nama)-len(namaTanpaCari),'huruf')

# soalbonus: cari kata
kalimat = 'Andi tidak masuk sekolah karena sekolah kebanjiran'
cari = 'sekolah'
kalimatTanpaSekolah = kalimat.split(cari)
jumlahCari = len(kalimatTanpaSekolah) - 1
print(jumlahCari)