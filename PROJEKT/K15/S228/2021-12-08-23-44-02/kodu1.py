import re
fail = open('aadressid.txt', encoding = 'UTF-8')
for rida in fail:
    otsitav = re.search('http://www.ut.ee/~(\w+)/', rida) 
    if otsitav:
        print(otsitav.group(1))
fail.close()