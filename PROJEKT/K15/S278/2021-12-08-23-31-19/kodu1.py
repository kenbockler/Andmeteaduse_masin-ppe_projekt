import re
fail = open("aadressid.txt", encoding = "UTF-8")
lingialgus = "http"
veebiaadressilink = "ut.ee/~(\w*)/"
for rida in fail:
    ridad = rida
    web = re.search(lingialgus, ridad)
    if web:
        veebinimi = re.search(veebiaadressilink, ridad)
        if veebinimi:
            print(veebinimi.group(1))
