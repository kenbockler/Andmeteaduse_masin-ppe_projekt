def poisse_ja_t�drukuid(nimed):
    poiss = 0
    tudruk = 0
    for n in range(len(nimed)):
        if nimed[n].endswith("P") == True:
            poiss += 1
        elif nimed[n].endswith("T") == True:
            tudruk += 1
    return (poiss,tudruk)