# Kalkulator v1.r by Mustaqiim Agam

angkapertama=input('Input angka pertama: ')
angka1='asd'
cek1=[]
cek1.extend(angkapertama)
i=0
if cek1[0]=='-' or cek1[0]=='+':
    cek1.pop(0)
    if cek1.count('.')==1 and cek1[len(cek1)-1]!='.' and cek1[0]!='.':
        cek1.remove('.')
        if len(cek1)==0:
            print('Input bukan angka')
        else:
            while i<len(cek1):
                if cek1[i].isdigit()==True:
                    i+=1
                    if i==len(cek1):
                        print('Angka pertama adalah',angkapertama)
                        angka1=float(angkapertama)
                        break
                elif cek1[i]=='/':
                    i+=1
                    if i==len(cek1):
                        print('Input bukan bilangan')
                        break
                    else:
                        while i<len(cek1):
                            if cek1[i].isdigit()==True:
                                i+=1
                                if i==len(cek1):
                                    print('Harap input bentuk desimalnya.')
                                    break
                            else:
                                print('Input bukan bilangan')
                                break
                else:
                    print('Input bukan bilangan')
                    break  
    elif cek1.count('.')>1:
        print('Input tidak valid')
    elif cek1.count('.')==0:
        if len(cek1)==0:
            print('Input bukan angka')
        else:
            while i<len(cek1):
                if cek1[i].isdigit()==True:
                    i+=1
                    if i==len(cek1):
                        print('Angka pertama adalah',angkapertama)
                        angka1=float(angkapertama)
                        break
                elif cek1[i]=='/':
                    i+=1
                    if i==len(cek1):
                        print('Input bukan bilangan')
                        break
                    else:
                        while i<len(cek1):
                            if cek1[i].isdigit()==True:
                                i+=1
                                if i==len(cek1):
                                    print('Harap input bentuk desimalnya.')
                                    break
                            else:
                                print('Input bukan bilangan')
                                break
                else:
                    print('Input bukan bilangan')
                    break    
    else:
        print('Input tidak valid')
        
elif cek1.count('.')==1 and cek1[len(cek1)-1]!='.' and cek1[0]!='.':
    cek1.remove('.')
    if len(cek1)==0:
        print('Input bukan angka')
    else:
        while i<len(cek1):
            if cek1[i].isdigit()==True:
                i+=1
                if i==len(cek1):
                    print('Angka pertama adalah',angkapertama)
                    angka1=float(angkapertama)
                    break
            elif cek1[i]=='/':
                    i+=1
                    if i==len(cek1):
                        print('Input bukan bilangan')
                        break
                    else:
                        while i<len(cek1):
                            if cek1[i].isdigit()==True:
                                i+=1
                                if i==len(cek1):
                                    print('Harap input bentuk desimalnya.')
                                    break
                            else:
                                print('Input bukan bilangan')
                                break
            else:
                print('Input bukan bilangan')
                break                        
elif cek1.count('.')>1:
    print('Input tidak valid')
elif cek1.count('.')==0:
    if len(cek1)==0:
        print('Input bukan angka')
    else:
        while i<len(cek1):
            if cek1[i].isdigit()==True:
                i+=1
                if i==len(cek1):
                    print('Angka pertama adalah',angkapertama)
                    angka1=float(angkapertama)
                    break
            elif cek1[i]=='/':
                    i+=1
                    if i==len(cek1):
                        print('Input bukan bilangan')
                        break
                    else:
                        while i<len(cek1):
                            if cek1[i].isdigit()==True:
                                i+=1
                                if i==len(cek1):
                                    print('Harap input bentuk desimalnya.')
                                    break
                            else:
                                print('Input bukan bilangan')
                                break
            else:
                print('Input bukan bilangan')
                break    
else:
    print('Input tidak valid')

