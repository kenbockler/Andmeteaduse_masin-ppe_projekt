def poisse_ja_t�drukuid(a):
    for i in range(len(a)):
        a[i] = a[i][-1]
    return (a.count("P"),a.count("T"))
print(poisse_ja_t�drukuid(['Mati P', 'Kati T', 'Siim Aleksander P', 'J�ri P', 'Veronika T']))
print(poisse_ja_t�drukuid([]))