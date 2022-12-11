from random import randint
from math import floor
def minu_shuffle(a):
    eelmine_suvaindeks=0
    suvaindeks=randint(0, len(a)-1)
    eelmine_asuva=0
    i=0
    while i < floor(len(a)/2):
        suvaindeks=randint(0, len(a)-1)
        if suvaindeks==eelmine_suvaindeks or suvaindeks==i or eelmine_asuva==a[suvaindeks]:
            continue
        algne_a=a[i]
        a[i]=a[suvaindeks]
        a[suvaindeks]=algne_a
        eelmine_asuva=a[suvaindeks]
        eelmine_suvaindeks=suvaindeks
        i+=1