import re
nimi = str(input("Sisestage kasutaja nimi:"))
while True:
    parool1 = str(input("Seatke kontole parool:"))
    parool2 = str(input("Seatke konto parool uuesti:"))
    if parool1 == parool2:
        if len(parool1) >= 8:
            kontroll_2 = re.sub(r'[^\w\s]','',parool1)
            kontroll = bool(re.match('^(?=.*[0-9]$)(?=.*[a-zA-Z])', kontroll_2))
            if kontroll == True :
                parool1 = parool1[::-1]
                f = open("users.txt","w+")
                f.write(nimi + ":" + parool1)
                f.close()
                break
            else:
                print("paroolis pole kasutatud vähemalt ühte tähte ja ühte numbrit")
                continue
        else:
            print("parool pole piisavalt pikk")
            continue
    else:
        print("Paroolid ei kattu, vigane parool")
        continue
