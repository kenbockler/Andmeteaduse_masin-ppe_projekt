import random
def suurväike(sone):
    uus_sone=""
    suvaline_kirjavahemark=random.choice(['"',"'",".","?","!",",",":",";","-","(",")","{","}","[","]","/"])
    for taht in sone:
        if (taht.isupper())==True:
            uus_sone+=(taht.lower())
        elif (taht.islower())==True:
            uus_sone+=(taht.upper())
        elif (taht.isspace())==True:
            uus_sone+=taht
        elif taht in ('"',"'",".","?","!",",",":",";","-","(",")","{","}","[","]","/"):
            uus_sone+=suvaline_kirjavahemark
    return uus_sone
print(suurväike( '! ! " " ' ' ( ( ) ) , , - - . . / / : : ; ; ? ? [ [ ] ]'))