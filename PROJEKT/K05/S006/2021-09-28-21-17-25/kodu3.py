def moos(suurte_arv, v�ikeste_arv, kaal):
    karbid_kokku = 0
    while (kaal - 5) >= 0 and suurte_arv > 0:
        kaal -=  5
        suurte_arv -= 1
        karbid_kokku += 1
        if suurte_arv <= 0:
            break
    while (kaal - 1) >= 0:
        kaal -= 1
        v�ikeste_arv -= 1
        karbid_kokku += 1
        if v�ikeste_arv <= 0 and kaal > 0:
            karbid_kokku = -1
            break
    return(karbid_kokku)
suurte_arv =0
v�ikeste_arv =10
kaal = 7
moos(suurte_arv, v�ikeste_arv, kaal)
print(moos(suurte_arv, v�ikeste_arv, kaal))
    