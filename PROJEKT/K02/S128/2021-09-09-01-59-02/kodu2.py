import math
liini_pikkus = int(input("Mis on liini pikkus?: "))
maksimaalkaugus = int(input("Mis on kõrvutiasetsevate postide vaheline maksimaalkaugus?: "))
postide_arv = math.ceil(liini_pikkus / maksimaalkaugus + 1)
print(postide_arv)