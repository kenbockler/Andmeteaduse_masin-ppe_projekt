import math
a = int(input("Palun sisesta liini pikkust (täisarvuna meetrites): "))
b = int(input("Palun sisesta kõrvutiasetsevate postide maksimaalkaugust (täisarvuna meetrites): "))
z = "Liini ehitamiseks minimaalselt on vaja: "
d = " posti"
c = math.ceil(a/b)
i = (int(c) + int(1))
print(z + str(i) + d)
