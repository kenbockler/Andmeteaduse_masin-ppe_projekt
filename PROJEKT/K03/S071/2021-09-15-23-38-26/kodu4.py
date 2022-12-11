f = open("kinganumbrid.txt", "r")
for rida in f:
    try:
        print(round(2 / 3 * (float(rida) - 2)))
    except:
        print("Vigane sisend")
f.close()
