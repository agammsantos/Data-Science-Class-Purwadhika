import numpy as np
from scipy import stats

a=np.array([[1,4],[2,5],[3,6]])
b=np.array([[3,6],[4,7],[5,8]])

print(a+b)
print(2*a)

a=np.array([[2,1,4,3],[2,5,1,2],[1,3,2,2]])
b=np.array([[1,3],[3,2],[2,5],[1,4]])

print(a*a) # operasi perkalian biasa
print(b/b)
print(a.dot(b)) # operasi perkalian matriks (dot product)
print(a@b) # operasi perkalian matriks (dot product juga)
print(np.cross(b,b)) # operasi perkalian cross (cross product) vektor pada matriks

a=np.array([[2,3],[4,5]])

print(np.linalg.det(a)) # determinan untuk matriks biasa
# print(round(np.linalg.det(a))) # jika hasil determinan tidak presisi dan hasilnya bilangan bulat
(sign,log)=np.linalg.slogdet(a) # determinan lebih presisi untuk nilai yang cukup kecil dan sangat besar
print(sign*np.exp(log))
# untuk determinan matriks 3-dimensi hasilnya berupa vektor berelemen 3, dengan masing2 entrinya berupa determinan matriks2 2-dimensinya

print(np.linalg.inv(a)) # invers matriks

print(np.pi) # pi
print(np.exp(1)) # eksponensial natural
print(np.exp(2)) 
print(np.log(np.exp(2))) # logaritma natural
print(np.log10(1000)) # logaritma bilangan 10

a=np.random.randint(5,size=(6))
print(a)
print(np.mean(a)) # rata2
print(np.median(a)) # median
print(stats.mode(a)) # modus (harus mengimport stats dari scipy)

a=np.array([
    [1,2,3],
    [4,5,6]
])
print(np.mean(a))
print(np.mean(a,axis=0)) # rata2 dari sumbu vertikal
print(np.mean(a,axis=1)) # rata2 dari sumbu horizontal


# membaca file txt dan csv
x,y,z=np.loadtxt( # membaca file txt/csv jika entrynya angka kedalam tiga list kolom
    'Book1.csv', # nama file csv
    skiprows=1, # menghilangkan baris pertama
    delimiter=';', # pemisah antar kolom
    usecols=range(3), # menyatakan panjang kolom agar delimiter terakhir tidak terbaca (jika file convert melalui excel) 
    unpack=True # membalikkan baris menjadi kolom
)
print(x)
print(y)
print(z)

z=np.loadtxt( # membaca file txt/csv jika entrynya angka kedalam tiga list kolom
    'Book1.txt', # nama file csv
    skiprows=1, # menghilangkan baris pertama
    delimiter=',', # pemisah antar kolom
    usecols=range(3), # menyatakan panjang kolom agar delimiter terakhir tidak terbaca (jika file convert melalui excel) 
    unpack=True # membalikkan baris menjadi kolom
)
print(z)

z=np.genfromtxt( # membaca file txt/csv jika entrynya angka kedalam tiga list kolom, tetap berjalan apabila ada string dan sel yg kosong
    'Book1.csv', # nama file csv
    delimiter=';', # pemisah antar kolom
    usecols=range(3), # menyatakan panjang kolom agar delimiter terakhir tidak terbaca (jika file convert melalui excel) 
    unpack=True # membalikkan baris menjadi kolom
)
print(z)
