kasutajanimi = input(str("Palun sisestage kasutajanimi: "))
parool1 = input("Palun sisestage parool: ")
parool2 = input("Palun sisestage parool teist korda: ")
while parool1 != parool2:
    print("Sisestatud paroolid ei kattu!")
    parool1 = input("Palun sisestage parool: ")
    parool2 = input("Palun sisestage parool teist korda: ")
while len(parool1) <= 8:
    print("Parool peab olema v�hemalt 8 t�hem�rki pikk!")
    parool1 = input("Palun sisestage parool: ")
    parool2 = input("Palun sisestage parool teist korda: ")
while parool1.isalpha() or parool1.isnumeric():
    print("Parool peab sisaldama numbreid ja t�hti!")
    parool1 = input("Palun sisestage parool: ")
    parool2 = input("Palun sisestage parool teist korda: ")
kr�pteeritud = str(parool1[::-1])
sihtf = open("users.txt", "w")
sihtf.write(kasutajanimi + ":" + kr�pteeritud)
sihtf.close()
       