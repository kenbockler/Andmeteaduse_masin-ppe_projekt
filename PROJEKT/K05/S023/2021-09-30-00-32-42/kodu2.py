import string
import random
a = input("Sisestage s�na: ")
def suurv�ike(a):
    uuss�na = ""
    kirjavahem�rgid = []
    for j in string.punctuation:
        kirjavahem�rgid.append(j)
    suvalinem�rk = random.choice(kirjavahem�rgid)
    for i in range(len(a)):
        if a[i].isupper():
            uuss�na = uuss�na + a[i].lower()
        elif a[i].islower():
            uuss�na = uuss�na + a[i].upper()
        elif a[i] in kirjavahem�rgid:
            uuss�na = uuss�na + suvalinem�rk
        else:
            uuss�na = uuss�na + a[i]
    return uuss�na
print(suurv�ike(a))