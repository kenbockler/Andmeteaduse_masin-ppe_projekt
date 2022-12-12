from math import *
liinipikkus = int(input("Mis on liini pikkus?" + " "))
maksimaalkaugus = int(input("Mis on maksimaalkaugus?" + " "))
postidearv = ceil(liinipikkus / maksimaalkaugus) + 1
print("Postide arv on: " + str(postidearv))