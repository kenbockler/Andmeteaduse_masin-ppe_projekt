file = open("kinganumbrid.txt")
for rida in file:
    try:
        kinganumber = float(rida.strip())
        pikkus = round(2/3 * (kinganumber - 2))
        print(pikkus)
    except:
        print("Vigane sisend")