from math import *
liini_pikkus = float(input('Sisesta liini pikkus t�isarvuna meetrites '))
kaugus = float(input('Sisesta k�rvutiasetsevate postide maksimaalkaugus meetrites '))
if liini_pikkus < kaugus:
    print('Minimaalne postide arv liini ehitamiseks on', 2)
else:
    print('Minimaalne postide arv liini ehitamiseks on ',(ceil(liini_pikkus / kaugus)) + 1)