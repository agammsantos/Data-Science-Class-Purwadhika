# {a,b,c} set = no indexing

# data={1,2,3}
# print(data)
# print(type(data))

# dataSet={1,2,3}
# dataList=[1,2,3]
# dataTuple=(1,2,3)

# print(2 in dataSet)
# print(2 in dataList)
# print(2 in dataTuple)
# print(dataTuple[0:2:1])
# print(dataTuple + dataTuple)
# print(dataTuple * 3)

dataS={'Andi','Budi','Caca'}

for elemen in dataS:
    print(elemen)

dataS.add('Deni') # add: hanyalah penambahan elemen non-list
dataS.update(['Euis','Fafa']) # update: menambahkan elemen-elemen ke set
dataS.update({'Gigi','Hani'})
dataS.remove('Fafa') # remove: menghapus suatu elemen dengan syarat elemen harus ada
dataS.discard('Asd') # discard: menghapus suatu elemen
# dataS.remove('Zizi')
# dataS.discard('Zizi')
# dataS.clear() # clear: mengosongkan set
print(dataS)

# del dataS # del: menghapus set beserta definisinya
# print(dataS)