f=open("taksohinnad.txt",encoding="UTF-8")
tee_pikkus_koju = float(input("Sisesta tee pikkus kilomeetrites: "))
rida=f.readline()
a=rida.strip("\n").split(",")
if rida=="":
    taksosse_sisisenemise_hind=0
    kilomeetri_hind=0
else:    
    taksosse_sisisenemise_hind=float(a[1])
    kilomeetri_hind=float(a[2])
taksosõit_koju= taksosse_sisisenemise_hind+(tee_pikkus_koju*kilomeetri_hind)
miinimum=taksosõit_koju
f.close()
f=open("taksohinnad.txt",encoding="UTF-8")
if rida=="":
    print("Kahjuks taksod puuduvad.")
else:
    for rida in f:
        a=rida.strip("\n").split(",")
        takso_firma=a[0]
        taksosse_sisisenemise_hind=float(a[1])
        kilomeetri_hind=float(a[2])
        taksosõit_koju= taksosse_sisisenemise_hind+(tee_pikkus_koju*kilomeetri_hind)
        if taksosõit_koju<=miinimum:
            miinimum=taksosõit_koju
            vastav_firma=takso_firma
    print("Kõige odavam on "+vastav_firma+".")
f.close()