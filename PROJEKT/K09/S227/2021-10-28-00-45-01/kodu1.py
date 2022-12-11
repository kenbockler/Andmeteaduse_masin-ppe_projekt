from statistics import harmonic_mean
read=open("aktsiad.txt")
alghinnad=[]
kuupäevad=[]
for i in read.readlines():
    kuupäevad+=[i.split(",")[0].strip()]
    alghinnad+=[float(i.split(",")[-1].rstrip("\n").lstrip())]
def silu_andmed(alghinnad,y):
    vahetulem=[]
    abilist=[]
    abi=0
    for i in alghinnad:
        if abi != y:
            abilist=abilist+[i]
            vahetulem+=[harmonic_mean(abilist)]
            abi+=1
        else:
            abilist.append(i)
            abilist.pop(0)
            vahetulem+=[harmonic_mean(abilist)]
    return vahetulem
read.close()
pt.show()