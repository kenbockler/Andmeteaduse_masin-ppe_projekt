def erinevad_sümbolid(sõne):
    return set(sõne)
def sümbolite_sagedus(sõne):
    d = {}
    for sümbol in sõne:
        d[sümbol] = d.get(sümbol, 0) + 1
    return d
def grupeeri(sõne):
    täishäälikud = "aeiouõäöüAEIOUÕÄÖÜ"
    d = {}
    for sümbol in sõne:
        d[sümbol] = d.get(sümbol, 0) + 1
    d2 = {"Täishäälikud": set(),
          "Kaashäälikud" : set(),
          "Muud" : set()}
    for võti in d:
        if võti in täishäälikud:
            d2["Täishäälikud"].add((võti, d[võti]))
        elif võti.isalpha() != True:
            d2["Muud"].add((võti, d[võti]))
        else:
            d2["Kaashäälikud"].add((võti, d[võti]))
    return(d2)
    