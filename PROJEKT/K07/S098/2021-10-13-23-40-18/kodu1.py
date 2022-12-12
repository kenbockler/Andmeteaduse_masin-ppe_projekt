juhuu = ['Mati P', 'Kati T', 'Siim Aleksander P', 'Jüri P', 'Veronika T']
def poisse_ja_tüdrukuid(x):
    n = str(x)
    a = n.split()
    b = n.count('P')
    c= n.count('T')
    return (b , c)
print(poisse_ja_tüdrukuid(juhuu))
