j�r = []
def v�ljasta_liin(eellane, j�rglane, s�nastik):
    j�r.append(eellane)
    if j�rglane not in s�nastik:
        return False
    elif eellane in s�nastik[j�rglane]:
        j�r.append(j�rglane)
        for i in j�r:
            print(i)
        return True
    else:
        for i in s�nastik:
            if eellane in s�nastik[i]:
                uuseel = i
                break
        try:
            return v�ljasta_liin(uuseel, j�rglane, s�nastik)
        except:
            return False