import math
def koogi_hind(name, size):
    if(name.lower() == "šokolaadikook"):
        return round(math.pi * size * size * 0.06, 2)
    elif(name.lower() == "ploomikook"):
        return round(math.pi * size * size * 0.04, 2)
    elif(name.lower() == "napoleoni kook"):
        return round(size * size * 0.10, 2)
    else:
        raise Exception("Sellist kooki andmebaasist ei leitud")
cakename = ""
cakesize = 0
try:
    while(True):
        cakename = str(input("Sisestage koogi nimi: "))
        if(cakename == ""):
            break
        cakesize = float(input("Sisestage koogi mõõt: "))
        print(koogi_hind(cakename, cakesize))
except Exception as e:
    print(e)