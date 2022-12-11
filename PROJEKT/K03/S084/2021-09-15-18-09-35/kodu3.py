while True:
    try:
        n = int(input("Sisestage naturaalarv: "))
        break
    except:
        print("Midagi valesti")
a = n
nsum = 0
nruutsum = 0
while a > 0:
    nsum += a
    a -= 1
a = n
while a > 0:
    nruutsum += a * a
    a -= 1
tulemus = nsum * nsum - nruutsum
print(tulemus)