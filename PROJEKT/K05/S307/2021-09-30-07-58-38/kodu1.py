K = input("Sisestage kasutajanimi")
P = "parool"
P1 = "parool1"
A = 1
while A == 1:
    P = input("Sisestage parool")
    P1 = input("Sisestage parool uuesti")
    if not P == P1:
        print("Sisestatud paroolid ei ole samad, palun sisestage mõlemad paroolid uuesti")
    elif not len(P1) >= 8:
        print("Parool peab olema vähemalt 8 tähemärki")
    elif any(p.isdigit() for p in P1) == False:
        print("Parool peab sisaldama vähemalt ühte numbrit")
    elif any(p.isalpha() for p in P1) == False:
        print("Parool peab sisaldama tähti")
    else:
        break
P2 = P1[::-1]
PK = K + ":" + P2
fail = open("users.txt", "w")
fail.write(PK)
fail.close()
