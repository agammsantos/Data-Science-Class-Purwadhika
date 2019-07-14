import matplotlib.pyplot as plt
import matplotlib.image as mimg
import numpy as np
from PIL import Image

gambar=Image.open('1.jpg').convert('L') # membuka gambar menggunakan library pillow, convert to b&w:'L' rgba:'RGBA' cmyk:'CMYK'
gambar=np.array(gambar)
print(gambar)
gbr=Image.fromarray(gambar,'L')
gbr.show()

gambar=mimg.imread('1.jpg')
gambar=gambar[:,:,2] # agar file jpg bisa dimanipulasi color mapping
print(gambar)
print(gambar.ndim) # dimensi representasi matriks dari suatu gambar
print(gambar.shape) # bentuk representasi gambar berupa (tinggi,lebar,warna:rbg/cmyk)
print(len(gambar)) # tinggi pixel gambar, secara teknis menghitung jumlah baris dari matriks representasi
print(len(gambar[0])) # lebar pixel gambar, secara teknis menghitung jumlah kolom dari matriks representasi

gbrplot=plt.imshow(gambar,cmap='rainbow') # color mapping tertentu berlaku untuk gambar png
plt.axis('off') # menghilangkan axis
plt.show()


