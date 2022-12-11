from math import ceil, floor
liini_pikkus = int(input("Mis on elektriliini pikkus? Sisesta täisarvu ja meetrites: "))
postide_maxkaugus = int(input("Milline on kõrvutiasestsevate postide maksimaalkaugus?(täisarv meetrites): "))
postide_arv = liini_pikkus / postide_maxkaugus + 1
print("Postide arv on: " + str(ceil(postide_arv)))