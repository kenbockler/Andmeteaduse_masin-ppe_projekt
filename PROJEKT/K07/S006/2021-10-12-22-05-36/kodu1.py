def poisse_ja_t�drukuid(nimed):
    poisid = 0
    t�tred = 0
    for nimi in nimed:
        list(nimi)
        if nimi[-1] == "P" and nimi[-2] == " ":
            poisid += 1
        elif nimi[-1] == "T" and nimi[-2] == " ":
            t�tred += 1
        else:
            continue
    ennik = (poisid, t�tred)
    return ennik
nimed = ['Mati P', 'Kati T', 'Siim AleksanderP', 'J�ri P', 'Veronika T']
print(str(poisse_ja_t�drukuid(nimed)))