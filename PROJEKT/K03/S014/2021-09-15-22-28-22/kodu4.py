import time
f=open("kinganumbrid.txt")
while True:
    try:
        kinganumber=float(f.readline())
        jalalaba=float(round(2/3*(kinganumber-2),2))
        print(jalalaba)
    except:
        print("Paha lugu, failis on midagi k�est l�inud. Ehk kirjutasid sinna m�ne arvu asemele hoopis lemmikpoliitiku nime? Kontrolli �le, kas failis on k�ik ikka arvud!")
        time.sleep(3)
        break
f.close()
print("Jooksis l�puni, jee!")
