file=open('master.csv','r',encoding='utf-8-sig') # encoding untuk mengatur format data agar tidak ada embel2
print(file.readable())
print(file.read())

import csv
myData=[]

with open('master.csv','r',encoding='utf-8-sig') as fileku:
    baca=csv.DictReader(fileku,delimiter=',')
    # print(baca)
    for i in baca:
        # print(i)
        print(dict(i))  # mengoutput per line sebagai dictionary
        myData.append(dict(i))  # mengoutput dictionary sbg list

print(myData)