l�htefail = input("Sisesta l�htefaili nimi: ")
sihtfail = input("Sisesta sihtfaili nimi: ")
f = open(l�htefail, "r")
sisu = f.read()
hello = "Hello"
tere = "Tere"
asendused = sisu.count(hello)
f.close()
s = open(sihtfail, "w")
s.write(sisu.replace(hello,tere))
s.close()
print("Sooritati", asendused, "asendust.")