kasutajanimi = str(input("Palun sisesta kasutajanimi "))
def onnumbreid(s�ne):
    for i in s�ne:
        if i.isnumeric():
            return True
    return False
def ont�hti(s�ne):
    for i in s�ne:
        if i.isnumeric():
            return True
    return False
while True :
    parool1 = str(input("Palun sisesta parool "))
    parool2 = str(input("Palun sisesta parool teist korda "))
    if parool1 != parool2:
        print("paroolid ei kattu!")
        continue
    if len(parool1) < 8:
        print("parool on l�hem kui 8 t�hem�rki")
        continue
    if onnumbreid(parool1) == False or ont�hti(parool1) == False:
        print("s�nes poe kasutatud nii t�hti kui ka numbreid")
        continue
    break
parool = parool1[::-1]
f = open("users.txt","w")
f.write(kasutajanimi + ":" + parool)
f.close()
