# string

nama='Andi Susilo Siregar'

print(nama.lower()) # mengecilkan huruf
print(nama.upper()) # mengkapitalkan huruf
print(nama.isupper()) # cek apakah semua kapital
print(nama.islower()) # cek apakah semua kecil
print(nama.lower().islower())
print(nama.upper().isupper())
print(type(nama.upper().isupper()))
print(len(nama)-1) # panjang karakter
print(nama[0])
print(nama[10])
print(nama[len(nama)-1])
print(nama.index('Siregar')) # urutan karakter pertama yang disebutkan
print(nama.replace('Siregar','Hadiwijaya')) # mengganti karakter atau kata tertentu
print(nama.split('i')) # memisahkan string pada huruf yang didefinisikan, menjadi barisan
print(nama.split(' '))
print(nama.split(' ')[1]) # memisahkan dan mengoutput baris/entry pertama

# penghitung jumlah huruf di nama seseorang? (spasi tidak dihitung)
# penghitung jumlah huruf tertentu dalam suatu kata