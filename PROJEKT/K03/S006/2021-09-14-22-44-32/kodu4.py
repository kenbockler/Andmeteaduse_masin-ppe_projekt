f = open("kinganumbrid.txt")
while True:
    kinganr = f.readline()
    if kinganr == "":
        break
    else:
        try:
            �mardus = round(float(kinganr))
            str(�mardus).isnumeric()
            print(round(2/3 * (float(kinganr) - 2)))
        except:
            print("Vigane sisend")
f.close()
