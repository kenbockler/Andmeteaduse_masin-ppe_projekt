def poisse_ja_tüdrukuid(eesnimi):
    loendurP=0
    loendurT=0
    for j in eesnimi:
        if list(j)[-1]=='P':
            loendurP+=1
        if list(j)[-1]=='T':
            loendurT+=1
    return (loendurP, loendurT)