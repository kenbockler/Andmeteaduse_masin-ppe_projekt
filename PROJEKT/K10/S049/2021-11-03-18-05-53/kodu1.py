def erinevad_sümbolid(a):
    el = set(a)
    return(el)
def sümbolite_sagedus(b):
    hulk = {}
    for el in b:
        if el in hulk:
            hulk[el] = hulk[el] + 1
        else:
            hulk[el] = 1   
    return(hulk)
def grupeeri(c):
    sõnastik = {'Täishäälikud': set(), 'Kaashäälikud': set(), 'Muud': set()}
    täishäälikud = ('a', 'e', 'i','o', 'u', 'õ', 'ä', 'ö','ü')
    kaashäälikud = ('b', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n',
                    'p', 'w', 'y', 'q', 'c', 'x', 'r', 's','š', 'z', 'ž', 't', 'v')
    b = sümbolite_sagedus(c)
    for el, x in b.items():
        if el in täishäälikud:
            m = (el, x)
            sõnastik['Täishäälikud'].add(m) 
        elif el in kaashäälikud:
            m = (el, x)
            sõnastik['Kaashäälikud'].add(m)
        else:
            m = (el, x)
            sõnastik['Muud'].add(m)
    return(sõnastik)
