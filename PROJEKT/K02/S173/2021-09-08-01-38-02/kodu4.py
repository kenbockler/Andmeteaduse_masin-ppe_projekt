a = open(input("Sisesta faili nimi:"))
b = open(input("sisesta teise faili nimi:"), "a")
A = a.read()
c = A
B = A
if "Hello" in B:
    B = B.replace("Hello","Tere")
    b.write(B)
    print("Tehti " + str(c.count("Hello")) + " muudatust.")
else:
    print("Tehti 0 muudatust.")
a.close()
b.close()