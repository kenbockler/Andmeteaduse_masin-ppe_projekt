fail = open('kinganumbrid.txt')
for rida in fail:
    try:
        kinganumber = float(rida.strip())
        pikkus = 2 / 3 * (kinganumber - 2)
        �_arv = round(pikkus)
        print(�_arv)
    except:
        print('Vigane sisend')