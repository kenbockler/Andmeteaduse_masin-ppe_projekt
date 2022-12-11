liini_pikkus = int(input("Sisesta liini pikkus meetrites: "))
max_postide_kaugus = int(input("Sisesta kõrvutiasetsevate postide maksimaalkaugus meetrites: "))
vastus = int(liini_pikkus / max_postide_kaugus)
jäägiga_vastus = (liini_pikkus / max_postide_kaugus)
if vastus == jäägiga_vastus and vastus != 1 and vastus != 2:
    print(int(vastus))
elif vastus != jäägiga_vastus and jäägiga_vastus != 1 and jäägiga_vastus != 2:
    print(int(vastus)+2)
elif jäägiga_vastus == 1 or jäägiga_vastus == 2:
    print(int(vastus)+1)