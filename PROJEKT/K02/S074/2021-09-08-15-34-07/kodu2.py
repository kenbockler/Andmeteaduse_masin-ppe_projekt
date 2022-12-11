from math import ceil
pikkus = int(input("Sisesta liini pikkus: "))
kaugus = int (input("Sisesta postide maksimaalkaugus: "))
kogus = ceil(pikkus/kaugus) +1
print(kogus)