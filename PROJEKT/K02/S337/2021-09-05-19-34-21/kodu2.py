import math
s = float(input("Liini pikkus meetrites: "))
d = float(input("Kõrvutiasetsevate postide maksimaalkaugus: "))
print(int(math.ceil(s/d+1)))