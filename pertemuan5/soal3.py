# sandi morse

transformasi=input('Masukkan huruf-huruf yang ingin ditransformasikan: ')
huruf={
    '._':'a',
    '_...':'b',
    '_._.':'c',
    '_..':'d',
    '.':'e',
    '.._.':'f',
    '__.':'g',
    '....':'h',
    '..':'i',
    '.___':'j',
    '_._':'k',
    '._..':'l',
    '__':'m',
    '_.':'n',
    '___':'o',
    '.__.':'p',
    '__._':'q',
    '._.':'r',
    '...':'s',
    '_':'t',
    '.._':'u',
    '..._':'v',
    '.__':'w',
    '_.._':'x',
    '_.__':'y',
    '__..':'z',
    ' ':'',
    '':''
}

if transformasi.count('_')>=1 and transformasi.count('.')>=1:
    kataTrans=transformasi.split('/')
    i=0
    hasil=''
    while i<len(kataTrans):
        kataTrans[i]=kataTrans[i].replace(' ','')
        if huruf.__contains__(kataTrans[i]):
            raw=huruf[kataTrans[i]]
            hasil+=raw
            i+=1
            if i==len(transformasi):
                break
        else:
            print('Input anda salah')
            break
    print(hasil)
elif transformasi.count('_')==0 and transformasi.count('.')==0:
    kataTrans=list(transformasi)
    i=0
    hasil=''
    while i<len(transformasi):
        if huruf.__contains__(list(huruf.keys())[list(huruf.values()).index(kataTrans[i])]):
            hasil+=list(huruf.keys())[list(huruf.values()).index(kataTrans[i])]+' / '
            i+=1
            if i==len(transformasi):
                break
        else:
            print('Input anda salah')
            break
    print(hasil)

#     translate=kataTrans[i]
#         raw=huruf[translate]
#         hasilTrans.extend(raw)
#         i+=1
#     list(huruf.keys())[list(huruf.values()).index(transformasi)]