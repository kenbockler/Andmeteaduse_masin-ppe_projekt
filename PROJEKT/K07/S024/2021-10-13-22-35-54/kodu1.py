def poisse_ja_t�drukuid(j�rjend):
    poisid = 0
    t�drukud = 0
    for rida in j�rjend:
        uus_j�rjend = rida.split(" ")
        if uus_j�rjend[-1] == "P":
            poisid += 1
        elif uus_j�rjend[-1] == "T":
            t�drukud += 1
    return (poisid, t�drukud)
        