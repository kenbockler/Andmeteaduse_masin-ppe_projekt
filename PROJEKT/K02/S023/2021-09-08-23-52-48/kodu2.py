import math
x  = int(input("Sisestage liini pikkus: "))
z = int(input("Sisestage k�rval asetsevate postide maksimaalne kaugus"))
print(math.ceil(x/z)-1+2)