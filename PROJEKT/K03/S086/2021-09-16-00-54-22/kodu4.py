f = open("kinganumbrid.txt", encoding = "UTF-8")
while True:
    try:
        kinganumber = f.readline()
        if kinganumber == "":
            break
        print(str(round(2/3 * (float(kinganumber) - 2))))
    except:
        print("Vigane sisend")