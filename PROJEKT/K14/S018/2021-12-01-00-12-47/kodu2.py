def printimine(j�r):
    for el in j�r:
        print(el)
def v�ljasta_liin(eel,j�rg,sug,mag=[]):
    if j�rg in sug:
        if eel in sug[j�rg]:
            mag.append(eel)
            mag.append(j�rg)
            printimine(mag)
            return True
        for inim in sug:
            if eel in sug[inim]:
                mag.append(eel)
                liin = v�ljasta_liin(inim,j�rg,sug)
                if liin:
                    return True
                else:
                    break
    return False