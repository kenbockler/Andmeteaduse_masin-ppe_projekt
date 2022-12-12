username=input("Palun vali endale kasutajanimi: ")
pass1=input("Palun vali endale parool: ")
pass2=input("Palun korda oma parooli: ")
while True:
    if pass1==pass2:
        if len(pass1)>=8:
            nr=sum(i.isdigit() for i in pass1)
            if nr>0 and nr!=len(pass1):
                ssap1=reversed(pass1)
                f=open("users.txt","w")
                f.write(username)
                f.write(":")
                for i in ssap1:
                    f.write(i)
                f.close()
                break
            else:
                pass1=input("Palun vali endale parool mis sisaldab nii tähti kui numbreid: ")
                pass2=input("Palun korda oma parooli: ")
        else:
            pass1=input("Palun vali endale pikem parool: ")
            pass2=input("Palun korda oma parooli: ")
    else:
        pass1=input("Sinu sisestatud paroolid ei kattu. Palun vali endale parool: ")
        pass2=input("Palun korda oma parooli: ")
                