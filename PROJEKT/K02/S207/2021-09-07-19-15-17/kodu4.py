lahtenimi = str(input("Sisestage lähtefaili nimi: "))
loppnimi = str(input("Sisestage lõppfaili nimi: "))
lahtefail = open(lahtenimi, encoding = "UTF-8")
tekst = lahtefail.read()
print("Tehti", tekst.count("Hello"), "asendamist.")
tekst = tekst.replace("Hello", "Tere")
loppfail = open(loppnimi,"w", encoding = "UTF-8")
loppfail.write(tekst)
lahtefail.close()
loppfail.close()