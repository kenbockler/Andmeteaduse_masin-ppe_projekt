import math
a = int(input("palun sisesta liini pikkus meetrites: "))
b = int(input("palun sisesta k�rvutiasetsevate postide maksimaalkaugus meetrites: "))
postideArv = math.ceil((a/b) + 1)
print(postideArv)