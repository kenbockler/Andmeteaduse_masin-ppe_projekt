def erinevad_s�mbolid(s�ne):
    return set(list(s�ne))
def s�mbolite_sagedus(s�ne):
    d={}
    for s�mbol in list(s�ne):
        if s�mbol in d:
            d[s�mbol]=d[s�mbol]+1
        else:
            d[s�mbol]=1
    return d
def grupeeri(s�ne):
    d={}
    t=set()
    k=set()
    m=set()
    d['T�ish��likud']=t
    d['Kaash��likud']=k
    d['Muud']=m
    s�nastik=s�mbolite_sagedus(s�ne)
    for v�ti in s�nastik:
        if v�ti.lower() in 'aeiou����':
            t.add((v�ti,s�nastik[v�ti]))
        elif v�ti.lower() in 'bcdfghjklmnpqrs�z�tvwxy':
            k.add((v�ti,s�nastik[v�ti]))
        else:
            m.add((v�ti,s�nastik[v�ti]))
    return d
