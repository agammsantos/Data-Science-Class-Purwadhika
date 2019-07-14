jenis=input('''\
    Pilih tipe konversi uang yang diinginkan:
    A. USD => RP
    B. RP => USD
''')
if jenis.lower()=='a' or jenis.lower()=='b':
    if jenis.lower()=='a':
        nilai=input('Nilai USD: ')
        if nilai.isdigit():
            print('Nilai konversi: USD 1 = Rp10.000')
            konversiRp=14150
            nilai=float(nilai)
            print('Hasil konversi: Rp',nilai*konversiRp)
        else:
            print('Harap memasukkan nilai nominal dengan benar')
    elif jenis.lower()=='b':
        nilai=input('Nilai Rp: ')
        if nilai.isdigit():
            print('Nilai konversi: Rp 1 = USD 0.000071')
            konversiUsd=0.000071
            nilai=float(nilai)
            print('Hasil konversi: Rp',nilai*konversiUsd)
        else:
            print('Harap memasukkan nilai nominal dengan benar')
else:
    print('Harap menginputkan pilihan yang ada')
