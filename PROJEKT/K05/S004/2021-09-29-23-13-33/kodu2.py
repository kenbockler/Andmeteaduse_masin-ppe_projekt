import random
import string
a=[]
for x in string.punctuation:
    a.append(x)
def suurv�ike(sisend):
    v�ljund=""
    b=a[random.randint(0,len(a)-1)]
    for x in sisend:
        if x.isupper():
            v�ljund += x.lower()
        if x.islower():
            v�ljund += x.upper()
        if x == " ":
            v�ljund += " "
        if (x in a):
            v�ljund += b
    return(v�ljund)
print(suurv�ike("dsa dasdas ...."))