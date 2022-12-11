from math import *
def moos(suur,väike,moos):
    if moos == 0:
        return 0
    suured = floor(moos/5)
    if suured >= 1 and suur >= 1 and suured == suur:
        suured = suured
    elif suured != suur:
        if suured > suur:
            suured = suur
        elif suur > suured:
            suured = suured
    else:
        suured = 0
    if suured < 0:
        return -1
    if suur != 0:
        moos -= suured * 5
    väiksed = moos / 1
    if väiksed > väike:
        return -1
    if väiksed / 1 < 1 and moos != 0:
        return -1
    if väike != 0:
        moos -= väiksed
    return int(suured + väiksed)
print(moos(2,6,14))