import string
import random
def suurv�ike(s�ne):
    uus_s�ne =""
    juhuslik_s�mbol = random.choice(string.punctuation)
    for t�hem�rk in s�ne:
        if (t�hem�rk.isupper()) == True:
            uus_s�ne += (t�hem�rk.lower())
        elif (t�hem�rk.islower()) == True:
            uus_s�ne += (t�hem�rk.upper())
        elif (t�hem�rk.isspace()) == True:
            uus_s�ne += t�hem�rk
        elif t�hem�rk in string.punctuation:
            s�mboli_muutus = t�hem�rk.replace(t�hem�rk, juhuslik_s�mbol)
            uus_s�ne += s�mboli_muutus    
    return uus_s�ne
