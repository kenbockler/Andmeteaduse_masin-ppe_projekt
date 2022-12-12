from random import randint
def minu_shuffle(järjend):
    if järjend != []:
        for i in range(20):
            kust = randint(0, len(järjend)-1)
            arv1 = järjend[kust]
            kuhu = randint(0, len(järjend)-1)
            arv2 = järjend[kuhu]
            if kust == kuhu:
                continue
            else:
                järjend[kust] = arv2
                järjend[kuhu] = arv1