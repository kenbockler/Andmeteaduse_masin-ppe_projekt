from math import pi
def koogi_hind (koogid, m��dud):
    if koogid == "�okolaadikook":
        return round((m��dud**2 * pi) * 0.06, 2)
    elif koogid == "ploomikook":
        return round((m��dud**2 * pi) * 0.04, 2)
    elif koogid == "Napoleoni kook" or koogid == "napoleoni kook":
        return round((m��dud**2) * 0.1, 2)
while True:
    koogid = input("Sisestage soovitav kook: ")
    if koogid == "":
        break
    elif koogid != "�okolaadikook" and koogid != "ploomikook" and koogid != "Napoleoni kook" and koogid !="napoleoni kook":
        print ("Sellist kooki meie men��s ei ole!")
    else:
        m��dud = float(input ("Sisestage soovitava koogi m��t: "))
        print (koogi_hind(koogid, m��dud))