import string
import random
suurväike=input("Sisesta sõne:")
suurväike.swapcase()
for string.punctuation in suurväike:
string.punctuation.replace(string.punctuation,random.choice(string.punctuation))
print(suurväike)