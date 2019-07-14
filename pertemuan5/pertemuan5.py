# nested for loop

listku=[
    ['a','b','c'],
    ['d','e','f'],
    ['g','h','i']
]

for baris in listku:
    for elemen in baris:
        print(elemen)

data=[
    [
        ['Andi','Budi','Caca'],
        ['Deni','Euis','Fafa'],
        ['Gigi','Hani','Inne']
    ],
    [
        ['Janu','Koko','Lani'],
        ['Momo','Nina','Opik'],
        ['Peni','Qiqi','Rogi']
    ]
]

for baris in data:
    for anggota in baris:
        for elemen in anggota:
            print(elemen)