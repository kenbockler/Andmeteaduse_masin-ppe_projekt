f = open('lapsed.txt')
n = open('nimed.txt', encoding = 'utf-8')
def seosta_lapsed_ja_vanemad(f, n):
    d = {}
    lopp = {}
    for rida in n:
        c = rida.strip().split(' ',1)
        d[c[0]] = c[1]
    for rida in f:
        a = rida.strip().split()
        voti = a[1]
        vaartus = a[0]
        if voti in d:
            if voti not in lopp:
                lopp[d[voti]] = set()
        if vaartus in d:
            if d[vaartus] not in lopp:
                lopp[d[voti]].add(d[vaartus])
            else:
                lopp[d[voti]].add(d[vaartus])
    print(lopp)
print(seosta_lapsed_ja_vanemad(f,n))
f.close()
n.close()