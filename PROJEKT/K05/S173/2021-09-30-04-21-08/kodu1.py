import re
file = open("users.txt", "w")
nimi = input("Sisesta kasutajanimi:")
krüpt = ""
while True:
    parool1 = input("Sisesta parool:")
    parool2 = input("Sisesta parool uuesti:")
    if parool1 != parool2:
        continue
    if len(parool1)<8:
        continue
    if re.search("[a-z]", parool1.lower()):
        if re.search("[0-9]", parool1):
            break
for i in parool1:
    krüpt = i + krüpt
file.write(nimi + ":" + krüpt)
file.close()