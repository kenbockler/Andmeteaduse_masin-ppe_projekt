fail = open("users.txt", "a")
kasutajaNimi = input("Sisestage oma kasutajanimi: ")
tagurpidi = ""
while True:
    summa = 0
    t�hed= 0
    arvud = 0
    parool1 = input("Sisestage oma parool: ")
    parool2 = input("Sisesatge oma parool uuesti: ")
    if parool2 != parool1:
        print ("Paroolid ei ole samad, proovige uuesti!")
        continue
    for t�htedeArv in parool2:
        summa +=1
        try:
            t�htedeArv = int(t�htedeArv)
        except:
            t�htedeArv = t�htedeArv
        if isinstance(t�htedeArv, int):
            arvud +=1
        if isinstance(t�htedeArv, str):
            t�hed +=1
    if arvud == 0 or t�hed == 0:
        print ("Salas�nas peavad olema nii t�hed kui ka numbrid")
        continue
    if summa < 8:
        print("Parool liiga l�hike, sisestage uus")
        continue
    break
while summa > 0:
    tagurpidi += parool2[summa - 1]
    summa -= 1
fail.write(kasutajaNimi + ":" + tagurpidi + "\n")
fail.close()