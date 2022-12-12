from statistics import harmonic_mean
failinimi = "aktsiad.txt" 
perioodi_pikkus = int(input("Sisesta perioodi pikkus: "))
def silu_andmed(andmed, perioodi_pikkus):
    with open(andmed) as fail:
        aktsiahinnad = []
        for rida in fail:
            rida = rida.strip().split(', ')
            aktsiahinnad.append(float(rida[1]))
    pikkus = len(aktsiahinnad)
    keskmised = []
    for i in range(pikkus):
        periood = aktsiahinnad[i:i+perioodi_pikkus]
        keskmine = round(harmonic_mean(periood), 6)
        keskmised.append(keskmine)
    return(keskmised)
print(silu_andmed(failinimi, perioodi_pikkus))