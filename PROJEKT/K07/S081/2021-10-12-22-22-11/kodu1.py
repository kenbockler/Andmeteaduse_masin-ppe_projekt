def poisse_ja_tüdrukuid(a):
    poisse = 0
    tüdrukuid = 0
    for i in range(len(a)):
        sugu = (a[i])[-1]
        if sugu == 'P':
            poisse += 1
        else:
            tüdrukuid += 1
    return((poisse, tüdrukuid))