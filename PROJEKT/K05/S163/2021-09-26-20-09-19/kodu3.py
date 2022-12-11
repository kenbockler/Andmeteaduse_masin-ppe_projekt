def moos(suured, väiksed, moos):
    karbid = 0
    while True:
        if moos >= 5 and suured >= 1:
            karbid += 1
            moos -= 5
            suured -= 1
            continue
        elif moos >= 1 and väiksed >= 1:
            karbid += 1
            moos -= 1
            väiksed -= 1
            continue
        else: 
            if moos > 0:
                return -1
            else:
                return karbid
print(moos(2, 6, 14))