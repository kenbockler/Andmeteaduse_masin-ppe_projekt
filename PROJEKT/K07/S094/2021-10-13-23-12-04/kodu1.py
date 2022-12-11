def poisse_ja_tüdrukuid(nimed):
    poiste_arv = 0
    tydrukute_arv = 0
    for nimi in nimed:
        viimane_taht = nimi[-1]
        if(viimane_taht == "P"):
            poiste_arv += 1
        elif(viimane_taht == "T"):
            tydrukute_arv += 1
    return poiste_arv, tydrukute_arv
