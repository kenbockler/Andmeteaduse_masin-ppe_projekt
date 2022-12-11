kilomeetrite_arv = float(input("Sisesta tee pikkus kilomeetrites: "))
fail = open("taksohinnad.txt", encoding="UTF-8")
taksode_hinnad = []
for rida in fail:
    rida = rida.split(",")
    stardihind = rida[1]
    stardihind = float(stardihind)
    kilomeetri_tasu = rida[2]
    kilomeetri_tasu = float(kilomeetri_tasu)
    hind = stardihind + kilomeetrite_arv*kilomeetri_tasu
    taksode_hinnad.append(hind)
väiksem = min(taksode_hinnad)
indeks = taksode_hinnad.index(väiksem)
if indeks == 0:
    print("Kõige odavam takso Maksitaksi.")
elif indeks == 1:
    print("Kõige odavam takso 'Sõps veab'.")
elif indeks == 2:
    print("Kõige odavam takso 'Waldo takso'.")
