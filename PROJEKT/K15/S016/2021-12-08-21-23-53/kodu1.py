f = open("aadressid.txt", "r", encoding = "UTF-8")
for rida in f:
    if rida.startswith("http://www.ut.ee/~"):
        i = rida.index("~")
        tulemus = rida[i+1:-1]
        x = tulemus.index("/")
        l�plik = tulemus[0:x]
        print(l�plik)