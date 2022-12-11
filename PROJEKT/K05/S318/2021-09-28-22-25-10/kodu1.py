k_nimi=input("Sisesta kasutajanimi: ")
try:
    while True:
        paro=input("Sisesta parool: ")
        paro2=input("Sisesta taas parool: ")
        if paro == paro2 and paro.isalnum == True and len(paro) >= 8:
            break
        else:
            if paro != paro2:
                print("Paroolid ei ole samad.")
                if len(paro) < 8:
                    print("Parool pole vähemalt 8.")
                    if paro.isalnum() != True:
                        print("Ei sisalda.")
            else:
                break
except:
    raise ValueError()
taga=paro[::-1]
print(taga)
f=open("users.txt", "w")
f.write(str(k_nimi)+ ":"+str(taga))
f.close()