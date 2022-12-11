import string
import random
def suurväike(x):
    kirjavahemärk = random.choice(string.punctuation)
    for mark in string.punctuation:
        x = x.replace(mark, kirjavahemärk)
    print(x.swapcase())
    