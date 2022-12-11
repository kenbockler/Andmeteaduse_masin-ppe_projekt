from random import randint
def suurväike(sõna):
    töödeldud_sõna = ""
    märgid = '!"
    juhuslik_märk = märgid[randint(0,len(märgid))]
    for i in range(len(sõna)):
        karakter = sõna[i]
        if karakter.isalpha():
            if karakter.isupper():
                töödeldud_sõna += karakter.lower()
            else:
                töödeldud_sõna += karakter.upper()
        elif karakter == " ":
            töödeldud_sõna += " "
        else:
            töödeldud_sõna += juhuslik_märk
    return töödeldud_sõna
