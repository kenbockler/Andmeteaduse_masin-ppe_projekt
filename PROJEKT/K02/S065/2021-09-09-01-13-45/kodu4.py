a = input("Lähtefaili nimi: ")
b = input("Sihtfaili nimi: ")
faila = open(a, encoding="UTF-8")
failb = open(b, "w", encoding="UTF-8")
i=0
for rida in faila:
    failb.write(rida.replace("Hello", "Tere"))
    i += rida.count("Hello")
faila.close()
failb.close()
print("Tehti",i,"asendust.")