nimi=input("Sisestage kasutajanimi: ")
def parool1():
    parool1=input("Sisestage parool: ")
    return(parool1)
def parool2():
    parool2=input("Sisestage parool uuesti: ")
    return(parool2)
salasõna1=parool1()
salasõna2=parool2()
while True:
    if salasõna1==salasõna2:
        if len(salasõna1)>=8:
            if any(täht.isalpha() for täht in salasõna1):
                if any(täht.isdecimal() for täht in salasõna1):
                    loorap=salasõna1[::-1]
                    f=open("users.txt", "w")
                    f.write(nimi+":"+ loorap)
                    f.close()
                    break
                else:
                    salasõna1=parool1()
                    salasõna2=parool2()
            else:
                salasõna1=parool1()
                salasõna2=parool2()
        else:
            salasõna1= parool1()            
            salasõna2= parool2()
    else:
        salasõna1=parool1()        
        salasõna2=parool2()
        