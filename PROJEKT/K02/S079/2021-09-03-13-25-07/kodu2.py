from math import ceil
pikkus = int(input("Palun sisesta liini pikkus (täisarvuna meetrites): "))
max_kaugus = int(input("Palun sisesta kõrvutiasetsevate postide maksimaalkaugus (täisarvuna meetrites): "))
postide_arv = ceil(pikkus/max_kaugus) + 1
print(postide_arv)
             