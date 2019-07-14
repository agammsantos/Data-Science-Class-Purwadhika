# tuple = immutable

angkaList=[11,12,13,14,15,16]
angkaTuple=(1,2,3,4,5,6)

angkaList[0]=1234
print(angkaList)

# angkaTuple[0]=1234 error, tuple tidak dapat dimodifikasi
# print(angkaTuple)

angkaList=[
    (1,2),
    (3,4)
]
angkaTuple=(
    ['a','b'],
    ['c','d']
)

print(angkaList[0][1])
print(angkaTuple[1][1])

angkaTuple=(
    ['a','b',(3,9)],
    ['c','d']
)

angkaTuple[0][1]='Andi' # bisa diubah karena elemen berada di dalam list yang berada di dalam tuple
print(angkaTuple)
# angkaTuple[0][2][0]='Andi' error karena elemen berupa tuple
# print(angkaTuple)
