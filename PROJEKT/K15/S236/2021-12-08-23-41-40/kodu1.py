import re
with open('aadressid.txt', encoding='UTF-8') as fail:
    print('Kasutajanimed on: ')
    for rida in fail:
        muster =  'http://www.ut.ee/~([a-z0-9]+)'
        tulemus = re.search(muster, rida)
        if tulemus:
            nimi = (tulemus.group(1))
            print(nimi)
        else:
            pass
