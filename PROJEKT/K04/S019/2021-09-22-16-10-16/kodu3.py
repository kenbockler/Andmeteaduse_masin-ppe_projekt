from turtle import *
k�lgede_arv = int(input("Sisestage k�lgede arv: "))
k�ljepikkus = int(input("Sisestage k�ljepikkus: "))
i = 0
nurk = 180 -(((k�lgede_arv - 2) * 180) / k�lgede_arv)
while i < k�lgede_arv:
    forward(k�ljepikkus)
    left(nurk)
    i = i + 1