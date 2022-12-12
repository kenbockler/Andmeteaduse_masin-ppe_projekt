import math
liin= int(input("Sisesta soovitud liini pikkus meetrites: "))
kaugus= int(input("Sisesta soovitud kõrvutiasetsevate postide maksimaalkaugus meetrites: "))
post=liin/kaugus
vastus=math.ceil(post)
v1=vastus+1
print("ehitmiseks läheb vaja",v1,"posti.")
