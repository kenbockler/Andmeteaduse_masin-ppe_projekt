firstname = input("Eesnimi?").lower()
lastname = input("Perekonnanimi?").lower()
def letterhandler(word):
    return word.replace("õ", "o").replace("ä", "a").replace("ö", "o").replace("ü", "u").replace(" ", "").strip()
firstname = letterhandler(firstname)
lastname = letterhandler(lastname)
print(firstname + "." + lastname)