import string
import random
def suurv�ike(s�ne):
    s�mbolid = string.punctuation
    suvaline_s�mbol = random.choice(string.punctuation)
    uus_s�ne = ''
    for a in s�ne:
        if (a.isupper()) == True:
            uus_s�ne += (a.lower())
        elif (a.islower()) == True:
            uus_s�ne += (a.upper())
        elif (a.isspace()) == True:
            uus_s�ne += a
        elif a in s�mbolid:
            uus_s�ne += suvaline_s�mbol
    return uus_s�ne