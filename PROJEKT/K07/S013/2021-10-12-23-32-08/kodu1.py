x=[]
def poisse_ja_t�drukuid(x):
    t�druk = 0
    poiss = 0
    for rida in x:
        uus_x =rida.split(" ")
        sugu = uus_x[-1]
        if sugu == "T":
            t�druk += 1
        elif sugu == "P":
            poiss += 1
    return poiss, t�druk
print(poisse_ja_t�drukuid(x))