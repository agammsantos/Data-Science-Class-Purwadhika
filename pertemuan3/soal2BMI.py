# program penghitung BMI by Mustaqiim Agam

berat=input('Masukkan berat badan(kg): ')

i=0
beratBadan='end'
cekBerat=[]
cekBerat.extend(berat)
if cekBerat.count('.')==1 and cekBerat[len(cekBerat)-1]!='.' and cekBerat[0]!='.':
        cekBerat.remove('.')
        if len(cekBerat)==0:
            print('Harap masukkan angka yang sesuai.')
        else:
            while i<len(cekBerat):
                if cekBerat[i].isdigit()==True:
                    i+=1
                    if i==len(cekBerat):
                        print('Berat badan anda adalah: ',berat,'kg')
                        beratBadan=float(berat)
                        break
                else:
                    print('Harap masukkan angka yang sesuai.')
                    break
elif cekBerat.count('.')==0:
    if len(cekBerat)==0:
        print('Harap masukkan angka yang sesuai.')
    else:
        while i<len(cekBerat):
            if cekBerat[i].isdigit()==True:
                i+=1
                if i==len(cekBerat):
                    print('Berat badan anda adalah: ',berat,'kg')
                    beratBadan=float(berat)
                    break
            else:
                print('Harap masukkan angka yang sesuai.')
                break
else:
    print('Harap masukkan angka yang sesuai.')

if beratBadan!='end':
    tinggi=input('Masukkan tinggi badan(meter): ')
    i=0
    cekTinggi=[]
    cekTinggi.extend(tinggi)
    if cekTinggi.count('.')==1 and cekTinggi[len(cekTinggi)-1]!='.' and cekTinggi[0]!='.':
        cekTinggi.remove('.')
        if len(cekTinggi)==0:
            print('Harap masukkan angka yang sesuai.')
        else:
            while i<len(cekTinggi):
                if cekTinggi[i].isdigit()==True:
                    i+=1
                    if i==len(cekTinggi):
                        print('Tinggi badan anda adalah: ',tinggi,'meter')
                        tinggiBadan=float(tinggi)
                        bmi=beratBadan/tinggiBadan**2
                        float(bmi)
                        if bmi<18.5:
                            print('Anda tergolong dalam golongan Underweight.')
                        elif 18.5<=bmi<25:
                            print('Anda tergolong dalam golongan Healthy weight.')
                        elif 25<=bmi<30:
                            print('Anda tergolong dalam golongan Overweight.')
                        else:
                            print('Anda tergolong dalam golongan Obese!')
                        break
                else:
                    print('Harap masukkan angka yang sesuai.')
                    break
    elif cekTinggi.count('.')==0:
        if len(cekTinggi)==0:
            print('Harap masukkan angka yang sesuai.')
        else:
            while i<len(cekTinggi):
                if cekTinggi[i].isdigit()==True:
                    i+=1
                    if i==len(cekTinggi):
                        print('Tinggi badan anda adalah: ',tinggi,'meter')
                        tinggiBadan=float(tinggi)
                        bmi=beratBadan/tinggiBadan**2
                        float(bmi)  
                        if bmi<18.5:
                            print('Anda tergolong dalam golongan Underweight.')
                        elif 18.5<=bmi<25:
                            print('Anda tergolong dalam golongan Healthy weight.')
                        elif 25<=bmi<30:
                            print('Anda tergolong dalam golongan Overweight.')
                        else:
                            print('Anda tergolong dalam golongan Obese!')
                        break
                else:
                    print('Harap masukkan angka yang sesuai.')
                    break
    else:
        print('Harap masukkan angka yang sesuai.')