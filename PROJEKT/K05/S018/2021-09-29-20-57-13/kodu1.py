k = str(input("Kasutajanimi: "))
while True:
    p1 = str(input("Parool esimest korda: "))
    p2 = str(input("Pareool teist korda: "))
    if p1 == p2:
        if len(p1) >= 8:
            if p1.isalpha() == False and p1.isnumeric() == False:
                break
            else:
                print("Sisestatud parool peab sisaldama nii t�hti kui numbreid")
                continue
        else:
            print("Sisestatud parool peab sisaldama v�hemalt kaheksat s�mbolit")
            continue
    else:
        print("Sisestatud paroolid ei olnud samad")
        continue
kr�pt = ""
i = len(p1)
while i > 0:
    kr�pt += p1[i - 1]
    i -= 1
f = open("users.txt", "a")
f.write(k)
f.write(":")
f.write(kr�pt)
f.close()