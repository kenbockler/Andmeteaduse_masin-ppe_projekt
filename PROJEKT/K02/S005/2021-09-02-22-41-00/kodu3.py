firstname = input("Eesnimi?").lower()
lastname = input("Perekonnanimi?").lower()
def letterhandler(word):
    return word.replace("�", "o").replace("�", "a").replace("�", "o").replace("�", "u").replace(" ", "").strip()
firstname = letterhandler(firstname)
lastname = letterhandler(lastname)
print(firstname + "." + lastname)