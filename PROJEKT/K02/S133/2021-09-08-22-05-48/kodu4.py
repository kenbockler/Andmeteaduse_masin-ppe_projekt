fail1=input("sisestage tõlgitava faili nimi: ")
f1s=open(fail1,"r")
faili_sisu=f1s.read()
a = faili_sisu.count("Hello")
b = faili_sisu.count("hello")
faili_sisu = faili_sisu.replace("Hello","Tere")
faili_sisu = faili_sisu.replace("hello","tere")
failinimi=input("sisestage lähtefaili nimi: ")
fail2 = open(failinimi,"w")
fail2.write(faili_sisu)
print("uue faili nimi on tõlgitud.txt")
fail2.close()
c = a+b
print("vahetati "+ str(c) +" hello-t välja")   
