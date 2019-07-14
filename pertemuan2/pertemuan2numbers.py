x = 12.0
y = 3

print(x+y)
print(x-y)
print(x*y)
print(x/y)
print(12**2)
print(pow(12,2))
print(abs(-1234))
print((144))
print(8**(1/3))
print(pow(8,1/3))

# special case
a=0.1
b=0.2
c=.1
print(a+b) # kesalahan karena float 0.1 direpresentasikan dengan binary code yang tidak presisi
print((a*10+b*10)/10) # salah satu cara menangani kasus ini, dengan mengubah float kedalam int terlebih dahulu

x=3.24689
y=4.99872
print(round(x))
print(round(y))
print(round(x,2)) # pembulatan 2 angka dibelakang koma
print(round(y,2)) 