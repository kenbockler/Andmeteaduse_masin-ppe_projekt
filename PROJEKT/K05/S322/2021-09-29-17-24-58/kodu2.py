import string, random
def suurväike(sõne):
    suurtähed = "ABCDEFGHIJKLMNOPQRSŠZŽTUVWÕÄÖÜXY"
    väiketähed = "abcdefghijklmnopqrsšzžtuvwõäöüxy"
    kirjavahemärgid = string.punctuation
    asendusmärk = kirjavahemärgid[random.randint(0, len(kirjavahemärgid) - 1)]
    uus = ""
    for i in range(len(sõne)):
        vanapikkus = len(uus)
        for j in range(len(suurtähed)):
            if suurtähed[j] == sõne[i]:
                uus += väiketähed[j]
                break
        for j in range(len(väiketähed)):
            if väiketähed[j] == sõne[i]:
                uus += suurtähed[j]
                break
        for j in range(len(kirjavahemärgid)):
            if kirjavahemärgid[j] == sõne[i]:
                uus += asendusmärk
                break
        if vanapikkus == len(uus):
            uus += sõne[i]
    return uus
