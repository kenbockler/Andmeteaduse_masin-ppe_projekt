from random import sample
def bingo():
    while True:
        loosime_3 = sample(range(1,11), 3)
        loosime_2 = sample(range(11,21), 2)
        loosinumbrid = loosime_3 + loosime_2
        if "1" and "2" and "3" in loosinumbrid:
            continue
        else:
            break
    return loosinumbrid
