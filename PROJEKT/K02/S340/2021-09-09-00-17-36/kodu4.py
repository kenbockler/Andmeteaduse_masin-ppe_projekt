inglise = input("Lähtefaili nimi: ")
eesti = input("Sihtfaili nimi: ")
g = open(inglise)
faili_sisu = g.read()
f = open("eesti" , "w")
f.write((faili_sisu).replace('Hello','Tere'))
f.close()
print("Tehti" , faili_sisu.count("Hello") , "asendamist.")
g.close()