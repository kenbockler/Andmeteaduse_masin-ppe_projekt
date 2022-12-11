def poisse_ja_tüdrukuid(a):
    for i in range(len(a)):
        a[i] = a[i][-1]
    return (a.count("P"),a.count("T"))
print(poisse_ja_tüdrukuid(['Mati P', 'Kati T', 'Siim Aleksander P', 'Jüri P', 'Veronika T']))
print(poisse_ja_tüdrukuid([]))