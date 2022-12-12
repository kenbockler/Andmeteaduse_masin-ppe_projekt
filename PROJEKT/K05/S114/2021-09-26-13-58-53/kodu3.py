def moos(suurK,vaikeK,kilogramm):
    karpidearv = 0
    if (suurK*5+vaikeK) < kilogramm:
        return -1
    while True:
        while suurK > 0 and kilogramm >= 5:
            kilogramm = kilogramm - 5
            karpidearv += 1
            suurK -=1
        while vaikeK > 0 and kilogramm > 0:
            kilogramm = kilogramm -1
            karpidearv += 1
            vaikeK -=1
        if vaikeK == 0 and kilogramm > 0:
            karpidearv = -1
        break
    return karpidearv