# library: math (built-in)

import math

print(math.pi)
print(math.sqrt(16))
print(math.floor(2.98))
print(math.ceil(5.21))
print(math.factorial(5))
print(1%2) # modulo

x=12
x+=1 # x=x+1
print(x)
x-=1 # x=x-1
print(x)
x*=2 # x=x*2
print(x)
x/=2 # x=x/2
print(x)

# penyelesaian aljabar
# diketahui total usia andi dan budi yakni 49, 
# lalu perbandingan usia antara andi dan budi adalah 4/10
# berapa usia andi dan budi?

total=49
rasio=0.4

budi=total/(1+rasio)
andi=total-budi

print('Usia budi adalah',budi,'dan usia andi adalah',andi)