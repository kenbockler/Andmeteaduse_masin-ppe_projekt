def erinevad_sümbolid(x):
    osad = set(x)
    return osad
def sümbolite_sagedus(y):
    sõnastik = {}
    sumbolid = list(y)
    for i in range(len(sumbolid)):
        vastus = sumbolid.count(y[i])
        sõnastik[y[i]] = vastus
    return sõnastik
def grupeeri(z):
    sõnastik = {}
    sona = {}
    sumbolid = list(z)
    for i in range(len(sumbolid)):
        vastus = sumbolid.count(z[i])
        sõnastik[z[i]] = vastus
        if sumbolid[i] in "aeiouõäöü":
            sona["Täishäälikud"] = set(sumbolid[i])
        elif sumbolid[i] in "bdfghjklmnoprsšzžtv":
            sona["Kaashäälikud"] = set(sumbolid[i])
        else:
            sona["Muud"] = set(sumbolid[i])
    return sona
print(grupeeri("sõida tasa üle silla"))