from math import *
pikkus = int(input("Sisestage liini pikkus: "));
postivahe = int(input("Sisestage liinil olevate postide maksimaalne vahe: "));
var1 = ceil(pikkus / postivahe) + 1;
if(var1 < 2):
    var1 = 2;
print(var1)
