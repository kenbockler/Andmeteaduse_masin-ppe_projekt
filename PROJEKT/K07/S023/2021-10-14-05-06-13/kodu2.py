a = input("Sisestage teepikkus  kilomeetrites")
def takso(a):
    kogulist = []
    algus = []
    kilomeeter = []
    fail  = open("taksohinnad.txt", encoding = "utf8")
    for i in fail:
        i = i.strip().split(",")
        algus.append(i[1])
        kilomeeter.append(i[2])
        print(algus)
        print(kilomeeter)
    maksitaksi = float(float(algus[0]) + float(kilomeeter[0])* a)
    s�ps = float(float(algus[1]) + float(kilomeeter[1])* a)
    waldo = float(float(algus[2]) + float(kilomeeter[2])* a)
    if maksitaksi < s�ps and maksitaksi < waldo:
        return print("K�ige odavam on Maksitaksi")
    elif s�ps < maksitaksi and s�ps < waldo:
        return print("K�ige odavam on S�ps veab")
    elif waldo < s�ps and waldo < maksitaksi:
        return print("K�ige odavam on Waldo takso")
takso(7)