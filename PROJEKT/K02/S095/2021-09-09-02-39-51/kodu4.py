x=input("""Sisesta(kirjuta) teksti fail, kus soovid "Hello" asendada sõnaga "Tere": """)
y=input("Sisesta uue faili nimi, kuhu läheb muudetud text: ")
f= open('hello.txt', 'r+')
faili_sisu= f.read()
print(faili_sisu)
print("Muudeti",faili_sisu.count('Hello'),"rida")
f.write(faili_sisu.replace("Hello","Tere"))
f=open("tere.txt", "a+")
f.write(faili_sisu.replace("Hello","Tere"))
print(faili_sisu)
f.close()
f.close()