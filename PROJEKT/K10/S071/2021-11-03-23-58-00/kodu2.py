def read_kontroll(rida):
    x = 0
    o = 0
    if rida[0] == rida[1] and rida[0] == rida[2]:
        if rida[0] == 'X':
            x += 1
        elif rida[0] == 'O':
            o += 1
    elif rida[1] == rida[2] and rida[1] == rida[3]:
        if rida[0] == 'X':
            x += 1
        elif rida[0] == 'O':
            o += 1
    xo = [x,o]
    return xo
def võitja(mängu_seis):
    sõnastik = {}
    for rida in mängu_seis:
        xo = read_kontroll(rida)
        sõnastik['X'] = xo[0]
        sõnastik['O'] = xo[1]
    esimesed = []
    for rida in mängu_seis:
        esimesed.append(rida[0])
    x = ['X','X','X']
    if x in esimesed:
        sõnastik['X'] = sõnastik.get['X'] + 1
    print(sõnastik)
võitja([['O',' ','O','X'],
        ['O','O','X','X'],
        ['O','X','O',' '],
        ['X','X','X','O']])
