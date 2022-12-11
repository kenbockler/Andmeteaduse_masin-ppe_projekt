import string
import random
b = "MinA oleN Tubli!!"
def suvalinepunkts():
    for i1 in b:
        s1 = str(i1)
        l1 = "0"
        if s1 in string.punctuation:
            l1 = random.choice(string.punctuation)
        if s1 in string.punctuation:
            break
    return l1
o = str(suvalinepunkts())
def suurväike(a):
    list = []
    for i in a:
        s = str(i)
        m = s
        l = "0"
        if s == s.upper():
            l = m.lower()
        if s == s.lower():
            l = m.upper()
        if s in string.punctuation:
            l = o
        list.append(l)
    j = "".join(list)
    return j
print(suurväike(b))