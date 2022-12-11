import time
f=open("kinganumbrid.txt")
while True:
    try:
        kinganumber=float(f.readline())
        jalalaba=float(round(2/3*(kinganumber-2),2))
        print(jalalaba)
    except:
        print("Paha lugu, failis on midagi käest läinud. Ehk kirjutasid sinna mõne arvu asemele hoopis lemmikpoliitiku nime? Kontrolli üle, kas failis on kõik ikka arvud!")
        time.sleep(3)
        break
f.close()
print("Jooksis lõpuni, jee!")
