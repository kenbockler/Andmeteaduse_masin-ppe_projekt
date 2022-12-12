def suurväike(inputString):
    def replace(text):
        from random import randint
        a = randint(1,32)
        symbol = "!\"
        return text.replace("!",symbol).replace("\"",symbol).replace("
    return replace(inputString.swapcase())