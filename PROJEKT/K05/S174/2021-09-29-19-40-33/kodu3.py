def moos(suured, väiksed, moosikogus):
    karpide_arv = 0
    vaj_suured = moosikogus // 5
    if vaj_suured <= suured:
        karpide_arv += vaj_suured
        vaj_väiksed = moosikogus % 5
        if vaj_väiksed <= väiksed:
            karpide_arv += vaj_väiksed
        else:
            return -1
    else:
        return -1
    return karpide_arv