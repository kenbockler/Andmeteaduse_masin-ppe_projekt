def v�ljasta_liin(eellane, j�rglane, s�nastik):
    t�ene = True
    if eellane == j�rglane:
        print(eellane)
        return True
    if j�rglane in s�nastik:
        for vanem in s�nastik[j�rglane]:
            if v�ljasta_liin(eellane, vanem, s�nastik):
                print(j�rglane)
                return True
    return False
s�nastik = {
 'Kalle': ('Teet', 'Maris'),
 'Maris': ('Konstantin', 'Mari'),
 'Rita': ('Teet', 'Maris'),
 'Siim': ('Teet', 'Maris'),
 'Mari': ('Karl', 'Leeni'),
 'Teet': ('Joosep', 'Adele'),
 'Adele': ('Johannes', 'Leida'),
 'Konstantin': ('Viktor', 'Jelena'),
 'Joosep': ('August', 'Emma'),
 'Viktor': ('Nikolai', 'Maria')
}
print(v�ljasta_liin("Jelena", "Leeni", s�nastik))