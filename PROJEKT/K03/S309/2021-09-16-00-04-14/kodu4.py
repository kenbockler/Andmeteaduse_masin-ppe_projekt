failinimi = "kinganumbrid.txt"
with open((failinimi), "r") as fail:
    for line in fail:
        try:
            kinganumber = float(line)
            pikkus = round((2/3 * (kinganumber - 2)))
            print(pikkus)
        except:
            print("Vigane sisend")