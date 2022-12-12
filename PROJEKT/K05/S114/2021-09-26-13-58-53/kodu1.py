kasutajanimi = input("Sisesta kasutajanimi: ")
ParooliPikkus = 0
i = 0
numbritearv = 0
tahtedearv = 0
while i < 1:
    while True:
        parool1 = input("Sisesta esimest korda parool: ")
        parool2 = input("Sisesta teist korda parool: ")
        if parool1 != parool2:
           print("Paroolid ei klapi omavahel! Sisesta korrektne teine parool!")
           break
        for taht in parool1:
            ParooliPikkus += 1
            if taht.isdigit():
                numbritearv += 1
            elif taht.isalpha():
                tahtedearv += 1
        if ParooliPikkus < 8:
            print("Parool on lühem kui 8 tähemärki!")
            break
        elif numbritearv == 0 or tahtedearv == 0:
            print("Paroolis pole kasutatud numbreid ega ka tähti!")
            break
        parool1 = parool1 [::-1]
        f = open("users.txt","a")
        f.write(kasutajanimi+":"+parool1+"\n")
        f.close()
        i +=1
        break
