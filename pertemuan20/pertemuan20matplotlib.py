#  pip install matplotlib

# from matplotlib import pyplot as plt
import matplotlib.pyplot as plt
import numpy as np

x=np.arange(10)
y=np.array([8,3,2,5,6,7,2,4,7,6])

# x=[0,1,2,3,4,5,6,7,8,9]
# y=[1,4,6,7,4,3,6,2,1,5]

print(plt.style.available) # menampilkan style2 grafik yg ada
plt.style.use('bmh') # menggunakan style grafik tertentu

# plt.plot(x,y,'r-s',x,y**2,'g^',x,y**3,'b.') # plot grafik secara bersamaan
# plt.plot(x,y,linestyle='--',color='y',linewidth=3,label='Dataku')
# plt.plot(x,y**2,'bs')
# plt.plot(x,y**3,'o','#FF00FF')
# plt.plot(x,2*y,'r-*')
plt.plot(x,y,'-*',color='pink',linestyle='-',linewidth=3)
plt.fill_between(x,y,0,facecolor='y',alpha=0.3) # mengisi luasan di bawah kurva x,y dan di atas garis y=0 dengan warna kuning transparansi 0,3
# plt.fill_between(x,y[3],y[1],facecolor='y',alpha=0.3)

i=0
while i<len(x):
    plt.text(x[i]-0.3,y[i]+0.2,f'({x[i]},{y[i]})') # memasukkan text di atas titik koordinat tertentu
    i+=1

plt.annotate( # memasukkan text keterangan untuk titik tertentu pada posisi koordinat yg diinginkan dengan fitur relasional
    'Nilai tertinggi',xy=(0,8),xytext=(1,7),
    # arrowprops=dict(facecolor='blue', shrink=0.2)
    arrowprops=dict(arrowstyle='fancy',facecolor='black') # mengatur style dari tanda panah, tidak bisa gunakan properti shrink
)

# linestyle terbatas pada -  dan --
# - : line
# -- : dash
# o : point
# s : square
# ^ : segitiga
# * : star
# . : dot
# r red, g green, b blue, y yellow 

plt.title('Tes Matplotlib') # judul grafik
plt.xlabel('Nilai x')
plt.ylabel('Nilai y')
plt.xticks(np.arange(-2,len(x),step=1),rotation=90) # mengatur indikator garis bilangan dan memutar teksnya
plt.yticks(np.arange(-2,len(y)),rotation=90)

plt.grid(True) # menampilkan grid/ garis2 kotak
plt.legend(['x , y','x , y^2','x , y^3','x , 2*y'], loc=0) # data legend dengan posisi legend dalam rentang 0-10
plt.savefig('ini grafikku.png') # autosave grafik pada folder yang sama
plt.subplots_adjust( # untuk configure table lewat koding
    left=0.14,bottom=0.14,right=0.95,top=0.88,wspace=0.2,hspace=0.2 
)
plt.show() # tampilkan grafik