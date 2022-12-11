import string
import random
string.punctuation = '!
punctuation = random.choice('!
def suurväike(x):
    x = x.replace(string.punctuation, punctuation)
    return str.swapcase(x)