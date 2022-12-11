pikkus = int(input("Sisesta elektriliini pikkus(m): "))
max_kaugus = int(input("Sisesta kõrvalasetsevate postide maksimaalkaugus(m): "))
if max_kaugus >= pikkus:
    min_poste = 2
else:
    if pikkus % max_kaugus != 0:
        min_poste = pikkus // max_kaugus + 2
    else:
        if pikkus // max_kaugus == pikkus:
            min_poste = pikkus // max_kaugus + 1
        else:
            min_poste = pikkus // max_kaugus
print(f"Minimaalselt läheb vaja {int(min_poste)} posti")