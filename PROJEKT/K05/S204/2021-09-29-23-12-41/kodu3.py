suurte_karpide_arv=int(input("Suurte arv:"))
väikeste_karpide_arv=int(input("Väikeste arv:"))
moosi_kogus=int(input("Moosi kogus:"))
def moos(suurte_karpide_arv,väikeste_karpide_arv,moosi_kogus):
    d=moosi_kogus//5
    if d <= suurte_karpide_arv and moosi_kogus >= (5*d) and moosi_kogus <=(5*d+väikeste_karpide_arv):
        return(d+(moosi_kogus-5*d))
    if  d>suurte_karpide_arv or moosi_kogus < (5*d) or  moosi_kogus > (5*d+väikeste_karpide_arv):
        return("-1")
print(moos(suurte_karpide_arv,väikeste_karpide_arv,moosi_kogus))
