from turtle import*
import random
hulknurki = 30
while hulknurki > 0:
    hulknurki -= 1
    arv_k�lgi = random.randint(3, 20)
    k�ljepikkus = random.randint(10, 100)
    def hulknurk(arv_k�lgi, k�ljepikkus):
        joonistatud_k�lgi = 0
        while joonistatud_k�lgi < arv_k�lgi:
            forward(k�ljepikkus)
            left(360/arv_k�lgi)
            joonistatud_k�lgi += 1
    hulknurk(arv_k�lgi, k�ljepikkus)
    penup()
    left(random.randint(1, 360))
    forward(random.randint(70, 100))
    pendown()