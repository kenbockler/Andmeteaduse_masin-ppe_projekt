kasutajanimi = str(input("Sisestage kasutajanimi: "))
while True:
    parool1 = str(input("Sisestage parool: "))
    parool2 = str(input("Sisestage parool uuesti: "))
    if parool1 != parool2:
        print("Esimene parool ei kattu teise parooliga!")
        continue
    if len(parool1) < 8:
        print("Parool ei sisalda vähemalt 8 tähemärki!")
        continue
    if parool1.isalpha() == True or parool1.isnumeric() == True:
        print("Paroolis ei kasutatud nii tähti kui numbreid!")
        continue
    break
tagurpidi = parool1[::-1]
f = open("users.txt", "w")
f.write(kasutajanimi + ":" + tagurpidi)
f.close()
