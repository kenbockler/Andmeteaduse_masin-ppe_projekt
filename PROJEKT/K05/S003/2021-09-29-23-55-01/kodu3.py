def moos(suuredkarbid, v�iksedkarbid, moosikogus):
    karpidearv = 0
    if moosikogus <= 0:
        return 0
    if moosikogus >= 5:
        for i in range(suuredkarbid):
            moosikogus -= 5
            karpidearv += 1
            if moosikogus <= 0:
                return karpidearv
            if moosikogus < 5:
                break
    for i in range(v�iksedkarbid):
        moosikogus -= 1
        karpidearv += 1
        if moosikogus == 0:
            return karpidearv
    return -1