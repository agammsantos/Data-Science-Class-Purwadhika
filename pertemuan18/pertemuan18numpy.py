# pip install numpy
# python -m pip install numpy

import numpy as np

x1=[1,2,3,4,5,6]
x2=(1,2,3,4,5,6)
x3={1,2,3,4,5,6} # masih tetap set apabila diubah mjd ndarray namun tipenya berubah
y1=np.array(x1)
y2=np.array(x2)
y3=np.array(x3)
z1=np.array(['a','b','c'])
z2=np.arange(100)
z3=np.arange(5,100)
z4=np.arange(50,100,2)
z5=np.array([1,'a',2,'b',3,'c'])

print(x1)
print(type(x1))
print(y1)
print(y2)
print(y3)
print(type(y3))
print(y2[0])
print(z1)
print(z2)
print(z3)
print(z4)
print(z4.ndim) # dimensi dari array
print(len(z4))
print(z4.size) # jumlah elemen
print(z4.itemsize) # ukuran dalam bytes (B)
print(z4.dtype) # menentukan tipe array
print(z5.dtype) # unicode string yg kurang dari 11 karakter


x=np.random.rand(5) # menampilkan 5 angka random dari 0 sampai 1
y=np.random.rand(4,5) # menampilkan array 4x5 berisi angka random 0 sampai 1
z=np.random.randint(10) # menampilkan 1 angka dengan range hingga 10
j=np.random.randint(10, size=10) # menampilkan angka2 random dengan ukuran list 10
k=np.random.randint(10, size=(1,10)) # menampilkan angka2 random dengan ukuran matriks 1x10

print(x)
print(y)
print(z)
print(j)
print(k)

satu=np.array([1,2,3])
dua=np.array([[1,2,3]])
tiga=np.array([[[1,2,3]]])
a=[[[[1,2,3,11],[4,5,6,12],[7,8,9,13]]]]
a=np.array(a)
b=a.reshape(6,2) # membentuk ulang array dengan shape yg diinginkan

print(satu.ndim)
print(dua.ndim)
print(tiga.ndim)
print(a.ndim)
print(a.shape) # bentuk array dalam jumlah elemen tiap dimensi
print(b)
print(b.shape)
print(a[0][0][1][3])
print(a[0,0,1,3]) # mengoutput data dalam array dgn cara numpy
print(a[0:,0:,0:,3:]) # mengoutput data2 tertentu dalam array
print(a[0:,0:,0:,3])
print(a[:,:,:,[0,2]])

x=np.linspace(1,10,10) # menampilkan data dengan step yg merata dan jumlah tertentu (awal,akhir,jumlah elemen) dlm bentuk array
y=np.random.randint(10,size=(1,10))

print(x)
print(y)
print(y.shape)
print(y.max())
print(y.min())

x1=np.array([1,2,3])
x2=np.array([4,2,0])
x3=np.array([[1,2,3],[4,5,6]])

print(x1+x2)
print(x1-x2)
print(x1*x2)
print(x1/x2)
print(x3+x3)
print(x3-x3)
print(x3*x3)
print(x3/x3)

a=np.array([[2,1],[1,1]])
b=np.array([5,7])
c=np.linalg.solve(a,b) # menyelesaikan persamaan linear dengan format (matriks koefisien, matriks konstanta)
print(c)
