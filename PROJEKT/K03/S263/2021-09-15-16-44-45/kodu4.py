f = open("kinganumbrid.txt")
while True:
    rida = f.readline()
    if rida == "" :
        break
    else:
        try:
            kinganumber = round((2/3 * (float(rida) - 2)))
            print(kinganumber)
        except:
            print("Vigane sisend")
f.close()
