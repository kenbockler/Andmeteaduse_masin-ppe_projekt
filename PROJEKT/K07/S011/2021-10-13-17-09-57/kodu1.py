def poisse_ja_t�drukuid(a):
    m = 0
    n = 0
    for el in a:
        nimi_ja_sugu = el.split(" ")
        sugu = nimi_ja_sugu[-1]
        if sugu == "P" :
            m += 1
        if sugu == "T" :
            n += 1
    return (m,n)