def poisse_ja_tüdrukuid(a):
    boys = 0
    girls = 0
    for element in a:
        x = element[-1]
        if x == "T":
            girls += 1
        if x == "P":
            boys += 1
    return(boys,girls)