import re
kasutajanimi = input("Sisesta kasutajanimi: ")
i = 0
while True:
    parool1 = input("Sisesta parool: ")
    parool2 = input("Sisesta parool teist korda: ")
    if parool1 != parool2:
        print("Paroolid ei �hti!")
    elif len(parool1) < 8:
        print("Sisestatud parool ei ole v�hemalt 8 t�hem�rki pikk!")
    elif not re.search("[a-z]", parool1):
        print("Parool peab sisaldama v�hemalt �hte t�hte!")
    elif not re.search("[0-9]", parool1):
        print("Parool peab sisaldama v�hemalt �hte numbrit!")
    else:
        i = 1
        break
if i == 1:
    tagurpidi = parool1.join(w[::-1] for w in parool1.split())
    f = open("users.txt", "x")
    f.write(kasutajanimi + ":" + tagurpidi)
    f.close()
    