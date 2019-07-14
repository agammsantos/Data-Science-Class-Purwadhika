# read .txt files => 'r'
# write/overwrite new file => 'w'
# open() => access local file
# append() => menambahkan konten

file = open('test.txt','r')

if file.readable():
    # print(file.read())
    mylist=file.readlines()
    print(mylist[0])
else:
    print('error file tidak terbaca')

file=open('overwrite.txt','w')
file.write('Selamat pagi!')

file=open('test.py','w')
file.write('print(\'Halo!\')') # atau
# file.write("print('Halo!')")

file=open('write.txt','w')
file.write('Print(\'Halo 1!\')\n')
file.write('Print(\'Halo 2!\')\n')

file=open('writetest.txt','w')
file.write('print(\'Halo !!\')\n')
file=open('writetest.txt','w')
file.write('print(\'Halo 2!\')\n')

file=open('append.txt','w')
file.write('print(\'Halo 1!\')\n')
file=open('append.txt','a')
file.write('print(\'Halo 2!\')\n')

ls=['Andi','Budi','Cici']
file=open('nama.txt','w')
for i in range(len(ls)):
    file.write(ls[i]+'\n')
