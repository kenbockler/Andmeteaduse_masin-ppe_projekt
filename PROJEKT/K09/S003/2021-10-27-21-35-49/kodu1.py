import matplotlib.pyplot as plt
def silu_andmed(j�rjend, arv):
    uusj�rjend = []
    from statistics import harmonic_mean
    for i in range(len(j�rjend)):
        if i < arv:
            esimene = 0
        else:
            esimene = i-arv+1
        uusj�rjend.append(harmonic_mean(j�rjend[esimene:i+1]))
    return uusj�rjend
failinimi = input("palun sisesta failinimi: ")
fail = open(failinimi)
kuup�evad = []
hinnad = []
for rida in fail:
    reaj�rjend = rida.strip("\n").split(",")
    kuup�evad.append(reaj�rjend[0])
    hinnad.append(float(reaj�rjend[1]))
for i in range(len(kuup�evad)):
    kuup�evad[i]= i
silutudhinnad = silu_andmed(hinnad,3)
plt.plot(kuup�evad, hinnad, silutudhinnad)
plt.xlabel("Kuup�evad")
plt.show()