angka2='asd'
if angka1!='asd':
    operator=input('Input operator: ')
    if operator=='+' or operator=='-' or operator=='/' or operator=='*' or operator=='x' or operator=='**' or operator=='^' or operator=='//' or operator=='%':
        angkakedua=input('Input angka kedua: ')
        cek2=[]
        cek2.extend(angkakedua)
        i=0
        if cek2[0]=='-' or cek2[0]=='+':
            cek2.pop(0)
            if cek2.count('.')==1 and cek2[len(cek2)-1]!='.' and cek2[0]!='.':
                cek2.remove('.')
                if len(cek2)==0:
                    print('Input bukan angka')
                else:
                    while i<len(cek2):
                        if cek2[i].isdigit()==True:
                            i+=1
                            if i==len(cek2):
                                print('Angka kedua adalah',angkakedua)
                                angka2=float(angkakedua)
                                if operator=='+':
                                    print('Hasil operasi adalah:',angka1+angka2)
                                elif operator=='-':
                                    print('Hasil operasi adalah',angka1-angka2)
                                elif operator=='*' or operator=='x':
                                    print('Hasil operasi adalah',angka1*angka2)
                                elif operator=='/':
                                    print('Hasil operasi adalah',angka1/angka2)
                                elif operator=='**' or operator=='^':
                                    print('Hasil operasi adalah',angka1**angka2)
                                elif operator=='//':
                                    print('Hasil operasi adalah',angka1//angka2)
                                elif operator=='%':
                                    print('Hasil operasi adalah',angka1%angka2)

                                break
                        elif cek2[i]=='/':
                            i+=1
                            if i==len(cek2):
                                print('Input bukan bilangan')
                                break
                            else:
                                while i<len(cek2):
                                    if cek2[i].isdigit()==True:
                                        i+=1
                                        if i==len(cek2):
                                            print('Harap input bentuk desimalnya.')
                                            break
                                    else:
                                        print('Input bukan bilangan')
                                        break
                        else:
                            print('Input bukan bilangan')
                            break   
            elif cek2.count('.')>1:
                print('Input tidak valid')
            elif cek2.count('.')==0:
                if len(cek2)==0:
                    print('Input bukan angka')
                else:
                    while i<len(cek2):
                        if cek2[i].isdigit()==True:
                            i+=1
                            if i==len(cek2):
                                print('Angka kedua adalah',angkakedua)
                                angka2=float(angkakedua)
                                if operator=='+':
                                    print('Hasil operasi adalah:',angka1+angka2)
                                elif operator=='-':
                                    print('Hasil operasi adalah',angka1-angka2)
                                elif operator=='*' or operator=='x':
                                    print('Hasil operasi adalah',angka1*angka2)
                                elif operator=='/':
                                    print('Hasil operasi adalah',angka1/angka2)
                                elif operator=='**' or operator=='^':
                                    print('Hasil operasi adalah',angka1**angka2)
                                elif operator=='//':
                                    print('Hasil operasi adalah',angka1//angka2)
                                elif operator=='%':
                                    print('Hasil operasi adalah',angka1%angka2)

                                break
                        elif cek2[i]=='/':
                            i+=1
                            if i==len(cek2):
                                print('Input bukan bilangan')
                                break
                            else:
                                while i<len(cek2):
                                    if cek2[i].isdigit()==True:
                                        i+=1
                                        if i==len(cek2):
                                            print('Harap input bentuk desimalnya.')
                                            break
                                    else:
                                        print('Input bukan bilangan')
                                        break
                        else:
                            print('Input bukan bilangan')
                            break
            else:
                print('Input tidak valid')
                
        elif cek2.count('.')==1 and cek2[len(cek2)-1]!='.' and cek2[0]!='.':
            cek2.remove('.')
            if len(cek2)==0:
                print('Input bukan angka')
            else:
                while i<len(cek2):
                    if cek2[i].isdigit()==True:
                        i+=1
                        if i==len(cek2):
                            print('Angka kedua adalah',angkakedua)
                            angka2=float(angkakedua)
                            if operator=='+':
                                print('Hasil operasi adalah:',angka1+angka2)
                            elif operator=='-':
                                print('Hasil operasi adalah',angka1-angka2)
                            elif operator=='*' or operator=='x':
                                print('Hasil operasi adalah',angka1*angka2)
                            elif operator=='/':
                                print('Hasil operasi adalah',angka1/angka2)
                            elif operator=='**' or operator=='^':
                                print('Hasil operasi adalah',angka1**angka2)
                            elif operator=='//':
                                print('Hasil operasi adalah',angka1//angka2)
                            elif operator=='%':
                                print('Hasil operasi adalah',angka1%angka2)

                            break
                    elif cek2[i]=='/':
                        i+=1
                        if i==len(cek2):
                            print('Input bukan bilangan')
                            break
                        else:
                            while i<len(cek2):
                                if cek2[i].isdigit()==True:
                                    i+=1
                                    if i==len(cek2):
                                        print('Harap input bentuk desimalnya.')
                                        break
                                else:
                                    print('Input bukan bilangan')
                                    break
                    else:
                        print('Input bukan bilangan')
                        break
        elif cek2.count('.')>1:
            print('Input tidak valid')
        elif cek2.count('.')==0:
            if len(cek2)==0:
                print('Input bukan angka')
            else:
                while i<len(cek2):
                    if cek2[i].isdigit()==True:
                        i+=1
                        if i==len(cek2):
                            print('Angka kedua adalah',angkakedua)
                            angka2=float(angkakedua)
                            if operator=='+':
                                print('Hasil operasi adalah:',angka1+angka2)
                            elif operator=='-':
                                print('Hasil operasi adalah',angka1-angka2)
                            elif operator=='*' or operator=='x':
                                print('Hasil operasi adalah',angka1*angka2)
                            elif operator=='/':
                                print('Hasil operasi adalah',angka1/angka2)
                            elif operator=='**' or operator=='^':
                                print('Hasil operasi adalah',angka1**angka2)
                            elif operator=='//':
                                print('Hasil operasi adalah',angka1//angka2)
                            elif operator=='%':
                                print('Hasil operasi adalah',angka1%angka2)

                            break
                    elif cek2[i]=='/':
                        i+=1
                        if i==len(cek2):
                            print('Input bukan bilangan')
                            break
                        else:
                            while i<len(cek2):
                                if cek2[i].isdigit()==True:
                                    i+=1
                                    if i==len(cek2):
                                        print('Harap input bentuk desimalnya.')
                                        break
                                else:
                                    print('Input bukan bilangan')
                                    break
                    else:
                        print('Input bukan bilangan')
                        break
        else:
            print('Input tidak valid')

    else:
        print('Operator tidak terdefinisi')
        print('Harap masukkan operator yang sesuai.')
else:
    print('Harap masukkan angka yang sesuai.')

if angka2=='asd':
    print('Harap masukkan angka yang sesuai.')

# if angkapertama.isdigit() and angkakedua.isdigit():
#     if operator==+ and operator==- and operator==/ and operator==* and operator==x and operator==** and operator==// and operator==%:
