from math import ceil
liini_pikkus = int(input("Sisesta liini pikkus t�isarvuna (meetrites): "))
postide_max_kaugus = int(input("Sisesta k�rvutiasetsevate postide maksimaalkaugus t�isarvuna (meetrites): "))
if liini_pikkus > postide_max_kaugus:
    postid = ceil(liini_pikkus / postide_max_kaugus) + 1
else:
    postid = 2
print("Elektriliini ehitamiseks kulub minimaalselt " + str(postid) + " posti")
