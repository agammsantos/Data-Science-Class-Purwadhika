# looping 2

kata = 'Andilala'
for x in kata:
    print(x)
    
angka=[0,1,2,3,4,5,6,7,8,9]
for y in angka:
    print(y)

for data in range(9):
    print('Haha ke-',data)

for data in range(3,10):
    print('Haha ke-',data)

for x in angka:
    print(x)

for i in range(len(angka)):
    print(angka[i])

star=''
for i in range(5):
    star='*'*(len(range(5))-i) # star sebagai string
    print(star)

angka=''
for i in range(5):
    angka=angka+str(i)+' '
    print(angka)

for i in range(5):
    for j in range(5):
        print(i,'dan',j)

# soal 1
i=0
password='12345'
login=input('Masukkan password: ')
while i<3:
    if login==password:
        print('password benar!')
        break
    login=input('Harap memasukkan password dengan benar: ')
    if i==2:
        print('Akun anda diblokir')
        break
    i+=1
