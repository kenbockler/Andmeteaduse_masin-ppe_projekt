from math import *
liini_pikkus = int(input("Sisesta liini pikkus meetrites: "))
postide_kaugus = int(input("Sisesta postide kaugus meetrites: "))
postide_arv = liini_pikkus / postide_kaugus + 2
print("Minimaalselt on liini ehitamiseks poste vaja: ")
print(floor(postide_arv))
