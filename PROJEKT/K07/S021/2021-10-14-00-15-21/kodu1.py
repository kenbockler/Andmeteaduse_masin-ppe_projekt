def poisse_ja_t�drukuid(j�rjend):
    p=0
    t=0
    for s�ne in j�rjend:
        sugu = s�ne[-1]
        if sugu == "P":
            p += 1
            continue
        elif sugu == "T":
            t += 1
            continue
    return(p, t)  
poisse_ja_t�drukuid(["Mati P", "Kati T", "Siim Aleksander P", "J�ri P", "Veronika T"])