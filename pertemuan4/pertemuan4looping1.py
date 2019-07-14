# looping 1

'''
while condition:
    argument
'''

angka=1
while angka<=10:
    print('Haha ke-',angka)
    angka+=1

angka=[11,22,23,24,25,26,27]
angka2=[]
i=0
while i<=len(angka)-1:
    print(angka[i]*2)
    angka2.append(angka[i]*2)
    i+=1
print(angka2)

i=0
while i<=6:
    if i==4:
        i+=1
        continue
    print(i)
    i+=1
i=0
while i<=6:
    if i==4:
        i+=1
        break
    print(i)
    i+=1