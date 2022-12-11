import re
f=open('aadressid.txt', encoding= 'UTF-8')
for rida in f:
    if re.match('(http://www.ut.ee/~)',rida):
        sõnad= rida.split('/')
        print(sõnad[3].lstrip('~'))
f.close()