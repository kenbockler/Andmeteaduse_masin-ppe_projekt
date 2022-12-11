def suurväike(sõne):
    import string
    märk = string.punctuation
    print(sõne.swapcase().replace(märk, '
sõne = input("Kirjuta siia midagi: ")
print(suurväike(sõne))
