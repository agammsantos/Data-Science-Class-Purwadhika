# lambda function: single return function

def x(a):
    return a

y=lambda a:a*2

print(x(23))
print(y(24))

def z(a,b,c):
    return a+b+c

a=lambda a,b,c:a+b+c

print(z(2,3,4))
print(a(2,3,4))

def kali(n):
    return lambda x:x*n

kaliDua=kali(2)
kaliTiga=kali(3)

print(kaliDua(26))
print(kaliTiga(33))

# =======================================================
def y(a):
    
    return a
def x(a):
    print(y(a))
x(12)

def z():
    return lambda c:c
b=z()
print(b(13))
# ========================================================

