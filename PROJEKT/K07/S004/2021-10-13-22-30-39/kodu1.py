def poisse_ja_tüdrukuid(maania):
    tarv=0
    parv=0
    for x in maania:
        if x[-1]=="P":
            parv+=1
        elif x[-1]=="T":
            tarv+=1
    pp=(parv,tarv)
    return(pp)
