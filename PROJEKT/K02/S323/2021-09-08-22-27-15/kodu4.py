fail1 = input("Lähtefail: ")
fail2 = input("Sihtfail: ")
f1 = open(fail1)
f2 = open(fail2, "w")
loend = 0
for line in f1:
    f2.write(line.replace("Hello", "Tere"))
    if "Hello" in line:
        loend += line.count("Hello")
print("Tehti", str(loend) ,"asendamist.")
f1.close()
f2.close()
