nimi = input("sisesta kasutajanimi ")
def checkString(sone):
    isAlpha = 0
    isDigit = 0
    for char in sone:
        if char.isalpha():
            isAlpha = True
        if char.isdigit():
            isDigit = True
    if isAlpha and isDigit:
        return True
    else:
        return False
while True:
    parool = str(input("sisesta parool "))
    parool2 = str(input("sisesta parool uuesti "))
    if parool == parool2:
        if len(parool) >= 8:
            if checkString(parool):
                parool = parool[::-1]
                break
            else:
                print("parool peab sisaldama tähti ja numbreid")
                continue
        else:
            print("parool peab olema vähemalt 8 tähemärki pikk")
            continue
    else:
        print("paroolid peavad samasugused olema")
        continue
f = open("users.txt", "a")
f.write("\n" + nimi + ":" + parool)
f.close()
