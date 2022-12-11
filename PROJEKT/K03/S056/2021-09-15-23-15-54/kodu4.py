fail = open("kinganumbrid.txt", encoding = "utf-8")
while True:
    rida = fail.readline()
    if rida == "":
        break
    try:
        kinganumber = float(rida)
        pikkus = round(2/3 * (kinganumber - 2))
        print(pikkus)
    except:
        print("Vigane sisend")
fail.close()