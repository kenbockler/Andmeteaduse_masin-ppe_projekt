import re
user = input('Sisesta kasutajanimi: ')
while True:
    pass1 = input('Sisesta parool: ')
    pass2 = input('Sisesta parool teist korda: ')
    if not pass1 == pass2:
        print('Paroolid ei kattu, proovi uuesti.')
        continue
    elif not len(pass1) >= 8:
        print('Parool pole vähemalt 8 tähemärki pikk, proovi uuesti.')
        continue
    elif not re.search('\d', pass1) or not re.search('[a-zA-Z]', pass1):
        print('Paroolis pole korraga tähti ja numbreid, proovi uuesti.')
        continue
    break
pass1 = pass1[::-1]
f = open('users.txt', 'a')
f.write(f'\n{user}:{pass1}')
f.close()