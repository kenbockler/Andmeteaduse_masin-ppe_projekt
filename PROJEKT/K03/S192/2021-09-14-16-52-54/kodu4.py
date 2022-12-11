kinganr = open('kinganumbrid.txt')
while True:
    sisu = kinganr.readline()
    if sisu == '':
        break
    else:
        try:
            sisu = float(sisu)
            print(round(2/3 * (sisu-2)))
        except:
            print('Vigane sisend')
kinganr.close()