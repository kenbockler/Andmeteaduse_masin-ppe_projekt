numbrid=0
tähed=0
kasutajanimi= input('Sisesta kasutajanimi: ')
while True:
    parool1=input('Sisesta parool: ')
    parool2=input('Sisesta parool uuesti: ')
    pikkus= len(parool1)
    if parool1 != parool2:
        print('Teine sisestatud parool ei kattu esimesega!')
        continue
    elif pikkus < 8:
        print('Parool peab olema vähemalt 8 tähemärki pikk!')
        continue
    while pikkus> 0:
        for tähemärgid in parool1:
            if tähemärgid.isdigit():
                numbrid+=1
                pikkus-=1
                continue
            elif tähemärgid.isalpha():
                tähed+=1
                pikkus-=1
                continue
            else:
                pikkus-= 1
                continue
            break
        break
    if numbrid== 0 and tähed== 0:
        continue
    if numbrid <1:
        print('Paroolis peab olema lisaks tähtedele ka number!')
        continue
    if tähed <1:
        print('Paroolis peab olema lisaks numbritele ka täht!')
        continue
    else:
        print('Parool sobib!')
        break
pikkus= len(parool1)
parool=''
while pikkus >0:
    parool= parool+ (parool1[pikkus-1])
    pikkus -=1
fail= open('users.txt', 'w')
fail.write(kasutajanimi+':')
fail.write(parool)
fail.close()
