l�htefail=input("Sisestage l�htefaili nimi: ")
sihtfail=input("Sisestage sihtfaili nimi: ")
f1=open(l�htefail)
sisu_l�hte=f1.read()
sisu_l=sisu_l�hte.replace("Hello","Tere")
asendused=sisu_l�hte.count("Hello")
f1.close()
f2=open(sihtfail, "w")
f2.write(sisu_l)
f2.close()
if asendused==1:
    s�ne=" asendus."
else:
    s�ne=" asendust."
print("Tehti " + str(asendused) + s�ne)