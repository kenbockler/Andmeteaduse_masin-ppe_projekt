from random import randint
import copy
def minu_shuffle(a): 
    indeksi_pikkus=len(a)
    uus_indeks=[]
    b=copy.deepcopy(a)
    vana_indeks=[]
    i=indeksi_pikkus
    for e in range(0,indeksi_pikkus):
        vana_indeks+=[e]
    while i>0:
        n=randint(0, indeksi_pikkus-1)
        if n not in uus_indeks:
            uus_indeks+=[n]
            i-=1
    for el in range(0,indeksi_pikkus):
        a[vana_indeks[0]]=b[uus_indeks[0]]
        del uus_indeks[0]
        del vana_indeks[0]
