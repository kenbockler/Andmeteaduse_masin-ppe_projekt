def poisse_ja_t�drukuid(j�rjend):
    m = 0
    n = 0
    for rida in j�rjend:
        if rida[-1] == "P":
            m += 1
        if rida[-1] == "T":
            n += 1
    return m, n
