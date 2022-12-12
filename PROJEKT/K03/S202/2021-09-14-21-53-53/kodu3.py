un = int(input("Sisestage naturaalarv: "))
n = 0
nrs = 0
nsr = 0
while n <= un: 
    nrs += (n**2)
    n += 1
n = 0
while n <= un:
    nsr += n
    n += 1
print("Esimese " + str(un) + " naturaalarvu summa ruudu ja ruudu summa vahe on: " + str((nsr**2) - nrs))