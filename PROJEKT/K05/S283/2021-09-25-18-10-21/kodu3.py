def moos (karp_5L, karp_1L, moos_x_L):
    karpide_arv = 0
    if karp_5L >= 1 and moos_x_L >= 5:
        while karp_5L > 0 and moos_x_L >= 5:
            moos_x_L -= 5
            karp_5L -= 1
            karpide_arv += 1
    if moos_x_L >= 1 and karp_1L >= moos_x_L:
        while moos_x_L > 0:
            moos_x_L -= 1
            karp_1L -=1
            karpide_arv += 1
    if moos_x_L == 0:
        return karpide_arv
    else:
        return -1
suur_karp = int(input("Sisestage suurte karpide arv: "))
väike_karp = int(input("Sisestage väikeste karpide arv: "))
moosi = int(input("Sisestage moosi kogus: "))
print(moos(suur_karp, väike_karp, moosi))