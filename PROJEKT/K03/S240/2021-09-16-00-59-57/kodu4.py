f = open("kinganumber.txt", "r")
for x in f:
    if x.isnumeric():
        print (round(2/3 * (int(x)-2)))
    else:
        print("Vigane sisend")