fail = open("taksohinnad.txt", encoding="UTF-8")
s = float(input("Sisesta s�idetav teepikkus: "))
maksilisti = []
s�bralisti = []
waldolisti = []
for rida in fail:
    maksilisti = (rida).strip().split(",")
    rida2 = fail.readline().strip()
    s�bralisti = (rida2).split(",")
    rida3 = fail.readline().strip()
    waldolisti = (rida3).split(",")
hind1 = (float(maksilisti[1]) + float(maksilisti[2])* s)
hind2 = (float(s�bralisti[1]) + float(s�bralisti[2])* s)
hind3 = (float(waldolisti[1]) + float(waldolisti[2])* s)
if hind1 < hind2 and hind1 < hind3:
    print ("Maksitakso oleks k�ige odavam")
elif hind2 < hind1 and hind2 < hind3:
    print ("S�bratakso on k�ige odavam")
elif hind3 < hind1 and hind3 < hind2:
    print ("Waldo takso on k�ige odavam")