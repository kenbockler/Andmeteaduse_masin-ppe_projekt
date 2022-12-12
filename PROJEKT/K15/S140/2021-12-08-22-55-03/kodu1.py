import re
print('Kasutajanimed on:')
with open('aadressid.txt', encoding='utf-8') as f:
    for rida in f:
        rida = rida.strip()
        if re.match(r'\bhttp://www.ut.ee/~\b', rida):
            rida = rida.replace('http://www.ut.ee/~', '').split('/')
            print(rida[0])
