def poisse_ja_t�drukuid(lapsed):
    t�druk = 0
    poiss = 0
    poiste_arv = []
    t�drukute_arv = []
    for lapse_info in lapsed:
        lapse_info = lapsed.split(' ')
        sugu = lapse_info[1]
        for t�druk in sugu:
            t�druk = len(sugu[:'T'])
            t�druk += 1
            t�drukute_arv = t�drukute_arv + [t�druk]
        elif poiss in sugu:
            poiss = len(sugu[:'P'])
            poiss += 1
            poiste_arv = poiste_arv + [poiss]
    return (poiste_arv, t�drukute_arv)
    laste_arv = (poiste_arv, t�drukute_arv)
    print(laste_arv)
poisse_ja_t�drukuid(['Mati P', 'Kati T', 'Siim Aleksander P', 'J�ri P', 'Veronika T'])
