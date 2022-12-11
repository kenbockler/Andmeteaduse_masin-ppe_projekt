a = input("Sisesta kasutajanimi: ")
while True: 
    b = input("Sisesta parool esimest korda: ")
    c = input("Sisesta parool teist korda: ")
    def niinumberkuitaht(b):
        num = False
        tht = False
        for i in b:
            if i.isnumeric():
                num = True
            elif i.isalpha():
                tht = True
            if num == True and tht == True:
                return True
        return False
    if b == c and len(b) >= 8 and niinumberkuitaht(b):
        print(b[::-1])
        break
    else:
        print("Sisestage vähemalt kaheksa tähemärgiga parool, milles on nii number kui ka täht")
f = open("users.txt", "w")
f.write(a + ":" + b[::-1])
f.close()
    