a = (input("Lähtefaili nimi:"))
b = (input("Sihtfaili nimi:"))
inp = open(a, "r")
tekst = inp.read()
inp.close()
asendused = str(tekst.count("Hello"))
tekst = tekst.replace("Hello","Tere")
outp = open(b, "w")
outp.write(tekst)
outp.close()
print("Tehti "+ asendused + " asendamist.")
