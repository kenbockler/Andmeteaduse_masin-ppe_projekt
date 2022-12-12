import string
import random
sv = input("Sisesta siia lause mida soovid muuta: ")
märgid = string.punctuation
def suurväike(sv):
    random_symbol = random.choice(märgid)
    muudetud_lause = sv.swapcase()
    for i in märgid:
        muudetud_lause = muudetud_lause.replace(i , random_symbol)
    return muudetud_lause
muudetud_lause = suurväike(sv)
print(muudetud_lause)