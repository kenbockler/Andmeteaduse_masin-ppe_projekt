failinimi = "kinganumbrid.txt"
f = open(failinimi)
while True:
    EU = f.readline()
    if EU == "":
        break
    else:
        try:
            EU = float(EU)
            pikkus = round(2/3 * (EU-2))
            print(pikkus)
        except:
            print("Vigane sisend")
    