def erinevad_s�mbolid(a):
    k = set()
    for i in a:
        if i not in k:
            k.add(i)
        else:
            continue
    return k
def s�mbolite_sagedus(a):
    k = {}
    for i in a:
        if i not in k:
            k[i] = 0
            k[i] = k[i] + 1
        else:
            k[i] = k[i] + 1
    return k
def grupeeri(a):
    t�ish��likud = ["a", "e", "i", "o", "u", "�", "�", "�", "�"]
    kaash��likud = ["b","d","f","g","h","j","k","l","m","n","p","r","s","�","z","�","t","v","c"]
    k = s�mbolite_sagedus(a)
    t = {}
    t["t�ish��likud"] = ()
    t["kaash��likud"] = ()
    t["muud"] = ()
    for i in k:
        if i in t�ish��likud:
            t["t�ish��likud"] =t["t�ish��likud"]  + ((i,k[i]))
        elif i in kaash��likud:
            t["kaash��likud"] = t["kaash��likud"] + ((i,k[i]))
        else:
            t["muud"] = t["muud"] + ((i,k[i]))
    return t
print(grupeeri("s�ida tasa �le silla"))
    