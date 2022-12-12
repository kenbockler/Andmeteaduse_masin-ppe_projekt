import os
kaugus = float(input("Sisesta kodu kaugus: "))
f_suurus = "taksohinnad.txt"
if os.path.getsize(f_suurus) == 0:
    print("Fail on tühi.")
elif kaugus == 0:
    print ("Mine jala.")
else:
    f = open("taksohinnad.txt")
    def hind(kaugus, f):
        vähim_hind = 100000000000
        for rida in f:
            rida = rida.strip("\n")
            rida = rida.split(",")
            start = float(rida[-2])
            km_hind = float(rida[-1])
            hind = start + kaugus * km_hind
            takso = rida[0]
            if hind < vähim_hind:
                vähim_hind = hind
                odavaim_takso = takso
            else:
                odavaim_takso = odavaim_takso     
        return odavaim_takso
    print("Odavaim takso on " + hind(kaugus, f))
