def poisse_ja_tüdrukuid(list):
    p = 0
    t = 0
    for rida in list:
        sugu = rida[-1]
        if sugu == 'P':
            p += 1
        if sugu == 'T':
            t += 1
    return (p, t)