def poisse_ja_t�drukuid(j�rjend):
    m = 0
    n = 0
    for i in j�rjend:
        if i.count(" P") > 0:
            m += 1
        elif i.count(" T") > 0:
            n += 1
    return (m, n)
        