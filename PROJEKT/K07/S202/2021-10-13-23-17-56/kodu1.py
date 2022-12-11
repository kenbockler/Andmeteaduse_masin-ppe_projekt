def poisse_ja_tüdrukuid(nimisugu):
    Poisid = 0
    Tüdrukud = 0
    for el in nimisugu:
        splat = str(el).split() 
        if splat[-1] == "P":
            Poisid += 1
        if splat[-1] == "T":
            Tüdrukud += 1
    ennik = (Poisid, Tüdrukud)
    return(ennik)
