def poisse_ja_t�drukuid (j�rjend):
    poistearv = 0
    t�drukutearv = 0
    for inimene in j�rjend:
        if inimene[len (inimene) - 1] == "P":
            poistearv += 1
        else:
            t�drukutearv += 1
    return (poistearv, t�drukutearv)
print (poisse_ja_t�drukuid (['Mati P', 'Kati T', 'Siim Aleksander P', 'J�ri P', 'Veronika T']))