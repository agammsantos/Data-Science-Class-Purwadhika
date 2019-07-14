# pip install beautifulsoup4

from bs4 import BeautifulSoup

# mengambil dari text html
# web='<p>Halo gaes</p>'
# x=BeautifulSoup(web,'html.parser') # menginisiasi web scrapping dengan parsing method html.parser

# # mengambil dari file html
# web=open('tes.htm','r')
# x=BeautifulSoup(web,'html.parser')

# print(x.prettify())

# print(x.title)
# print(x.title.name)
# print(x.title.text)
# print(type(x.title.text))
# print(x.title.string)
# print(type(x.title.string))

# print(x.p)
# print(x.p.name)
# print(x.p.string)
# print(x.p.text)

# for i in x.find_all("p"): # mencari semua data yang ada di class atau id p1
#     print(i)

# for i in x.find_all('li'):
#     print(i)

# for i in x.find(id='p1'): # mecari konten berdasarkan class atau id tertentu, kalau tidak ditemukan akan menjadi NoneType
#     print(i)

# for i in x.find(class_='p2'): # menggunakan class_ karena class sudah reserved di python (sudah ada)
#     print(i)

# for i in x.find_all(class_='p2'): # mencari seluruh class p2 lalu mengoutput text yang ada didalam
#     print(i.text)

# data=x.ol
# for i in data.find_all('li'): # mencari seluruh data yang ada di li pada tag ol
#     print(i.text)


# mengambil dari website wiki dari dalam tabel
import requests
x=requests.get('https://en.wikipedia.org/wiki/List_of_Power_Rangers_episodes')
y=BeautifulSoup(x.content,'html.parser')
i=0
j=0
table=y.find(class_='wikitable')
alldata=table.find_all('tr')
alltd=[]
while i<len(alldata):
    alltd.extend(alldata[i].find_all('td'))
    data=[]
    while j<len(alltd):
        if str(alltd[j].i)!='None':
            if 'Rangers' in str(alltd[j].i.text):
                judul=alltd[j].i.text
                print(judul)
                if i<len(alldata)-1:
                    if i!=30:
                        print(alltd[j+2].span.text)
                        print(alltd[j+3].span.text)
                    else:
                        print(alltd[j+2].span.text)
                        print(alltd[j+3].text)
                        
            #     print(judul)
            # print(alltd[j].find(class_='bday dtstart published updated'))
            if str(alltd[j].find(class_='bday dtstart published updated'))!='None':
                judulstart=judul+' '+str(alltd[j].find(class_='bday dtstart published updated').text)
                print(alltd[j].find(class_='bday dtstart published updated'))
            if str(alltd[j].find(class_='dtend'))!='None':
                judulstartend=judulstart+' '+str(alltd[j].find(class_='dtend').text)
            # data.append(judulstartend)
        j+=1
    i+=1

# menampilkan seluruh nama power rangers melalui text dalam wiki
# for i in y.find_all('span',class_='mw-headline'):
#     if str(i.i)!='None':
#         print(i.i.text)

# print(x.prettify())