n= 1
f= open('kinganumbrid.txt')
while n==1:
    try:
        faili_sisu = f.readline()
        pikkus= round(2/3 *(float(faili_sisu)- 2))
        print(str(pikkus))
    except:
        if faili_sisu== '':
           break
        else:
            print('Vigane sisend')
            n+= 1
    while n==2:
        try:
            faili_sisu = f.readline()
            pikkus= round(2/3 *(float(faili_sisu)- 2))
            print(str(pikkus))
        except:
            if faili_sisu== '':
               break
            else:    
                print('Vigane sisend')
                n-= 1
