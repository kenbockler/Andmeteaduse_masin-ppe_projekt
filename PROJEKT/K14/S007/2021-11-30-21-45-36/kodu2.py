def v�ljasta_liin(eelane, j�rglane, s�nastik):
    if eelane == j�rglane:
        print(j�rglane)
        return True
    elif j�rglane not in s�nastik.keys():
        return False
    else:
        isa = v�ljasta_liin(eelane, s�nastik[j�rglane][0],s�nastik)
        ema = v�ljasta_liin(eelane, s�nastik[j�rglane][1],s�nastik)
        if ema:
            print(j�rglane)
        if isa:
            print(j�rglane)
        return isa or ema
    