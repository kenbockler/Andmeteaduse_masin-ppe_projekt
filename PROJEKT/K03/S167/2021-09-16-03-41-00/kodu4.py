f = open("kinganumbrid.txt", "r")
while True:
    rida = f.readline().strip()
    try:
        if rida == "":
            break
        kinganr = float(rida.strip())
        jalanumber = float((2/3)*(kinganr-2))
        jalanumber2 = int(round(jalanumber))
        c=str(jalanumber2)
        print(c)
    except ValueError:
        a = print("Vigane sisend")
