import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import axes3d # untuk grafik 3d

x=np.array([1,2,3,4,5])
y=np.array([2,4,6,8,10])
z=np.array([[1,3,5,7,9]])

plt.figure('Test 3D plot')
myplot=plt.subplot(111,projection='3d') # memproyeksikan plot 3d
myplot.plot_wireframe(x,y,z) # menentukan sumbu pada plot 3d
myplot.scatter(x,y,z,color='y',marker='*',s=200) # membuat diagram scatter 3d
myplot.set_xlabel('Nilai x')
myplot.set_ylabel('Nilai y')
myplot.set_zlabel('Nilai z')

z1=np.zeros(5) # array of five 0
x1=np.ones(5) # array of five 1
y1=np.ones(5)
z=np.array([1,3,5,7,9])

plt.figure('Tes 3D bar')
myplot=plt.subplot(111,projection='3d')
myplot.bar3d(x,y,z1,x1,y1,z, color=['black','pink','black','pink','black']) # formatnya adalah (nilai-x, nilai-y, titik dasar z, lebar x-bar, lebar y-bar, tinggi y-bar, color)

# myplot.set_xticks([1,2,3,4,5])
# myplot.set_xlim3d(right=5)

myplot.set_xlabel('Nilai x')
myplot.set_ylabel('Nilai y')
myplot.set_zlabel('Nilai z')
# myplot.set_title('Halo')
myplot.set_title(label='Tes 3D bar', loc='left')

plt.show()