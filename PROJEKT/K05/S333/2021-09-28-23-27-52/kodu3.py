def moos(suur,väike,kogus):
    suurte_arv= 0
    väikeste_arv= 0
    while kogus // 5 >0 :
        if suur== 0:
            break
        kogus= kogus-5
        suurte_arv+= 1
        if suurte_arv== suur:
            break
    while kogus // 1 >0:
        if väike== 0:
            break
        kogus= kogus-1
        väikeste_arv+= 1
        if väikeste_arv== väike:
            break
    if kogus>0 :
        return(-1)
    else:
        return(suurte_arv+väikeste_arv)
    