k_nimi = input("Kasutajanimi: ")
while True:
    parool = input("Parool: ")
    parool_k = input("Korrake parooli: ")
    if parool != parool_k:
        print("Teie paroolid ei kattu, palun proovige uuesti.")
        continue
    if not len(parool) >= 8:
        print("Teie parool peab olema vähemalt 8 tähemärki pikk.")
        continue
    number = 0
    täht = 0
    for i in parool:
        if i.isnumeric():
            number += 1
        if i.isalpha():
            täht += 1
    if not (täht > 0 and number > 0):
        print("Teie parool peab sisaldama nii tähti kui ka nubmreid.")
        continue
    else:
        break
krüpto_parool = parool[::-1]
f = open("users.txt", "w+")
f.write(k_nimi +":")
f.write(krüpto_parool)
f.close()    
