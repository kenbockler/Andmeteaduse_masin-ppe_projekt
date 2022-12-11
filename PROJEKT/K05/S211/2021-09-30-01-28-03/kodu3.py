def moos(suurte_kogus, väikse_kogus, moosi_kogus):
    kokku = 0
    while (moosi_kogus-5)>=0 and suurte_kogus>0:
        moosi_kogus -= 5
        suurte_kogus -= 1
        kokku += 1
    if moosi_kogus == 0:
        return(kokku)
    else:
        while moosi_kogus>0:
            if väikse_kogus>0:
                moosi_kogus -= 1
                väikse_kogus -= 1
                kokku += 1
            else:
                return(-1)
    return(kokku)
print(moos(4, 3, 23))