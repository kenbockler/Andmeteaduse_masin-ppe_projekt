def moos(suuredkarbid, v�iksedkarbid, moosikogus):
    karpide_kogus=0
    if moosikogus>=5:
        suurte_j��k=moosikogus%5
    else:
        suurte_j��k=0
    suuri_karpe=(moosikogus-suurte_j��k)//5
    if suuredkarbid<suuri_karpe:
        suuri_karpe=suuredkarbid
    v�ikeste_arv=moosikogus-suuri_karpe*5
    if suuredkarbid*5 + v�iksedkarbid<moosikogus:
        return int(-1)
    if suuri_karpe==0:
        if v�iksedkarbid>=moosikogus:
            return moosikogus
        else:
            return int(-1)
    elif suuredkarbid<suuri_karpe and v�iksedkarbid>=v�ikeste_arv:
        karpide_kogus+=suuri_karpe + v�ikeste_arv
        return int(karpide_kogus)
    elif suuredkarbid>=suuri_karpe and v�iksedkarbid<v�ikeste_arv:
        if suuri_karpe*5+v�iksedkarbid>=moosikogus:
            karpide_kogus+=suuri_karpe+v�ikeste_arv
            return int(karpide_kogus)
        else:
            return int(-1)
    elif suuredkarbid>=suuri_karpe and v�iksedkarbid>=v�ikeste_arv:
        karpide_kogus+= suuri_karpe + v�ikeste_arv
        return int(karpide_kogus)
    else:
        return int(-1)