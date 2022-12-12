def poisse_ja_tüdrukuid(inimesed):
    p = 0
    t = 0
    for inimene in inimesed:
        if inimene.split()[-1] == "P":
            p += 1
        elif inimene.split()[-1] == "T":
            t += 1
    return (p, t)
