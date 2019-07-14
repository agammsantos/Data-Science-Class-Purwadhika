import numpy as np
import pandas as pd
from sklearn.datasets import load_digits

dataDigit=load_digits()

print(dir(dataDigit))
print(len(dataDigit['images']))
print(dataDigit['data'][1796]) # array dari matriks data image
print(dataDigit['images'][1796]) # matriks data image yg berupa representasi dari gambar yang dapat diplot
print(dataDigit['target'][1796]) # angka yang tertera pada gambar image
import matplotlib.pyplot as plt

# plt.gray()
# plt.imshow(dataDigit['images'][1796])
# plt.show()

# menunjukkan 10 data gambar pertama dalam dataset digits kedalam suatu figure
# fig=plt.figure('Digit Dataset',figsize=(10,5))
# for i in range(10):
#     plt.subplot(2,5,i+1) # plt.subplot(<jumlah baris>,<jumlah kolom>,<posisi subplot 1~(barisxkolom)>)
#     plt.imshow(dataDigit['images'][i]) # data gambar angka ternyata berurutan sesuai index
#     plt.title('Ini angka = {}'.format(dataDigit['target'][i]))
# plt.show()

angka=input('Masukkan tanggal lahir: ') # print gambar angka-angka dari tanggal lahir
fig=plt.figure('Digit Dataset',figsize=(10,5))
for i in range(len(angka)):
    plt.subplot(1,len(angka),i+1) # plt.subplot(<jumlah baris>,<jumlah kolom>,<posisi subplot 1~(barisxkolom)>)
    plt.imshow(dataDigit['images'][int(angka[i])])
    plt.title('angka {}'.format(dataDigit['target'][int(angka[i])]))
plt.show()