f = open('kinganumbrid.txt')
num_lines = sum(1 for line in open('kinganumbrid.txt'))
count = 0
while num_lines > count:
    try:
        kinganumber = f.readline()
        pikkus = 2/3 * (float(kinganumber) - 2)
        print(round(pikkus))
        count += 1
    except:
        print("Vigane sisend")
        count += 1
f.close()
