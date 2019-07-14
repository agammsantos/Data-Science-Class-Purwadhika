import matplotlib.pyplot as plt
import numpy as np

x=np.arange(5)
y=np.array([1,2,3,4,5])
z=2*y
# plt.plot(x,y,'r-',x,z,'g--')

# fig 1
plt.figure('Ini grafik nomor satu')
plt.plot(x,y,'r-')
plt.grid(True)
plt.title('Grafik 1')
plt.xlabel('Nilai x')
plt.ylabel('Nilai y')
plt.legend(['Hubungan x-y'])

# fig 2
plt.figure('Ini grafik nomor dua')
plt.plot(x,z,'g--')
plt.grid(True)
plt.title('Grafik 2')
plt.xlabel('Nilai x')
plt.ylabel('Nilai z')
plt.legend(['Hubungan x-z'])

plt.figure('Ini grafik nomor tiga', figsize=(10,5)) # grafik dgn lebar 10 dan tinggi 5
plt.suptitle('2 Grafik') # super title

plt.subplot(1,2,1) # posisi subplot ada pada baris pertama kolom pertama dari jumlah baris:1 dan kolom:2
plt.plot(x,y,'r-')
plt.grid(True)
plt.title('Grafik 1')
plt.xlabel('Nilai x')
plt.ylabel('Nilai y')
plt.legend(['Hubungan x-y'])
plt.scatter(x,y, color='y', marker='s', s=200) # menambahkan plot titik dgn warna bentuk dan size tertentu
plt.bar(x,y, color='g') # menambahkan plot bar dgn warna bentuk dan size tertentu

plt.subplot(122) # posisi subplot ada pada baris pertama kolom kedua dari jumlah baris:1 dan kolom:2
plt.plot(x,z,'g--')
plt.grid(True)
plt.title('Grafik 2')
plt.xlabel('Nilai x')
plt.ylabel('Nilai z')
plt.legend(['Hubungan x-z'])
plt.scatter(x,z, color='pink', marker='*', s=200) # menambahkan plot titik dgn warna bentuk dan size tertentu
plt.bar(x,z, color='blue') # menambahkan plot bar dgn warna bentuk dan size tertentu

plt.figure('Ini grafik nomor 4')
plt.bar(x,z,color='k', yerr=0.4) # memberi keterangan garis margin error pada grafik nilai y
plt.bar(x,y,color='r', bottom=z) # menumpuk grafik ini diatas nilai z atau grafik x-z

plt.figure('Ini figure nomor lima')
plt.hist(y,x,histtype='bar',rwidth=0.5) # menambahkan plot tipe histogram dengan lebar bar tertentu

color=['r','orange','y','g','b']
plt.figure('Ini figure nomor enam')
plt.pie(x,labels=x,startangle=-90,colors=color, # menambahkan plot tipe pie dengan sudut mulai dari kuadran 1 dikurang 90* dgn warna2 tertentu
    shadow=True, explode=(0,0.3,0,0,0), # menambahkan shadow dan potongan pie pada plot
    autopct='%1.1f%%', textprops={'color':'brown'}) # menambahkan keterangan berupa persen pada label dgn warna seluruh teks coklat
plt.legend(x)

plt.show()
