from math import ceil
liini_pikkus = int(input("Sisestage liini kogupikkus: "))
maksimaal_kaugus = int(input("Sisestage postide maksimaalkaugus: "))
minimaalseid = 0
if maksimaal_kaugus >= liini_pikkus:
    minimaalseid = 2
else:
    minimaalseid = ceil(liini_pikkus / maksimaal_kaugus) + 1
print("Elektriliini ehitamiseks on vaja minimaalselt " + str(minimaalseid) + " posti.")