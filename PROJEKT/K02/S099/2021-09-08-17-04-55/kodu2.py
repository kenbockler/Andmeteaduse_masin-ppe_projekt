from math import ceil
pikkus = int(input("Sisesta liini pikkus: "))
vahe = int(input("Sisesta postide maksimaalkaugus: "))
postide_arv = ceil(pikkus / vahe) + 1
print(str(postide_arv))