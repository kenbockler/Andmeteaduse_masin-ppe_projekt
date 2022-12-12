def poisse_ja_tüdrukuid(nimekiri):
    m = 0
    n = 0
    for nimi in nimekiri:
        if nimi[-1] == 'P':
            m += 1
        elif nimi[-1] == 'T':
            n += 1
        else:
            print('Viga! Sugu pole listis määratud vastavalt standardile.')
    return tuple((m, n))