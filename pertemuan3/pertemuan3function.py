#if statement

sudahKerja = True

if sudahKerja: # karena boolean hanya ada 2 nilai, maka statement ini dianggap sudahKerja == True
    print('Traktiran dong!')
else:
    print('Sukses nyari kerja yak')

job = 'PNS'

if job=='PNS':
    print('Anda PNS')
elif job=='Swasta':
    print('Anda swasta')
else:
    print('Anda nganggur')

bekerja = False
jomblo = True

if bekerja and jomblo:
    print('Anda sudah kerja, kok jomblo?')
elif bekerja and not(jomblo): # berarti jomblo == False, khusus boolean
    print('Selamat ~ ~ ~')
elif not(bekerja and jomblo):
    print('Cari kerja dulu sana!')
else:
    print('Anda belum kerja, ko sudah taken?')

nilai=60

if nilai>=80:
    print('Nilai anda =',nilai,'=> Anda lulus!')
elif 80>nilai>=60:
    print('Nilai anda =',nilai,', => anda remedial')
elif nilai<60 and nilai>=0:
    print('Nilai anda =',nilai,'=> anda tidak lulus')
else:
    print('Anda tidak ikut ujian')

angka=input('Silahkan ketik angka: ')

if angka.isdigit()==True:
    if int(angka)%2==0:
        print('Angka genap')
    else:
        print('Angka ganjil')
else:
    print('input tidak valid')

# buat program kalkulator sederhana untuk memproses angka sbg berikut
# input('Input angka pertama = ')
# input('Input operator = ')
# input('Input angka kedua = ')
# print('Hasil=...)

# buat program untuk menghitung body mass index (BMI) dan IMT dgn rumus
# bmi = berat badan / (tinggi badan)
# print('Hasil IMT=... Anda tergolong=...')

#buat program konversi mata uang IDR=>USD dan USD=>IDR
# input('input konversi yang diinginkan= ')
# input('input nilai Rp= ')
# print('Nilai tukar $1 dengan rupiah adalah Rp...')
# print('Hasil konversi = $...')