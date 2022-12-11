from statistics import harmonic_mean
import matplotlib.pyplot as plt
def silu_andmed(algandmed_järjendina, keskmistamise_rakendamise_arv):
    järjend2 = []
    väljastatav_järjend = []
    for i in range(len(algandmed_järjendina)):
        järjend2.append(algandmed_järjendina[i])
        if len(järjend2) > keskmistamise_rakendamise_arv:
            järjend2.pop(0)
        harmooniline_keskmistamine = harmonic_mean(list(map(float, (järjend2))))
        väljastatav_järjend.append(harmooniline_keskmistamine)
    return väljastatav_järjend
fail = input("Palun sisestage failinimi: ")
aktsiafail = open(fail, encoding = "UTF-8")
viimaste_elementide_järjend = []
for rida in aktsiafail:
    elemendid_aktsiajärjendist = rida.split()
    viimaste_elementide_järjend.append(float(elemendid_aktsiajärjendist[3]))
aktsiafail.close()
silutud_järjend = silu_andmed(viimaste_elementide_järjend, 50)
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.plot(viimaste_elementide_järjend, label = "Silumata")
ax.plot(silutud_järjend, label = "Silutud")
ax.legend()
plt.show()