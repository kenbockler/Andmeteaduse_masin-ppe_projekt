from random import randint
import string
s�ne = input ("Sisestage oma tekst! ")
def suurv�ike (s�ne):
    muutunuds�ne = ""
    for t�ht in s�ne:
        if t�ht.isupper():
           muutunuds�ne += t�ht.lower()
        elif t�ht.islower():
            muutunuds�ne += t�ht.upper()
        elif t�ht in string.punctuation:
            nr = randint (1, 3)
            if nr == 1:
                if t�ht != ",":
                    muutunuds�ne += ","
                else:
                    muutunuds�ne += "&"
            elif nr == 2:
                if t�ht != "!":
                    muutunuds�ne += "!"
                else:
                    muutunuds�ne += "?"
            elif nr == 3:
                if t�ht != ":":
                    muutunuds�ne += ":"
                else:
                    muutunuds�ne += "/"
        else:
            muutunuds�ne += t�ht
    return muutunuds�ne
print (suurv�ike(s�ne))