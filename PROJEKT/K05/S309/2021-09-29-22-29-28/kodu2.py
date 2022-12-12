import random
def suurväike(workstring):
    newstring = ""
    newconnector = random.choice('!"
    for letter in workstring:
        if(letter.isupper() and (letter.isalpha() or letter == " ")):
            newstring += letter.lower()
        elif(letter.islower) and (letter.isalpha()  or letter == " "):
            newstring += letter.upper()
        for i in ('!"
            if(letter == i):
                newstring += newconnector
                break
    return newstring