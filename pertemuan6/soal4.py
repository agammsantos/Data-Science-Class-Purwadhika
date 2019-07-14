# mengubah file csv dalam string ke dalam bentuk dictionary tanpa dictreader
import csv
import json
myData=[]

with open('master.csv','r',encoding='utf-8-sig') as fileku:
    baca=csv.reader(fileku,delimiter=',')
    for i in baca:
        myData.append(i)

myDict='['
i=0
while i<len(myData)-1:
    if i<len(myData)-2:
        myDict+='{\"'+str(myData[0][0])+'\":'+str(myData[i+1][0])+','+'\"'+str(myData[0][1])+'\":\"'+str(myData[i+1][1])+'\",'+'\"'+str(myData[0][2])+'\":'+str(myData[i+1][2])+'},'
        i+=1
    else:
        myDict+='{\"'+str(myData[0][0])+'\":'+str(myData[i+1][0])+','+'\"'+str(myData[0][1])+'\":\"'+str(myData[i+1][1])+'\",'+'\"'+str(myData[0][2])+'\":'+str(myData[i+1][2])+'}]'
        i+=1

print(myDict)
realDict=json.loads(myDict)
print(realDict)
print(type(realDict))
print(realDict[1]['umur'])
print(type(realDict[1]['umur']))

# mengubah file csv ke dalam file json
myData=[]
namaFile=input('Masukkan nama file yang ingin diconvert dalam folder ini: ')
with open(namaFile+'.csv','r',encoding='utf-8-sig') as filecsv:
    bacacsv=csv.reader(filecsv,delimiter=',')
    for i in bacacsv:
        myData.append(i)

mycsv='['
i=0
while i<len(myData)-1:
    if i<len(myData)-2:
        mycsv+='{\"'+str(myData[0][0])+'\":'+str(myData[i+1][0])+','+'\"'+str(myData[0][1])+'\":\"'+str(myData[i+1][1])+'\",'+'\"'+str(myData[0][2])+'\":'+str(myData[i+1][2])+'},'
        i+=1
    else:
        mycsv+='{\"'+str(myData[0][0])+'\":'+str(myData[i+1][0])+','+'\"'+str(myData[0][1])+'\":\"'+str(myData[i+1][1])+'\",'+'\"'+str(myData[0][2])+'\":'+str(myData[i+1][2])+'}]'
        i+=1

namaOutput=input('Masukkan nama file json yang ingin dibuat: ')
# filejson=json.loads(mycsv)
jsonku=open(namaOutput+'.json','w')
jsonku.write(mycsv)