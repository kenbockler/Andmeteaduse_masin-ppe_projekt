kilomeetrite_arv = float(input("Sisesta tee pikkus kilomeetrites: "))
f = open("taksohinnad.txt", encoding="UTF-8")
nimed = []
takso_hinnad = []
uus_j�rjend = []
for rida in f:
    j�rjend = rida.split(",")
    nimi = j�rjend[0]
    stardihind = float(j�rjend[1])
    kilomeetri_hind = float(j�rjend[2])
    takso_hind = stardihind + kilomeetrite_arv * kilomeetri_hind
    takso_hinnad.append(takso_hind)
    nimed.append(nimi)
    uus_j�rjend.append(nimi)
    uus_j�rjend.append(takso_hind)
    if rida == "":
        break
v�ikseim = min(takso_hinnad)
indeks = uus_j�rjend.index(v�ikseim)
nime_indeks = indeks - 1
print("K�ige odavam on", uus_j�rjend[nime_indeks] + ".")
f.close()