import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

x=np.arange(1,11)
y=np.array([2,3,4,5,4,6,5,7,7,8])
print(x)
print(y)

lenx=len(x)
sumx=np.sum(x)
print(sumx)
sumy=np.sum(y)
print(sumy)
x2=x**2
y2=y**2
xy=x*y
df=pd.DataFrame({
    'x':x,
    'y':y,
    'x^2':x2,
    'y^2':y2,
    'xy':xy
})
print(df)
print(df.sum(axis=0)[0],df.sum(axis=0)[1],df.sum(axis=0)[2],df.sum(axis=0)[3],df.sum(axis=0)[4])

# menentukan slope/gradien dan intercept (dgn sb y) dari hubungan antara data-data x dan y
m=((lenx*np.sum(xy))-(sumx*sumy))/((lenx*np.sum(x2))-sumx**2)
print(m)
c=((sumy*np.sum(x2))-sumx*np.sum(xy))/((lenx*np.sum(x2))-(sumx**2))
print(c)

# menentukan pendekatan linear y / y best fit line untuk plot x dan y
df['yBest']=m*x+c
print(df)
# perlu dicatat bahwa pendekatan ini efektif hanya untuk data yg relatif naik/turun monoton

plt.plot(
    df['x'],df['y'],'g-',
    df['x'],df['yBest'],'r-'
)
plt.grid(True)
plt.show()