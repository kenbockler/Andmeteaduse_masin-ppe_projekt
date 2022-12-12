f = open('kinganumbrid.txt')
while True:
    txt = f.readline()
    txt.strip()
    if txt == "":
        break
    elif txt.strip().isnumeric():
        print(round(2 / 3 * (float(txt)-2)))
    elif not txt.isnumeric():
        try:
            isinstance(float(txt), float)
            print(round(2 / 3 * (float(txt)-2)))
        except:
            print("Vigane sisend")