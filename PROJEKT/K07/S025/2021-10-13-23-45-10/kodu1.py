def poisse_ja_t�drukuid(j�rjend):
    poisid = 0
    t�drukud = 0
    for a in j�rjend:
        for b in a[-1]:
            if b == 'P':
                poisid += 1
            if b == 'T':
                t�drukud += 1
    return (poisid, t�drukud)