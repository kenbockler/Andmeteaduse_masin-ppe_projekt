def poisse_ja_t�drukuid(j�r):
    p = 0
    t = 0
    for i in j�r:
        n = len(i) - 1
        if i[n] == "P":
            p += 1
        else:
            t += 1
    return(p, t)
j�rjend = ['Mati P', 'Kati T', 'Siim Aleksander P', 'J�ri P', 'Veronika T']
poisse_ja_t�drukuid(j�rjend)