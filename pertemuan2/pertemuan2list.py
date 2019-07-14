# contoh-contoh list dan penggunaannya
matkul=['Kalkulus','Astronomi','Elektronika']
genap=[0,2,4,6,8,10,12]
ganjil=[1.0,3.0,5.0]
boolean=[True, False]
campur=['Andi',21,'Budi',22]
x=12
y=13
z=14
s=[x,y,z]
print(s)
print(len(s))
print(s[0])
print(s[1])
print(s[2])
print(s[len(s)-1])
print(s[-1])
print(s[-2])
print(s[0:3]) # start:end
print(s[0:1])
print(s[1:3])
print(s[1:7])
print(s[0:3:2]) # start:end:step
print(s[0::2]) # print all from start with 2 steps
print(s[::2]) # print all with 2 steps

students=['Andi','Budi','Caca','Deni','Budi']
newStudents=['Euis','Fafa']
additionalStudents='Gilang'

print(students.index('Budi')) # nomor index elemen Budi
print(students.count('Budi')) # jumlah elemen Budi

students.extend(newStudents) # menambahkan elemen-elemen pada list tertentu
print(students)
students.append(additionalStudents) # menambahkan suatu var sebagai satu elemen pada list
print(students)
students.append(newStudents)
print(students)
print(students[-1][0]) # mengambil elemen urutan terakhir, apabila elemen tersebut list maka mengambil index yang ke 0 dari list tsb
print(students[-1][1])

students.insert(3,'Zaza') # menambah elemen pada index tertentu
print(students)

students.remove('Budi') # menghapus suatu elemen tertentu secara spesifik
print(students)

# students.clear() # menghapus semua elemen
# students.pop() # menghapus elemen terakhir
# students.pop(2) # menghapus elemen index ke-2

# students.sort() # mengurutkan sesuai jenis variabel
# students.reverse() # membalikkan urutan index
print(students)

# sorting angka pada elemen-elemen tertentu
angka=[14,2,34,12,67,2]
print(angka)

x=angka[0:3]
x.sort()
print(x)

angka[0:3]=x # atau angka[0:len(x)]=x
print(angka)
print(angka[1])