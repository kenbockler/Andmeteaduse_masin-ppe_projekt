from math import ceil
a = int(input("Sisesta soovitud liini pikkus meetrites: "))
b = int(input("Sisesta soovitud kõrvutiasetsevate postide maksimaalkaugus meetrites: "))
x = ceil(a/b) + 1
print(x)
