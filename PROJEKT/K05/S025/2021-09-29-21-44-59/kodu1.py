def kattumine():
    parool_1 = str(input('Sisestage parool esimest korda: '))
    parool_2 = str(input('Sisestage parool teist korda: '))
    while parool_2 != parool_1:
        print('Paroolid ei kattu, palun proovige uuesti.')
        parool_1 = str(input('Sisestage parool esimest korda: '))
        parool_2 = str(input('Sisestage parool teist korda: '))
    global parool
    parool = parool_1
def pikkus():
    t�hed = len(parool)
    while t�hed < 8:
        print('Parool on liiga l�hike, palun proovige uuesti.')
        kattumine()
        t�hed = len(parool)
def numbrid_t�hed():
    numbrid = sum(nr.isdigit() for nr in parool)
    t�hed = sum(t�ht.isalpha() for t�ht in parool)
    if numbrid == 0 or t�hed == 0:
        return False
    else:
        return True
kasutajanimi = str(input('Sisestage kasutajanimi: '))      
kattumine()
pikkus()
while numbrid_t�hed() == False:
    print('Parool peab sisaldama nii t�hti kui ka numbreid.')
    kattumine()
    pikkus()
tagurpidi = parool [::-1]
f = open('users.txt', 'a')
f.write(kasutajanimi + ':' + tagurpidi)
f.close()