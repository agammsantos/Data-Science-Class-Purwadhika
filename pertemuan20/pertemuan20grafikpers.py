import matplotlib.pyplot as plt
import numpy as np

# 3*x+2y=12
x=np.array([0,1,2,3,4,5,6,7,8,9])
y=np.arange(10).astype(float) # elemen2 entry dirubah kedalam float agar dapat diassign jg oleh float
for i in x:
    y[i]=(12/2)-(3*i/2)
    print(y[i])

plt.plot(x,y,'-*')
plt.show()