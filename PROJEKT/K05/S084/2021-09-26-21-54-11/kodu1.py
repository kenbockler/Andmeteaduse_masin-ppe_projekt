def kas_numbreid(text):
    numbreid = False
    for char in text:
        if char.isdigit():
            numbreid = True
    return numbreid
def kas_tähti(text):
    tähti = False
    for char in text:
        if char.isalpha():
            tähti = True
    return tähti
nimi = input("Kasutajanimi: ")
while True:
    parool = input("Parool: ")
    parool2 = input("Parool: ")
    if parool != parool2:
        print("Sisestatud paroolid on erinevad.")
        continue
    elif len(parool) < 8:
        print("Parool peab olema vähemalt 8 tähemärki.")
        continue
    elif not kas_numbreid(parool) or not kas_tähti(parool):
        print("Parool peab sisaldama tähti ja numbreid.")
        continue
    break
parool = parool[::-1]
with open("users.txt","w") as file:
    file.write(nimi+":"+parool)