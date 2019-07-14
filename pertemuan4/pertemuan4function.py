# function file

'''
format:
def namaFungsi():
    program

namaFungsi()
'''

def tes():
    print('Halo ini function!')

tes()

def halo(nama):
    print('Halo',nama)

halo('Andi')
halo(input('Ketik nama: '))

def hitung(x,y):
    z=x**y
    print('Hasil kali',x,'dan',y,'=',x*y)
    print('Hasil pangkat',x,'dan',y,'=',x**y)

hitung(2,3)

import math

def luasLingkaran(r):
    luas=math.pi*r*r
    print('Luas lingkaran dg r= ',r,'adalah',luas)

luasLingkaran(7)

def luasTrapesium(a,b,t):
    luas=(a+b)*(t/2)
    print('Luas trap a=',a,'b=',b,'t=',t,'adalah',luas)

luasTrapesium(3.2,6.1,4)

# return function

def aloha():
    print('Halo Andi')

def hai():
    return 'Halo Andi'

x='Halo Andi'

print(x)
print(hai())

def hola(nama):
    return 'Halo '+nama

def kuadrat(x):
    return x**2

print(kuadrat(12)+kuadrat(2))
print(kuadrat(8))
print(kuadrat(20))

# kurs mata uang

kurs={
    '1': 0.000071,
    '2': 14140
}

def konversi():
    print('Selamat datang di web KonversiDuit.com')
    print('Silakan pilih metode konversi:')
    print('1. IDR ke USD')
    print('2. USD ke IDR')
    metode=input('Ketik pilihan anda: ')
    if metode=='1':
        nominal=input('Ketik nominal Rupiah: Rp ')
        if nominal.replace('.','').replace(',','').isdigit():
            hasil=float(nominal.replace(',','.'))*kurs[metode]
            print('Konversi Rp',nominal,'= $',hasil)
        else:
            print('Mohon inputkan hanya angka')
    elif metode=='2':
        nominal=input('Ketik nominal Dollar: $ ')
        if nominal.replace('.','').replace(',','').isdigit():
            hasil=float(nominal.replace(',','.'))*kurs[metode]
            print('Konversi $',nominal,'= Rp',hasil)
        else:
            print('Mohon inputkan hanya angka')
    else:
        print('Harap masukkan metode konversi yang tersedia')

konversi()

# string format

print('Halo {}, umurmu {}'.format('Andi',27))
print('Halo {1}, umurmu {0}'.format('Andi',27))
print('Asalmu dari {kota}'.format(kota='Depok'))
print('Suhu udara = {:f}'.format(25))

x='Halo {:s}'
print(x.format('12'))

x=50000
print(x)
print('{:,}'.format(x))
print('{:,}'.format(x).replace(',','.'))