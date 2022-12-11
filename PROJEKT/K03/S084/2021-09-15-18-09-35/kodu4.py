with open("kinganumbrid.txt", "r") as file:
    lines = file.readlines()
    for line in lines:
        try:
            arv = float(line.strip())
            jalg = round(2 / 3 * (arv - 2))
            print(jalg)
        except:
            print("Vigane sisend")