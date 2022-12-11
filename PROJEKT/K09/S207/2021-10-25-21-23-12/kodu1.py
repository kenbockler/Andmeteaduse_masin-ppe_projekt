from statistics import harmonic_mean
def silu_andmed(andmed, n=50):
    tulem = []
    käsitlusel = []
    for i in range(0, n):
        käsitlusel += [andmed[i]]
        tulem += [harmonic_mean(käsitlusel)]
    for i in range(n, len(andmed)):
        käsitlusel.pop(0)
        käsitlusel.append(andmed[i])
        tulem += [harmonic_mean(käsitlusel)]
    return tulem
nimi = input("Sisestage failinimi: ")
andmed = []
with open(nimi, encoding = "UTF-8") as fail:
    for rida in fail:
        andmed += [float(rida.split(", ")[1].strip())]
silutud = silu_andmed(andmed)