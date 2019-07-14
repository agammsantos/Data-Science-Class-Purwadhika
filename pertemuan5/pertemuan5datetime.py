import datetime

x=datetime.datetime.now()

print(x.year)           # tahun
print(x.strftime('%m'))   # bulan index
print(x.strftime('%B'))   # bulan nama eng
print(x.strftime('%A'))   # hari eng
print(x.strftime('%d'))   # tanggal
print(x.strftime('%H'))   # jam 24h
print(x.strftime('%I'))   # jam 12h
print(x.strftime('%M'))   # menit
print(x.strftime('%S'))   # detik
print(x.strftime('%c'))   # ringkasan
print(x.strftime('%x'))   # bagian pertama tanggalan
print(x.strftime('%X'))   # bagian kedua tanggalan

from datetime import datetime
x='12/12/2019'
y='12 Apr 2019'
z='12-04-19 21.45'
a='Friday, 12 April 2019'
b="Jum'at, 12 April 2019"

if b.count("Jum'at")==1:
    c=b.replace("Jum'at","Friday")

ubahStrxkeDate=datetime.strptime(x,'%d/%m/%Y') # mengubah tanggalan kpd tanggal yang diinginkan
ubahStrykeDate=datetime.strptime(y,'%d %b %Y')
ubahStrzkeDate=datetime.strptime(z,'%d-%m-%y %H.%M')
ubahStrakeDate=datetime.strptime(a,'%A, %d %B %Y')
ubahStrbkeDate=datetime.strptime(c,'%A, %d %B %Y')

print(ubahStrxkeDate)
print(ubahStrykeDate)
print(ubahStrzkeDate)
print(ubahStrakeDate)
print(type(ubahStrakeDate))
print(ubahStrakeDate.strftime('%A'))
print(ubahStrbkeDate)
print(type(ubahStrbkeDate))
print(ubahStrbkeDate.strftime('%A'))

tgl=datetime.now()
if tgl.strftime('%A')=='Saturday'or'Friday'or'Sunday'or'Monday'or'Tuesday'or'Wednesday'or'Thursday':
    d=tgl.strftime('%A').replace("Saturday","Sabtu")
    d=tgl.strftime('%A').replace("Sunday","Minggu")
    d=tgl.strftime('%A').replace("Monday","Senin")
    d=tgl.strftime('%A').replace("Tuesday","Selasa")
    d=tgl.strftime('%A').replace("Wednesday","Rabu")
    d=tgl.strftime('%A').replace("Thursday","Kamis")
    d=tgl.strftime('%A').replace("Friday","Jum'at")

print(d)


