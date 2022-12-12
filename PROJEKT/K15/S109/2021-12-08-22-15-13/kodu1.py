import re
fail = open("aadressid.txt", encoding="UTF-8")
for rida in fail:
    var = re.search('www.ut.ee/', rida)
    nimi = re.search('~(\d+)/', var)
    print(nimi.group(1))
fail.close()