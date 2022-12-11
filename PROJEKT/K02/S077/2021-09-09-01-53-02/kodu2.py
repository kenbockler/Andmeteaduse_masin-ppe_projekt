from math import ceil
a=int(input("Sisesta elektriliini pikkus täisarvuna: "))
b=int(input("Sisesta kõrvutiasetsevate postide maksimaalne kaugus täisarvuna: "))
print()
if a<=b:
    print("Minimaalselt on elektriliini ehitamiseks vaja kahte posti.")
else:
    c=ceil(a/b + 1)
    print("Minimaalselt on elektriliini ehitamiseks vaja " + str(c) + " posti.")