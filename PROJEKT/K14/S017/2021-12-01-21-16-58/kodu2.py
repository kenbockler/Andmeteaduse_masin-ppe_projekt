def v�ljasta_liin(eellane, j�rglane, s�nastik):
    if eellane == j�rglane:
        print(eellane)
        return True
    if j�rglane in s�nastik:
        for vanem in s�nastik[j�rglane]:
            if v�ljasta_liin(eellane, vanem, s�nastik):
                print(j�rglane)
                return True
    return False
