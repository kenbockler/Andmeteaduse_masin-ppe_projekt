def poisse_ja_t�drukuid(j�rjend):
    t�drukud = 0
    poisid = 0
    for el in j�rjend:
        if el[-1] == 'P':
            poisid += 1
        if el[-1] == "T":
            t�drukud = t�drukud + 1
    arv = (poisid, t�drukud)
    return arv
poisse_ja_t�drukuid(['Mati P', 'Kati T', 'Siim Aleksander P', 'J�ri P', 'Veronika T'])