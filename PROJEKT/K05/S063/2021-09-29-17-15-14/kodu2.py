'''
Kirjuta funktsioon suurväike, mis võtab argumendiks mingi sõne ning tagastab sõne järgmisel kujul:
suured tähed on muudetud väikeseks;
väikesed tähed on muudetud suureks;
kõik kirjavahemärkide sümbolid on asendatud mingi ühe ja sama juhusliku kirjavahemärgisümboliga.
'''
import string
import random
def suurväike(sone):
    teisendatud = ""
    kirjavahemargid = string.punctuation
    juhuslik_kirjavahemark = random.choice(kirjavahemargid)
    for s in sone:
        if s.islower():
            s = s.upper()
        elif s.isupper():
            s = s.lower()
        elif s in kirjavahemargid:
            s = juhuslik_kirjavahemark
        teisendatud += s
    return teisendatud