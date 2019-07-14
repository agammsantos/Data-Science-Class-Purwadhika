import matplotlib.pyplot as plt
import numpy as np
import csv

x=[]
y=[]
with open('data.csv','r') as dataku: # membuka file csv dengan library csv
    data=csv.reader(dataku)
    print(data)
    for i in data:
        print(i)
        x.append(int(i[0]))
        y.append(int(i[1]))


# x,y=np.loadtxt( # membuka file tipe2 mark-up dengan library numpy
#     'data.csv',
#     delimiter=',',
#     unpack=True
# )

print(x)
print(y)

plt.plot(x,y)
plt.show()