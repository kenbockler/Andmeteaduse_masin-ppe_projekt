from turtle import *
def ruutude_fraktal(s�gavus):
    if s�gavus == 0:
        return
    global laius, suund
    for i in range(3):
        forward(laius)
        if s�gavus > 1:
            laius = laius/2
            suund = -suund
            ruutude_fraktal(s�gavus-1)
            suund = -suund
            laius *= 2
        right(suund)
    forward(laius)
    right(suund)
laius = 100
suund = 90
ruutude_fraktal(5)
exitonclick()
  